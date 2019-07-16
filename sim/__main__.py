from time import sleep

import numpy as np
import pandas as pd
from collections import defaultdict, Counter
from itertools import chain
from math import sqrt
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor

from loguru import logger
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from trueskill import quality_1vs1, Rating, BETA, global_env, rate_1vs1

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


def main():
    ratings = defaultdict(lambda: Rating())
    bet_cnt = 0
    balance = 0
    accuracy = (0, 0)
    ac_msgs = []
    logger.info(f'Balance is {balance}. good luck!')

    for scene in DATA:
        logger.info(f'{scene["date"]} {scene["name"]}')
        for fight in scene['fights']:
            f1 = fight['fighters'][0]['name']
            f2 = fight['fighters'][1]['name']

            draw_prob = round(quality_1vs1(ratings[f1], ratings[f2]), 2)
            win1_prob = round(win_probability([ratings[f1]], [ratings[f2]]), 2)

            # get winner
            fw = fight['winner']['fighter']
            is_win_1 = fw == f1
            fl = f2 if is_win_1 else f1
            if not is_win_1 and fw != f2 and fw is not None:
                raise ValueError(f'unknown winner {fw}')
            drawn = fw is None

            # skip if no odds:
            if not 'odds' in fight:
                continue

            # absolute betting
            correct = 0
            payout = -BET_AMT
            f1_odds = fight['odds'][f1]
            f2_odds = fight['odds'][f2]
            if is_win_1 and (win1_prob > 0.5 or win1_prob == 0.5 and f1_odds < f2_odds):
                correct = 1
                if f1_odds > 0:
                    payout += f1_odds / BET_AMT + BET_AMT
                else:
                    payout += 100 * BET_AMT / abs(f1_odds) + BET_AMT
            elif not is_win_1 and (win1_prob < 0.5 or win1_prob == 0.5 and f2_odds < f1_odds):
                correct = 1
                if f2_odds > 0:
                    payout += f2_odds / BET_AMT + BET_AMT
                else:
                    payout += 100 * BET_AMT / abs(f2_odds) + BET_AMT
            balance += payout
            bet_cnt += 1

            # accuracy
            upset = False
            fwr = round(ratings[fw].mu, 1)
            flr = round(ratings[fl].mu, 1)
            if fwr != 25 and flr != 25 and fwr != flr:
                accuracy = (accuracy[0] + correct, accuracy[1] + 1)
                if fwr < flr:
                    upset = True

            logger.info(f'{">>>>> " if upset else ""}[{ratings[fw].mu:.1f} : {ratings[fl].mu:.1f}] {fw} {fight["winner"]["by"]} {fl} ==> {payout:.0f} bal:{balance:.0f}')

            # update ratings
            ratings[fw], ratings[fl] = rate_1vs1(ratings[fw], ratings[fl], drawn=drawn)

    if accuracy[1]:
        logger.info(f'Accuracy {accuracy[0]}/{accuracy[1]} = {accuracy[0]/accuracy[1]*100:.0f}%')

    if bet_cnt:
        logger.info(f'Profit per bet: {balance/bet_cnt:.2f}')


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


