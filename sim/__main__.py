from datetime import datetime
from collections import Counter, defaultdict, OrderedDict
from itertools import chain

import numpy as np
from cma import CMAEvolutionStrategy
from loguru import logger
from math import sqrt
from sklearn.preprocessing import MinMaxScaler
from trueskill import BETA, global_env, rate_1vs1, Rating
from xgboost import XGBRegressor

from .data import DATA
from .data_2016 import DATA_2016
from .data_2017 import DATA_2017
from .data_2018 import DATA_2018


def win_probability(team1, team2):
    delta_mu = sum(r.mu for r in team1) - sum(r.mu for r in team2)
    sum_sigma = sum(r.sigma ** 2 for r in chain(team1, team2))
    size = len(team1) + len(team2)
    denom = sqrt(size * (BETA * BETA) + sum_sigma)
    ts = global_env()
    return ts.cdf(delta_mu / denom)


def to_decimal_odds(us_odds):
    if us_odds > 0:
        return us_odds / 100 + 1
    else:
        return 100 / us_odds + 1


def to_implied_odds(us_odds: float) -> float:
    decimal_odds = to_decimal_odds(us_odds)
    try:
        return 1 / decimal_odds
    except ZeroDivisionError:
        return 1


def get_regressor(training_data, label_data, scaler, estimators=100, max_depth=3):
    """get regressor"""
    #logger.info('')
    #logger.info('Training model...')

    # scale
    scaler.partial_fit(training_data)
    X_train = scaler.transform(training_data)
    y_train = label_data

    # train
    # reg = GradientBoostingRegressor(n_estimators=1000)
    # reg = reg.fit(X_train, y_train)
    # # mse = mean_squared_error(y_test, reg.predict(X_test))
    # # #logger.info(f'MSE: {mse:.2f}')
    # y_pred = reg.predict(X_test)
    # y_pred_bin = [round(value) for value in y_pred]
    # accuracy = accuracy_score(y_test, y_pred_bin)
    # #logger.info(f'Accuracy score: {accuracy*100:.0f}%')
    # sleep(2)

    reg = XGBRegressor(n_estimators=estimators, max_depth=max_depth, objective='reg:squarederror', n_jobs=4)
    reg = reg.fit(X_train, y_train)
    # y_pred = reg.predict(X_test)
    # y_pred_bin = [round(value) for value in y_pred]
    # accuracy = accuracy_score(y_test, y_pred_bin)
    # #logger.info(f'Accuracy score: {accuracy*100:.0f}%')
    # mse = mean_squared_error(y_test, y_pred)
    # #logger.info(f'MSE: {mse:.2f}')
    # sleep(3)
    # pyplot.bar(range(len(model.feature_importances_)), model.feature_importances_)
    # pyplot.show()

    return reg


