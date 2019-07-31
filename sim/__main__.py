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


def get_regressor(training_data, label_data, scaler, estimators=100):
    """get regressor"""
    # scale
    scaler.partial_fit(training_data)
    X_train = scaler.transform(training_data)
    y_train = label_data

    # train
    # reg = GradientBoostingRegressor(n_estimators=1000)
    # reg = reg.fit(X_train, y_train)
    # # mse = mean_squared_error(y_test, reg.predict(X_test))
    # # logger.info(f'MSE: {mse:.2f}')
    # y_pred = reg.predict(X_test)
    # y_pred_bin = [round(value) for value in y_pred]
    # accuracy = accuracy_score(y_test, y_pred_bin)
    # logger.info(f'Accuracy score: {accuracy*100:.0f}%')
    # sleep(2)

    reg = XGBRegressor(n_estimators=estimators, objective='reg:squarederror', n_jobs=4)
    reg = reg.fit(X_train, y_train)
    # y_pred = reg.predict(X_test)
    # y_pred_bin = [round(value) for value in y_pred]
    # accuracy = accuracy_score(y_test, y_pred_bin)
    # logger.info(f'Accuracy score: {accuracy*100:.0f}%')
    # mse = mean_squared_error(y_test, y_pred)
    # logger.info(f'MSE: {mse:.2f}')
    # sleep(3)
    # pyplot.bar(range(len(model.feature_importances_)), model.feature_importances_)
    # pyplot.show()
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
    # for name, val in zip(feature_names, reg.feature_importances_):
    #     logger.info(f'{name}: {val}')

    return reg


def main(bet_params):
    logger.info('Starting main training')

    all_data = DATA_2016 + DATA_2017 + DATA_2018 + DATA
    estimators, bet_max, bet_pred_bot_a, bet_pred_bot_b, bet_pred_top_a, bet_pred_top_b = bet_params
    estimators = int(estimators * 100)

    # init
    reg = None
    scaler = MinMaxScaler()
    cutoff = int(len(all_data) * 0.7)
    ratings = defaultdict(lambda: Rating())
    early_fights = defaultdict(lambda: 0.5)
    last_fights = defaultdict(lambda: 0.5)
    training_data = []
    label_data = []
    payouts = []
    bet_amts = []
    accuracy = (0, 0)
    tab = []
    actual = (0, 0)
    bet_multis = []

    # loop through scenes
    for i, scene in enumerate(all_data):
        is_training = i < cutoff
        if not is_training:
            if not reg:
                reg = get_regressor(training_data, label_data, scaler, estimators=estimators)
            logger.info('')
        logger.info(f'{scene["date"]} {scene["name"]}')

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
            # update ratings
            if 'winner' in fight:
                # get winner
                fw = fight['winner']['fighter']
                is_win_1 = fw == f1
                fl = f2 if is_win_1 else f1
                if not is_win_1 and fw != f2 and fw is not None:
                    raise ValueError(f'unknown winner {fw}')
                drawn = fw is None

                ratings[fw], ratings[fl] = rate_1vs1(ratings[fw], ratings[fl], drawn=drawn)
                # update fights
                early_fights[fw] = last_fights[fw]
                early_fights[fl] = last_fights[fl]
                last_fights[fw] = 1
                last_fights[fl] = 0

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

                if pred1 > pred2:
                    fw = f1
                    fw_odds = f1_odds
                    fw_pred = pred1
                    fl = f2
                    fl_odds = f2_odds
                    fl_pred = pred2
                else:
                    fw = f2
                    fw_odds = f2_odds
                    fw_pred = pred2
                    fl = f1
                    fl_odds = f1_odds
                    fl_pred = pred1

                #############################
                # bet scaling
                bet_multi = 1

                # pred
                bet_pred_bot_multi = np.polyval([bet_pred_bot_a, bet_pred_bot_b], [fw_pred])
                bet_multi += min(max(int(bet_pred_bot_multi), 0), min(max(int(bet_max), 0), 10))
                bet_pred_top_multi = np.polyval([bet_pred_top_a, bet_pred_top_b], [fw_pred])
                bet_multi += min(max(int(bet_pred_top_multi), 0), min(max(int(bet_max), 0), 10))

                bet_multis.append(bet_multi)
                bet_size *= bet_multi
                bet_amts.append(bet_size)
                #############################

                # prediction made
                if 'prediction' in fight and fight['prediction'] is None:
                    logger.warning(f'[{fw_pred * 100:.0f}% vs {fl_pred * 100:.0f}%] Bet x{bet_multi} on {fw} to beat {fl} [{ratings[fw].mu:.0f} vs {ratings[fl].mu:.0f}]')
                    continue

                # good luck with your bets
                elif 'winner' not in fight:
                    logger.warning(f'Pending {f1} vs {f2}')
                    continue

                if is_win_1:
                    fw_pred = pred1
                    fl_pred = pred2
                else:
                    fw_pred = pred2
                    fl_pred = pred1

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
                    payout = -fight['bet']
                    if is_actual_correct:
                        w_odds = f1_odds if is_win_1 else f2_odds
                        payout += w_odds * fight['bet']
                    tab.append(round(payout, 2))

                log_balance = f'[{sum(payouts):.0f}|{payout:.0f}]'
                log_pred = f'[{fw_pred * 100:.0f}% vs {fl_pred * 100:.0f}%]'
                log_fight = f'x{bet_multi} {fw} {fight["winner"]["by"]} {fl}'
                log_ratings = f'[{ratings[fw].mu:.0f} vs {ratings[fl].mu:.0f}]'
                logger.info(f'{log_balance} {log_pred} {log_fight} {log_ratings}')

    ###################################
    # Summary

    if accuracy[1]:
        payouts = np.array(payouts)
        logger.info('')
        logger.info('Testing:')
        logger.info(f'ROI {sum(payouts) / sum(bet_amts) * 100:.2f}%')
        logger.info(f'Accuracy {accuracy[0]}/{accuracy[1]} = {accuracy[0] / accuracy[1] * 100:.0f}%')
        logger.info(f'Profit ${sum(payouts):.0f} per bet: {payouts.mean():.2f}')
        # logger.info(f'Payouts: max={payouts.max()} min={payouts.min()}')
        logger.info(f'Most common: {Counter(payouts).most_common(5)}')
        logger.info(f'Common multis: {Counter(bet_multis).most_common(10)}')

    if actual[1]:
        tab = np.array(tab)
        logger.info('')
        logger.info('Actual:')
        logger.info(f'Accuracy {actual[0]}/{actual[1]} = {actual[0] / actual[1] * 100:.0f}%')
        logger.info(f'Profit ${sum(tab):.0f} per bet: {tab.mean():.2f}')
        logger.info(f'tab: max={tab.max()} min={tab.min()}')
        logger.info(f'Most common: {Counter(tab).most_common(5)}')

    logger.info('Done')
    return -(sum(payouts) / sum(bet_amts))


if __name__ == '__main__':
    bet_params = [
        # estimators
        2.276484519529152, 
        # bet max
        10.874928957139876, 
        # pred lower
        -12.785237743583401, -1.9265052392632152, 
        # pred higher
        15.659256378079002, -10.392205569263318,
    ]

    train = 0

    if not train:
        main(bet_params)
    else:
        es = CMAEvolutionStrategy(bet_params, 1)
        while not es.stop():
            solutions = es.ask()
            fitness = [main(x) for x in solutions]
            es.tell(solutions, fitness)
            # es.logger.add()
            es.disp()
            print(es.result[0])
        es.result_pretty()
        # es.logger.plot()
