from collections import Counter, defaultdict
from itertools import chain
from math import sqrt

import numpy as np
from loguru import logger
from sklearn.preprocessing import MinMaxScaler
from trueskill import BETA, global_env, rate_1vs1, Rating
from xgboost import XGBRegressor

from .data import DATA

BET_AMT = 10


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

    reg = XGBRegressor(n_estimators=1000, objective='reg:squarederror', n_jobs=4)
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
        'round']
    for name, val in zip(feature_names, reg.feature_importances_):
        logger.info(f'{name}: {val}')

    return reg


def main():
    logger.info('Starting main training')

    # init
    reg = None
    scaler = MinMaxScaler()
    cutoff = int(len(DATA) * 0.7)
    ratings = defaultdict(lambda: Rating())
    training_data = []
    label_data = []
    payouts = []
    accuracy = (0, 0)
    tab = []
    actual = (0, 0)
    predictions = {0: [], 1: []}

    # loop through scenes
    for i, event in enumerate(DATA):
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
            f1_odds = match['odds'][p1]
            f2_odds = match['odds'][p2]
            if not -30 < f1_odds < 30 or not -30 < f2_odds < 30:
                raise ValueError(f'surely these odds are wrong? {f1_odds} {f2_odds}')
            win1_prob = win_probability([ratings[p1]], [ratings[p2]])
            win2_prob = win_probability([ratings[p2]], [ratings[p1]])

            match_data = [
                [
                    win1_prob,
                    1 / f1_odds,
                    1 / f2_odds,
                    ratings[p1].mu,
                    ratings[p2].mu,
                    ratings[p1].sigma,
                    ratings[p2].sigma,
                    1 / match['round'],
                ],
                [
                    win2_prob,
                    1 / f2_odds,
                    1 / f1_odds,
                    ratings[p2].mu,
                    ratings[p1].mu,
                    ratings[p2].sigma,
                    ratings[p1].sigma,
                    1 / match['round'],
                ]
            ]

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
                predictions[1].append(pred1 - pred2)
                predictions[0].append(pred2 - pred1)
                """
                Winners: [-0.588073   -0.10473108  0.20082912  0.48903563  0.95547485]
                Losers: [-0.95547485 -0.48903563 -0.20082912  0.10473108  0.588073  ]
                1to2  -.10  -.05  0.00  0.05  0.10  0.20  0.30  0.40
                -.20  3.58  4.08  4.34  4.15  3.80  3.48
                -.10  ----  4.38  4.63  4.44  4.09  3.78
                -.05  ----  1.21  4.88  4.70  4.35
                0.00  ----  ----  5.01  4.82  4.47  4.16  3.58
                0.05  ----  ----  ----  1.93  4.38
                0.10  ----  ----  ----  ----  ----  3.89
                0.20  ----  ----  ----  ----  ----  ----  3.15  2.92
                0.30  ----  ----  ----  ----  ----  ----        2.63
                """
                multi_level_1 = -0.05
                multi_level_2 = 0.05
                multi = 2 if pred1 - pred2 > multi_level_1 else 1
                multi *= 2 if pred1 - pred2 > multi_level_2 else 1

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
                    logger.info(f'[x{multi}] [{predw * 100:.0f}% vs {predl * 100:.0f}%] {pw} to beat {pl} [{ratings[pw].mu:.0f} vs {ratings[pl].mu:.0f}]')
                    continue

                # testing outcome
                correct = 0
                payout = -bet_size * multi
                if pred1 > pred2:
                    correct = 1
                    payout += f1_odds * bet_size * multi
                payouts.append(round(payout, 2))
                accuracy = (accuracy[0] + correct, accuracy[1] + 1)

                # actual outcome
                if 'bet' in match:
                    is_actual_correct = match['prediction'] == p1
                    actual = (actual[0] + is_actual_correct, actual[1] + 1)
                    cash = -match['bet']
                    if is_actual_correct:
                        cash += f1_odds * match['bet']
                    tab.append(round(cash, 2))

                log_balance = f'[{sum(payouts):.0f}|{payout:.0f}x{multi}]'
                log_pred = f'[{pred1 * 100:.0f}% vs {pred2 * 100:.0f}%]'
                log_players = f'{p1} {match.get("score")} {p2}'
                log_odds = f'[{f1_odds:.2f} vs {f2_odds:.2f}]'
                log_trueskill = f'[{ratings[p1].mu:.0f}.{ratings[p1].sigma:.0f} vs {ratings[p2].mu:.0f}.{ratings[p2].sigma:.0f}]'
                logger.info(f'{log_balance} {log_pred} {log_players} {log_odds} {log_trueskill}')

            # update ratings
            ratings[p1], ratings[p2] = rate_1vs1(ratings[p1], ratings[p2])

    ###################################
    # Summary

    if accuracy[1]:
        logger.info('')
        logger.info('Testing:')
        logger.info(f'Accuracy {accuracy[0]}/{accuracy[1]} = {accuracy[0]/accuracy[1]*100:.0f}%')
        payouts = np.array(payouts)
        logger.info(f'Profit ${sum(payouts):.0f} per bet: {payouts.mean():.2f}')
        logger.info(f'Payouts: max={payouts.max()} min={payouts.min()}')
        logger.info(f'Most common: {Counter(payouts).most_common(5)}')

    if actual[1]:
        logger.info('')
        logger.info('Actual:')
        logger.info(f'Accuracy {actual[0]}/{actual[1]} = {actual[0]/actual[1] * 100:.0f}%')
        tab = np.array(tab)
        logger.info(f'Profit ${sum(tab):.0f} per bet: {tab.mean():.2f}')
        logger.info(f'tab: max={tab.max()} min={tab.min()}')
        logger.info(f'Most common: {Counter(tab).most_common(5)}')

    # logger.info('')
    # logger.info('prediction percentiles:')
    # logger.info(f'Winners: {np.percentile(predictions[1], [10, 30, 50, 70, 90])}')
    # logger.info(f'Losers: {np.percentile(predictions[0], [10, 30, 50, 70, 90])}')

    logger.info('Done')
    return sum(payouts)


if __name__ == '__main__':
    main()