def two_trees():
    logger.info('Starting main training')

    # build data
    training_data = []
    label_data = []
    ratings = defaultdict(lambda: Rating())
    for scene in DATA:
        logger.info(f'{scene["date"]} {scene["name"]}')
        for fight in scene['fights']:
            # skip if no odds:
            if 'odds' not in fight:
                continue

            f1 = fight['fighters'][0]['name']
            f2 = fight['fighters'][1]['name']

            # win1_prob = round(win_probability([ratings[f1]], [ratings[f2]]), 2)

            # get winner
            fw = fight['winner']['fighter']
            is_win_1 = fw == f1
            fl = f2 if is_win_1 else f1
            if not is_win_1 and fw != f2 and fw is not None:
                raise ValueError(f'unknown winner {fw}')
            drawn = fw is None

            fight_data = [
                [
                    to_decimal_odds(fight['odds'][f1]),
                    to_decimal_odds(fight['odds'][f2]),
                    ratings[f1].mu,
                    ratings[f2].mu,
                    ratings[f1].sigma,
                    ratings[f2].sigma,
                ],
                [
                    to_decimal_odds(fight['odds'][f2]),
                    to_decimal_odds(fight['odds'][f1]),
                    ratings[f2].mu,
                    ratings[f1].mu,
                    ratings[f2].sigma,
                    ratings[f1].sigma,
                ]
            ]
            training_data.extend(fight_data)
            label_data.extend([is_win_1, not is_win_1])
            # logger.info(f'[{ratings[fw].mu:.1f} : {ratings[fl].mu:.1f}] {fw} {fight["winner"]["by"]} {fl}')

            # update ratings
            ratings[fw], ratings[fl] = rate_1vs1(ratings[fw], ratings[fl], drawn=drawn)

    # scale
    scaler = MinMaxScaler()
    scaler.partial_fit(training_data)
    scaled = scaler.transform(training_data)

    # prepare data
    cutoff = int(len(scaled) * 0.80)
    X_train, X_test = scaled[:cutoff], scaled[cutoff:]
    y_train, y_test = label_data[:cutoff], label_data[cutoff:]

    # train
    reg = GradientBoostingRegressor()
    reg = reg.fit(X_train, y_train)
    mse = mean_squared_error(y_test, reg.predict(X_test))
    logger.info(f'MSE: {mse}')

    #########################################################################
    # calculate profit

    ratings = defaultdict(lambda: Rating())
    bet_cnt = 0
    balance = 0
    accuracy = (0, 0)
    logger.info(f'Balance is {balance}. good luck!')

    betting_data = []
    betting_labels = []

    for scene in DATA:
        logger.info(f'{scene["date"]} {scene["name"]}')
        for fight in scene['fights']:
            f1 = fight['fighters'][0]['name']
            f2 = fight['fighters'][1]['name']

            # draw_prob = round(quality_1vs1(ratings[f1], ratings[f2]), 2)
            # win1_prob = round(win_probability([ratings[f1]], [ratings[f2]]), 2)

            # get winner
            fw = fight['winner']['fighter']
            is_win_1 = fw == f1
            fl = f2 if is_win_1 else f1
            if not is_win_1 and fw != f2 and fw is not None:
                raise ValueError(f'unknown winner {fw}')
            drawn = fw is None

            # skip if no odds:
            if not 'odds' in fight:
                continue
            f1_odds = fight['odds'][f1]
            f2_odds = fight['odds'][f2]

            # clf betting
            scaled_data = scaler.transform([
                [
                    to_decimal_odds(fight['odds'][f1]),
                    to_decimal_odds(fight['odds'][f2]),
                    ratings[f1].mu,
                    ratings[f2].mu,
                    ratings[f1].sigma,
                    ratings[f2].sigma,
                ],
                [
                    to_decimal_odds(fight['odds'][f2]),
                    to_decimal_odds(fight['odds'][f1]),
                    ratings[f2].mu,
                    ratings[f1].mu,
                    ratings[f2].sigma,
                    ratings[f1].sigma,
                ]
            ])
            pred1, pred2 = reg.predict(scaled_data)

            # get bet recommendation
            bet_data = [pred1, pred2]
            try:
                clf = GradientBoostingClassifier().fit(betting_data, betting_labels)
                bet_pred = clf.predict([bet_data])[0]
            except ValueError as exc:
                if len(betting_data):
                    raise
                betting_data.append(bet_data)
                betting_labels.append(0)
                betting_data.append(bet_data)
                betting_labels.append(1)
                betting_data.append(bet_data)
                betting_labels.append(2)
                continue

            if bet_pred:
                correct = 0
                payout = -BET_AMT
                if is_win_1 and pred1 > pred2:
                    correct = 1
                    if f1_odds > 0:
                        payout += f1_odds / BET_AMT + BET_AMT
                    else:
                        payout += 100 * BET_AMT / abs(f1_odds) + BET_AMT
                elif not is_win_1 and pred2 > pred1:
                    correct = 1
                    if f2_odds > 0:
                        payout += f2_odds / BET_AMT + BET_AMT
                    else:
                        payout += 100 * BET_AMT / abs(f2_odds) + BET_AMT
                balance += payout
                bet_cnt += 1

                # accuracy
                upset = False
                accuracy = (accuracy[0] + correct, accuracy[1] + 1)
                if (is_win_1 and pred2 > pred1) or (not is_win_1 and pred1 > pred2):
                    upset = True

                logger.info(f'{">>>>> " if upset else ""}[{ratings[fw].mu:.1f} : {ratings[fl].mu:.1f}] {fw} {fight["winner"]["by"]} {fl} ==> {payout:.0f} bal:{balance:.0f}')

            # update betting data
            betting_data.append(bet_data)
            if is_win_1 and pred1 > pred2:
                betting_label = 1
            elif not is_win_1 and pred2 > pred1:
                betting_label = 2
            else:
                betting_label = 0
            betting_labels.append(betting_label)

            # update ratings
            ratings[fw], ratings[fl] = rate_1vs1(ratings[fw], ratings[fl], drawn=drawn)

    if accuracy[1]:
        logger.info(f'Accuracy {accuracy[0]}/{accuracy[1]} = {accuracy[0]/accuracy[1]*100:.0f}%')

    if bet_cnt:
        logger.info(f'Profit per bet: {balance/bet_cnt:.2f}')

    logger.info('Done')