def main(bet_params):
    #logger.info('Starting main training')

    all_data = DATA_2016 + DATA_2017 + DATA_2018 + DATA
    estimators, max_depth, bet_pred_a, bet_pred_b, bet_odds_a, bet_odds_b = bet_params
    if estimators > 5:
        estimators = 5 - (estimators - 5) * 2
    estimators = max(int(round(estimators * 100)), 10)
    max_depth = max(int(round(max_depth)), 1)

    # init
    reg = None
    scaler = MinMaxScaler()
    cutoff = int(len(all_data) * 0.7)
    start_date = None
    ratings = defaultdict(lambda: Rating())
    early_fights = defaultdict(lambda: 0.5)
    last_fights = defaultdict(lambda: 0.5)
    training_data = []
    label_data = []
    X_test = []
    y_test = []
    payouts = []
    bet_amts = []
    accuracy = (0, 0)
    tab = []
    tab_amts = []
    actual = (0, 0)
    bet_multis = []
    bet_multis_cat = []

    # loop through scenes
    for i, scene in enumerate(all_data):
        is_training = i < cutoff
        if not is_training:
            if not reg:
                start_date = datetime.strptime(scene['date'], '%Y-%m-%d')
                reg = get_regressor(training_data, label_data, scaler, estimators=estimators, max_depth=max_depth)
            #logger.info('')
        #logger.info(f'{scene["date"]} {scene["name"]}')

        for fight in scene['fights']:
            bet_size = 5
            # skip if no odds:
            if 'odds' not in fight:
                continue

            f1 = fight['fighters'][0]['name']
            f2 = fight['fighters'][1]['name']

            f1_odds = fight['odds'][f1]
            f2_odds = fight['odds'][f2]
            if not -50 < f1_odds < 50 or not -50 < f2_odds < 50:
                raise ValueError(f'surely these odds are wrong? {f1_odds} {f2_odds}')

            win1_prob = win_probability([ratings[f1]], [ratings[f2]])
            win2_prob = win_probability([ratings[f2]], [ratings[f1]])

            # wins and losses
            wins_and_losses_1 = fight['fighters'][0]['stats'].split('-')
            wins_and_losses_2 = fight['fighters'][1]['stats'].split('-')

            fight_data = [
                [
                    win1_prob,
                    f1_odds,
                    f2_odds,
                    ratings[f1].mu,
                    ratings[f2].mu,
                    ratings[f1].sigma,
                    ratings[f2].sigma,
                    last_fights[f1],
                    last_fights[f2],
                    early_fights[f1],
                    early_fights[f2],
                    wins_and_losses_1[0],
                    wins_and_losses_2[0],
                    wins_and_losses_1[1],
                    wins_and_losses_2[1],
                ],
                [
                    win2_prob,
                    f2_odds,
                    f1_odds,
                    ratings[f2].mu,
                    ratings[f1].mu,
                    ratings[f2].sigma,
                    ratings[f1].sigma,
                    last_fights[f2],
                    last_fights[f1],
                    early_fights[f2],
                    early_fights[f1],
                    wins_and_losses_2[0],
                    wins_and_losses_1[0],
                    wins_and_losses_2[1],
                    wins_and_losses_1[1],
                ]
            ]

            ##########################################
            # update data
            if 'winner' in fight:
                # get winner
                fw = fight['winner']['fighter']
                is_win_1 = fw == f1
                fl = f2 if is_win_1 else f1
                if not is_win_1 and fw != f2 and fw is not None:
                    raise ValueError(f'unknown winner {fw}')
                drawn = fw is None

                # update fights
                early_fights[fw] = last_fights[fw]
                early_fights[fl] = last_fights[fl]
                last_fights[fw] = 1
                last_fights[fl] = 0

                # update ratings
                ratings[fw], ratings[fl] = rate_1vs1(ratings[fw], ratings[fl], drawn=drawn)

            ###################################
            # train
            if is_training:
                training_data.extend(fight_data)
                label_data.extend([is_win_1, not is_win_1])

            ###################################
            # test
            else:
                scaled_fight_data = scaler.transform(fight_data)
                pred1, pred2 = reg.predict(scaled_fight_data)

                #############################
                # bet scaling
                bet_multi = 1

                # pred max
                pred_max = max(pred1, pred2)
                bet_pred_multi = np.polyval([bet_pred_a, bet_pred_b], [pred_max])[0]
                bet_pred_multi = int(min(max(round(bet_pred_multi), 0), 3))
                bet_multi += bet_pred_multi
                bet_multis_cat.append(f'bet_pred_multi-{bet_pred_multi}')

                # odds diff
                odds_diff = abs(1 / f1_odds - 1 / f2_odds)
                bet_odds_multi = np.polyval([bet_odds_a, bet_odds_b], [odds_diff])[0]
                bet_odds_multi = int(min(max(round(bet_odds_multi), 0), 3))
                bet_multi += bet_odds_multi
                bet_multis_cat.append(f'bet_odds_multi-{bet_odds_multi}')

                bet_multis.append(bet_multi)
                bet_size *= bet_multi
                bet_amts.append(bet_size)
                #############################

                # prediction made
                if 'prediction' in fight and fight['prediction'] is None:
                    if pred1 > pred2:
                        exp_winner = f1
                        pred_exp_winner = pred1
                        exp_loser = f2
                        pred_exp_loser = pred2
                    else:
                        exp_winner = f2
                        pred_exp_winner = pred2
                        exp_loser = f2
                        pred_exp_loser = pred1
                    #logger.warning(f'[{pred_exp_winner * 100:.0f}% vs {pred_exp_loser * 100:.0f}%] Bet x{bet_multi} on {exp_winner} to beat {exp_loser} [{ratings[exp_winner].mu:.0f} vs {ratings[exp_loser].mu:.0f}]')
                    continue

                # good luck with your bets
                elif 'winner' not in fight:
                    #logger.warning(f'Pending {f1} vs {f2}')
                    continue

                if is_win_1:
                    fw_pred = pred1
                    fl_pred = pred2
                else:
                    fw_pred = pred2
                    fl_pred = pred1

                # add test data
                X_test.extend(scaled_fight_data)
                y_test.extend([is_win_1, not is_win_1])

                # testing outcome
                correct = 0
                payout = -bet_size
                if is_win_1 and pred1 > pred2:
                    correct = 1
                    payout += f1_odds * bet_size
                elif not is_win_1 and pred2 > pred1:
                    correct = 1
                    payout += f2_odds * bet_size
                payouts.append(round(payout, 2))
                accuracy = (accuracy[0] + correct, accuracy[1] + 1)

                # actual outcome
                if 'bet' in fight:
                    is_actual_correct = fight['prediction'] == fw
                    actual = (actual[0] + is_actual_correct, actual[1] + 1)
                    cash = -fight['bet']
                    if is_actual_correct:
                        fw_odds = f1_odds if is_win_1 else f2_odds
                        cash += fw_odds * fight['bet']
                    tab.append(round(cash, 2))
                    tab_amts.append(fight['bet'])

                log_balance = f'[{sum(payouts):.0f}|{payout:.0f}]'
                log_pred = f'[{fw_pred * 100:.0f}% vs {fl_pred * 100:.0f}%]'
                log_fight = f'x{bet_multi} {fw} {fight["winner"]["by"]} {fl}'
                log_ratings = f'[{ratings[fw].mu:.0f} vs {ratings[fl].mu:.0f}]'
                #logger.info(f'{log_balance} {log_pred} {log_fight} {log_ratings}')

    ###################################
    # Summary

    #logger.info('')
    #logger.info('Tree info:')
    params = reg.get_params()
    #logger.info(f'Num estimators: {params["n_estimators"]}')
    #logger.info(f'Learning rate: {params["learning_rate"]:.2f}')
    #logger.info(f'Max depth: {params["max_depth"]}')
    #logger.info(f'Accuracy: {reg.score(X_test, y_test)*100:.0f}%')
    feature_names = [
        'win%',
        'odds', '~odds',
        'mu', '~mu',
        'sigma', '~sigma',
        'last', '~last',
        'early', '~early',
        'wins', '~wins',
        'losses', '~losses',
    ]
    features = {k: round(v, 2) for k, v in zip(feature_names, reg.feature_importances_)}
    #logger.info(f'Features: {features}')

    if accuracy[1]:
        payouts = np.array(payouts)
        #logger.info('')
        #logger.info('Testing:')
        #logger.info(f'Accuracy {accuracy[0]}/{accuracy[1]} = {accuracy[0]/accuracy[1]*100:.1f}%')
        logger.info(f'ROI {sum(payouts) / sum(bet_amts) * 100:.1f}%  Profit ${sum(payouts):.0f}')
        days = (datetime.now() - start_date).days
        #logger.info(f'Profit: per day: ${sum(payouts) / days:.2f}  per bet ${payouts.mean():.2f}')
        #logger.info(f'Common multis: {Counter(bet_multis).most_common(4)}')
        logger.info(f'cat multis: {Counter(bet_multis_cat).most_common()}')

    if actual[1]:
        tab = np.array(tab)
        #logger.info('')
        #logger.info('Actual:')
        #logger.info(f'Accuracy {actual[0]}/{actual[1]} = {actual[0]/actual[1] * 100:.1f}%')
        #logger.info(f'ROI {sum(tab) / sum(tab_amts) * 100:.2f}%  Profit ${sum(tab):.0f}')
        days = (datetime.now() - datetime(2019, 7, 13)).days
        #logger.info(f'Profit: per day: ${sum(tab) / days:.2f}  per bet ${tab.mean():.2f}')

    #logger.info('Done')
    return -(sum(payouts) / sum(bet_amts))


if __name__ == '__main__':
    bet_params_names = ['estimators', 'max depth',
                        'pred a', 'pred b',
                        'odds a', 'odds b']

    # bet_params = [2.653610696129586, 7.305015952243274, -3.1458427161818197, -7.247389262630655, -4.620856940161052, 1.928048253817689]
    bet_params = [2.665725804641588, 7.234505663761268, -3.331866015990036, -7.061660174861657, -4.605967770542017, 1.9248558611582418]

    assert len(bet_params) == len(bet_params_names)

    train = 1

    if not train:
        main(bet_params)
    else:
        es = CMAEvolutionStrategy(bet_params, 1)
        while not es.stop():
            solutions = es.ask()
            fitness = [main(x) for x in solutions]
            es.tell(solutions, fitness)
            es.disp()
            print(list(es.result[0]))
            print(list(es.result[5]))
        es.result_pretty()

        print('')
        print('best')
        print(list(es.result[0]))

        print('')
        print('xfavorite: distribution mean in "phenotype" space, to be considered as current best estimate of the optimum')
        print(list(es.result[5]))
