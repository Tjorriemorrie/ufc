from collections import Counter, defaultdict
from itertools import chain
from queue import Queue

from math import sqrt

import numpy as np
from cma import CMAEvolutionStrategy
from loguru import logger
from sklearn.preprocessing import MinMaxScaler
from trueskill import BETA, global_env, rate_1vs1, Rating
from xgboost import XGBRegressor

from data_2019_02 import DATA_2019_02
from data_2019_03 import DATA_2019_03
from data_2019_04 import DATA_2019_04
from .data import DATA


def win_probability(team1, team2):
    delta_mu = sum(r.mu for r in team1) - sum(r.mu for r in team2)
    sum_sigma = sum(r.sigma ** 2 for r in chain(team1, team2))
    size = len(team1) + len(team2)
    denom = sqrt(size * (BETA * BETA) + sum_sigma)
    ts = global_env()
    return ts.cdf(delta_mu / denom)


def get_regressor(training_data, label_data, scaler):
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

    reg = XGBRegressor(n_estimators=100, objective='reg:squarederror', n_jobs=4)
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
        'win%', 'odds', '~odds',
        'mu', '~mu', 'sigma', '~sigma',
        'round', 'retired', '~retired', 'upsets' '~upsets']
    # for name, val in zip(feature_names, reg.feature_importances_):
    #     logger.info(f'{name}: {val}')

    return reg


