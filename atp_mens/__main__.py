from collections import Counter, defaultdict
from itertools import chain
from time import sleep

import numpy as np
from loguru import logger
from math import sqrt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from trueskill import BETA, global_env, rate_1vs1, Rating

from data import DATA, PREDICTIONS

BET_AMT = 10


def win_probability(team1, team2):
    delta_mu = sum(r.mu for r in team1) - sum(r.mu for r in team2)
    sum_sigma = sum(r.sigma ** 2 for r in chain(team1, team2))
    size = len(team1) + len(team2)
    denom = sqrt(size * (BETA * BETA) + sum_sigma)
    ts = global_env()
    return ts.cdf(delta_mu / denom)


def get_implied_odds(american):
    if american > 0:
        return 100 / (american + 100)
    return abs(american) / (abs(american) + 100)


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


def main():
    logger.info('Starting main training')

    # build data
    training_data = []
    label_data = []
    ratings = defaultdict(lambda: Rating())
    for event in DATA:
        for match in event['matches']:
            f1, f2 = match['players']
            win1_prob = win_probability([ratings[f1]], [ratings[f2]])
            win2_prob = win_probability([ratings[f2]], [ratings[f1]])
            f1_io = 1 / match['odds'][f1]
            f2_io = 1 / match['odds'][f2]

            # get winner
            fw = match['winner']
            is_win_1 = fw == f1
            fl = f2 if is_win_1 else f1
            if not is_win_1 and fw != f2 and fw is not None:
                raise ValueError(f'unknown winner {fw}')
            drawn = fw is None

            player_data = [
                [
                    win1_prob,
                    win2_prob,
                    f1_io,
                    f2_io,
                    ratings[f1].mu,
                    ratings[f2].mu,
                    ratings[f1].sigma,
                    ratings[f2].sigma,
                ],
                [
                    win2_prob,
                    win1_prob,
                    f2_io,
                    f1_io,
                    ratings[f2].mu,
                    ratings[f1].mu,
                    ratings[f2].sigma,
                    ratings[f1].sigma,
                ]
            ]
            training_data.extend(player_data)
            label_data.extend([is_win_1, not is_win_1])

            # update ratings
            ratings[fw], ratings[fl] = rate_1vs1(ratings[fw], ratings[fl], drawn=drawn)

    # scale
    scaler = MinMaxScaler()
    scaler.partial_fit(training_data)
    scaled_training_data = scaler.transform(training_data)

    # prepare data
    cutoff = int(len(scaled_training_data) * 0.90)
    X_train, X_test = scaled_training_data[:cutoff], scaled_training_data[cutoff:]
    y_train, y_test = label_data[:cutoff], label_data[cutoff:]

    # train
    reg = GradientBoostingRegressor()
    reg = reg.fit(X_train, y_train)
    mse = mean_squared_error(y_test, reg.predict(X_test))
    logger.info(f'MSE: {mse:.2f}')
    sleep(1)

    #########################################################################
    # calculate profit

    actual = (0, 0)
    payouts = []
    ratings = defaultdict(lambda: Rating())
    bet_cnt = 0
    balance = 0
    accuracy = (0, 0)
    logger.info(f'Balance is {balance}. good luck!')

    for event in DATA:
        logger.info('')
        logger.info(f'{event["date"]} {event["name"]}')
        for match in event['matches']:
            f1, f2 = match['players']
            win1_prob = win_probability([ratings[f1]], [ratings[f2]])
            win2_prob = win_probability([ratings[f2]], [ratings[f1]])
            f1_odds = match['odds'][f1]
            f2_odds = match['odds'][f2]

            # get winner
            fw = match['winner']
            is_win_1 = fw == f1
            fl = f2 if is_win_1 else f1
            if not is_win_1 and fw != f2 and fw is not None:
                raise ValueError(f'unknown winner {fw}')
            drawn = fw is None

            player_data = [
                [
                    win1_prob,
                    win2_prob,
                    1 / f1_odds,
                    1 / f2_odds,
                    ratings[f1].mu,
                    ratings[f2].mu,
                    ratings[f1].sigma,
                    ratings[f2].sigma,
                ],
                [
                    win2_prob,
                    win1_prob,
                    1 / f2_odds,
                    1 / f1_odds,
                    ratings[f2].mu,
                    ratings[f1].mu,
                    ratings[f2].sigma,
                    ratings[f1].sigma,
                ]
            ]
            pred1, pred2 = reg.predict(player_data)

            correct = 0
            payout = -BET_AMT
            if is_win_1 and pred1 > pred2:
                correct = 1
                payout += f1_odds * BET_AMT
            elif not is_win_1 and pred2 > pred1:
                correct = 1
                payout += f2_odds * BET_AMT
            balance += payout
            bet_cnt += 1
            payouts.append(payout)

            # accuracy
            upset = False
            accuracy = (accuracy[0] + correct, accuracy[1] + 1)
            if (is_win_1 and pred2 > pred1) or (not is_win_1 and pred1 > pred2):
                upset = True

            # actual
            if 'prediction' in match:
                is_actual_correct = match['prediction'] == fw
                actual = (actual[0] + is_actual_correct, actual[1] + 1)

            logger.info(f'[{balance:.0f}::{payout:.0f}]{" !!" if upset else ""} [{pred1*100:.0f}%  vs {pred2*100:.0f}%] {fw} {match["score"]} {fl} [{ratings[f1].mu:.0f} vs {ratings[f2].mu:.0f}]')

            # update ratings
            ratings[fw], ratings[fl] = rate_1vs1(ratings[fw], ratings[fl], drawn=drawn)

    logger.info('')

    counter = Counter(payouts)
    payouts = np.array(payouts)
    logger.info(f'Payouts: max={payouts.max()} min={payouts.min()} mean={payouts.mean()}')
    logger.info(f'Most common: {counter.most_common()[:10]}')

    if accuracy[1]:
        logger.info(f'Accuracy {accuracy[0]}/{accuracy[1]} = {accuracy[0]/accuracy[1]*100:.0f}%')

    if bet_cnt:
        logger.info(f'Profit per bet: {balance/bet_cnt:.2f}')
        # logger.info(f'ROI: {balance/bet_cnt/BET_AMT*100:.0f}%')

    if actual[1]:
        logger.info(f'Actual {actual[0]}/{actual[1]} = {actual[0]/actual[1] * 100:.0f}%')

    # do predictions
    for event in PREDICTIONS:
        logger.info('')
        logger.info(f'{event["date"]} {event["name"]}')
        for match in event['fights']:
            # skip if no odds:
            if 'odds' not in match or not match['odds']:
                continue

            f1 = match['fighters'][0]['name']
            f2 = match['fighters'][1]['name']

            win1_prob = win_probability([ratings[f1]], [ratings[f2]])
            win2_prob = win_probability([ratings[f2]], [ratings[f1]])

            f1_odds = match['odds'][f1]
            f2_odds = match['odds'][f2]

            # regressor betting
            scaled_data = scaler.transform([
                [
                    win1_prob,
                    win2_prob,
                    to_implied_odds(f1_odds),
                    to_implied_odds(f2_odds),
                    ratings[f1].mu,
                    ratings[f2].mu,
                    ratings[f1].sigma,
                    ratings[f2].sigma,
                ],
                [
                    win2_prob,
                    win1_prob,
                    to_implied_odds(f2_odds),
                    to_implied_odds(f1_odds),
                    ratings[f2].mu,
                    ratings[f1].mu,
                    ratings[f2].sigma,
                    ratings[f1].sigma,
                ]
            ])
            pred1, pred2 = reg.predict(scaled_data)
            if pred1 > pred2:
                logger.info(f'Bet on {f1} [{pred1*100:.0f}% {f1_odds}] (against {f2} [{pred2*100:.0f}% {f2_odds}])')
            else:
                logger.info(f'Bet on {f2} [{pred2*100:.0f}% {f2_odds}] (against {f1} [{pred1*100:.0f}% {f1_odds}])')

    logger.info('Done')


if __name__ == '__main__':
    main()