def tree():
    logger.info('Starting main training')

    # build data
    training_data = []
    label_data = []
    ratings = defaultdict(lambda: Rating())
    for scene in DATA:
        # logger.info(f'{scene["date"]} {scene["name"]}')
        for fight in scene['fights']:
            # skip if no odds:
            if 'odds' not in fight:
                continue

            f1 = fight['fighters'][0]['name']
            f2 = fight['fighters'][1]['name']

            win1_prob = win_probability([ratings[f1]], [ratings[f2]])
            win2_prob = win_probability([ratings[f2]], [ratings[f1]])

            # get winner
            fw = fight['winner']['fighter']
            is_win_1 = fw == f1
            fl = f2 if is_win_1 else f1
            if not is_win_1 and fw != f2 and fw is not None:
                raise ValueError(f'unknown winner {fw}')
            drawn = fw is None

            f1_odds = fight['odds'][f1]
            f2_odds = fight['odds'][f2]

            fight_data = [
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
            training_data.extend(fight_data)
            label_data.extend([is_win_1, not is_win_1])
            # logger.info(f'[{ratings[fw].mu:.1f} : {ratings[fl].mu:.1f}] {fw} {fight["winner"]["by"]} {fl}')

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
    sleep(2)

    #########################################################################
    # calculate profit

    actual = (0, 0)
    payouts = []
    ratings = defaultdict(lambda: Rating())
    bet_cnt = 0
    balance = 0
    accuracy = (0, 0)
    logger.info(f'Balance is {balance}. good luck!')

    for scene in DATA:
        logger.info('')
        logger.info(f'{scene["date"]} {scene["name"]}')
        for fight in scene['fights']:
            # skip if no odds:
            if not 'odds' in fight:
                continue

            f1 = fight['fighters'][0]['name']
            f2 = fight['fighters'][1]['name']

            win1_prob = win_probability([ratings[f1]], [ratings[f2]])
            win2_prob = win_probability([ratings[f2]], [ratings[f1]])

            # get winner
            fw = fight['winner']['fighter']
            is_win_1 = fw == f1
            fl = f2 if is_win_1 else f1
            if not is_win_1 and fw != f2 and fw is not None:
                raise ValueError(f'unknown winner {fw}')
            drawn = fw is None

            f1_odds = fight['odds'][f1]
            f2_odds = fight['odds'][f2]

            # regressor betting
            scaled_data = scaler.transform([
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
            ])
            pred1, pred2 = reg.predict(scaled_data)
            if is_win_1:
                predw = pred1
                predl = pred2
            else:
                predw = pred2
                predl = pred1

            correct = 0
            payout = -BET_AMT
            if is_win_1 and pred1 > pred2:
                correct = 1
                payout += f1_odds * BET_AMT
            elif not is_win_1 and pred2 > pred1:
                correct = 1
                payout += f2_odds * BET_AMT
            payout = round(payout, 2)
            balance += payout
            bet_cnt += 1
            payouts.append(payout)

            # accuracy
            upset = False
            accuracy = (accuracy[0] + correct, accuracy[1] + 1)
            if (is_win_1 and pred2 > pred1) or (not is_win_1 and pred1 > pred2):
                upset = True

            # actual
            if 'prediction' in fight:
                is_actual_correct = fight['prediction'] == fw
                actual = (actual[0] + is_actual_correct, actual[1] + 1)

            logger.info(f'[{balance:.0f}::{payout:.0f}]{" !!" if upset else ""} [{predw * 100:.0f}% vs {predl * 100:.0f}%] {fw} {fight["winner"]["by"]} {fl} [{ratings[fw].mu:.0f} vs {ratings[fl].mu:.0f}]')

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
    for scene in PREDICTIONS:
        logger.info('')
        logger.info(f'{scene["date"]} {scene["name"]}')
        for fight in scene['fights']:
            # skip if no odds:
            if 'odds' not in fight or not fight['odds']:
                continue

            f1 = fight['fighters'][0]['name']
            f2 = fight['fighters'][1]['name']

            win1_prob = win_probability([ratings[f1]], [ratings[f2]])
            win2_prob = win_probability([ratings[f2]], [ratings[f1]])

            f1_odds = fight['odds'][f1]
            f2_odds = fight['odds'][f2]

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
    # main()
    # two_trees()
    tree()


# from trueskill import Rating, quality_1vs1, rate_1vs1
# alice, bob = Rating(25), Rating(30)  # assign Alice and Bob's ratings
# if quality_1vs1(alice, bob) < 0.50:
#     print('This match seems to be not so fair')
# alice, bob = rate_1vs1(alice, bob)  # update the ratings after the match