def main(bet_params=None):
    logger.info('Starting main training')

    all_data = DATA_2019_02 + DATA_2019_03 + DATA_2019_04 + DATA
    upsets_cutoff, retireds_cutoff, \
        bet_pred_bot_a, bet_pred_bot_b, bet_pred_top_a, bet_pred_top_b, \
        bet_rnd_bot_a, bet_rnd_bot_b, bet_rnd_top_a, bet_rnd_top_b = bet_params
    upsets_cutoff = int(upsets_cutoff)
    retireds_cutoff = int(retireds_cutoff)

    # init
    reg = None
    scaler = MinMaxScaler()
    cutoff = int(len(DATA) * 0.7)
    ratings = defaultdict(lambda: Rating())
    retireds = defaultdict(lambda: [])
    upsets = defaultdict(lambda: [])
    training_data = []
    label_data = []
    payouts = []
    bet_amts = []
    accuracy = (0, 0)
    tab = []
    actual = (0, 0)
    bet_multis = []

    # loop through scenes
    for i, event in enumerate(all_data):
        bet_size = 5
        is_training = i < cutoff
        if not is_training:
            if not reg:
                reg = get_regressor(training_data, label_data, scaler)
            logger.info('')
        logger.info(f'{event["date"]} {event["name"]}')

        for match in event['matches']:
            # skip if no odds:
            if 'odds' not in match:
                continue

            p1, p2 = match['players']
            p1_odds = match['odds'][p1]
            p2_odds = match['odds'][p2]
            if not -40 < p1_odds < 40 or not -40 < p2_odds < 40:
                raise ValueError(f'surely these odds are wrong? {p1_odds} {p2_odds}')
            win1_prob = win_probability([ratings[p1]], [ratings[p2]])
            win2_prob = win_probability([ratings[p2]], [ratings[p1]])

            # retired?
            p1_retired = sum(retireds[p1])
            p2_retired = sum(retireds[p2])

            # upsets
            p1_upsets = sum(upsets[p1])
            p2_upsets = sum(upsets[p2])

            match_data = [
                [
                    win1_prob,
                    1 / p1_odds,
                    1 / p2_odds,
                    ratings[p1].mu,
                    ratings[p2].mu,
                    ratings[p1].sigma,
                    ratings[p2].sigma,
                    1 / match['round'],
                    p1_retired,
                    p2_retired,
                    p1_upsets,
                    p2_upsets,
                ],
                [
                    win2_prob,
                    1 / p2_odds,
                    1 / p1_odds,
                    ratings[p2].mu,
                    ratings[p1].mu,
                    ratings[p2].sigma,
                    ratings[p1].sigma,
                    1 / match['round'],
                    p2_retired,
                    p1_retired,
                    p2_upsets,
                    p1_upsets,
                ]
            ]

            #########################################
            # update here as next sections can skip ahead
            # update upsets
            upset = win1_prob < 0.50
            upsets[p1] = upsets[p1][-upsets_cutoff:] + [upset]
            upsets[p2] = upsets[p2][-upsets_cutoff:] + [0]
            # update retireds
            retireds[p1] = retireds[p1][-retireds_cutoff:] + [0]
            retireds[p2] = retireds[p2][-retireds_cutoff:] + [match.get('retired', 0)]
            # update ratings
            ratings[p1], ratings[p2] = rate_1vs1(ratings[p1], ratings[p2])

            ###################################
            # train
            if is_training:
                training_data.extend(match_data)
                label_data.extend([1, 0])

            ###################################
            # test
            else:
                scaled_match_data = scaler.transform(match_data)
                pred1, pred2 = reg.predict(scaled_match_data)

                #########################
                # bet scaling
                bet_multi = 1

                """ 
                top  0.3  0.5  0.7  0.9  1.1  1.3  1.5  1.7
                1         -2.4                     -2.3
                2    -2.3                               -2.3
                3              -2.9
                4    
                5                   -2.5
                7                        -3.3
                9                             -2.3
                """
                max_pred = max(pred1, pred2)
                if max_pred > 0.3:
                    bet_multi += 4
                """ 
                bot   .60   .75   .85   .90   .95   1.0   1.1   1.15   1.2   1.4
                .4    -4.7         
                .5          -.30  
                .55               -.37        -.06        .32          0.85
                .6                      1.78  2.14  2.41  2.79  3.01   3.22  3.22
                .65               -.67        -.52                     -.07
                .7                                  -1.7
                """
                # if max_pred < 0.6:
                #     bet_multi += 5

                # round
                # rnd = 1 / match['round']
                # bet_rnd_bot_multi = np.polyval([bet_rnd_bot_a, bet_rnd_bot_b], [rnd])
                # bet_multi += min(max(int(bet_rnd_bot_multi), 0), 5)
                # bet_rnd_top_multi = np.polyval([bet_rnd_top_a, bet_rnd_top_b], [rnd])
                # bet_multi += min(max(int(bet_rnd_top_multi), 0), 5)

                bet_multis.append(bet_multi)
                bet_amt = bet_size * bet_multi
                bet_amts.append(bet_amt)

                if 'prediction' in match and match['prediction'] is None:
                    if pred1 > pred2:
                        predw = pred1
                        pw = p1
                        predl = pred2
                        pl = p2
                    else:
                        predw = pred2
                        pw = p2
                        predl = pred1
                        pl = p1
                    logger.warning(f'[x{bet_multi}] [{predw*100:.0f}% vs {predl*100:.0f}%] Bet on {pw} to beat {pl} [{ratings[pw].mu:.0f} vs {ratings[pl].mu:.0f}]')
                    continue

                # prediction bet on
                elif 'score' not in match:
                    logger.warning(f'Pending {p1} vs {p2}')
                    continue

                # testing outcome
                correct = 0
                payout = -bet_amt
                if pred1 > pred2:
                    correct = 1
                    payout += p1_odds * bet_amt
                payouts.append(round(payout, 2))
                accuracy = (accuracy[0] + correct, accuracy[1] + 1)

                # actual outcome
                if 'bet' in match:
                    is_actual_correct = match['prediction'] == p1
                    actual = (actual[0] + is_actual_correct, actual[1] + 1)
                    cash = -match['bet']
                    if is_actual_correct:
                        cash += p1_odds * match['bet']
                    tab.append(round(cash, 2))

                log_balance = f'[{sum(payouts):.0f}|{payout:.0f}]'
                log_pred = f'[{pred1 * 100:.0f}% vs {pred2 * 100:.0f}%]'
                log_players = f'x{bet_multi} {p1} {match.get("score")} {p2}'
                log_odds = f'[{p1_odds:.2f} vs {p2_odds:.2f}]'
                log_trueskill = f'[{ratings[p1].mu:.0f}.{ratings[p1].sigma:.0f} vs {ratings[p2].mu:.0f}.{ratings[p2].sigma:.0f}]'
                logger.info(f'{log_balance} {log_pred} {log_players} {log_odds} {log_trueskill}')

    ###################################
    # Summary

    if accuracy[1]:
        logger.info('')
        logger.info('Testing:')
        logger.info(f'ROI {sum(payouts) / sum(bet_amts) * 100:.2f}%')
        logger.info(f'Accuracy {accuracy[0]}/{accuracy[1]} = {accuracy[0]/accuracy[1]*100:.0f}%')
        payouts = np.array(payouts)
        logger.info(f'Profit ${sum(payouts):.0f} per bet: {payouts.mean():.2f}')
        logger.info(f'Payouts: max={payouts.max()} min={payouts.min()}')
        logger.info(f'Most common: {Counter(payouts).most_common(5)}')
        logger.info(f'Common multis: {Counter(bet_multis).most_common(10)}')

    if actual[1]:
        logger.info('')
        logger.info('Actual:')
        logger.info(f'Accuracy {actual[0]}/{actual[1]} = {actual[0]/actual[1] * 100:.0f}%')
        tab = np.array(tab)
        logger.info(f'Profit ${sum(tab):.0f} per bet: {tab.mean():.2f}')
        logger.info(f'tab: max={tab.max()} min={tab.min()}')
        logger.info(f'Most common: {Counter(tab).most_common(5)}')

    logger.info(f'Done')
    return -(sum(payouts) / sum(bet_amts))


if __name__ == '__main__':
    bet_params = [
        # cutoff (upsets, retireds)
        17.79032316, 12.4691518,
        # pred lower
        -22.23187227, 14.82638623,
        # pred higher
        9.74950199, -7.69972695,
        # round lower
        -22.23187227, 14.82638623,
        # round higher
        9.74950199, -7.69972695,
    ]
    main(bet_params)

    # es = CMAEvolutionStrategy(bet_params, 1)
    # while not es.stop():
    #     solutions = es.ask()
    #     fitness = [main(x) for x in solutions]
    #     es.tell(solutions, fitness)
    #     # es.logger.add()
    #     es.disp()
    #     print(es.result[0])
    # es.result_pretty()
    # # es.logger.plot()
