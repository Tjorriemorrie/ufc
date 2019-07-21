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
        'win%', '~win%', 'odds', '~odds',
        'mu', '~mu', 'sigma', '~sigma',
        'round']
    for name, val in zip(feature_names, reg.feature_importances_):
        logger.info(f'{name}: {val}')

    return reg


# 68 -0.57 <- 2019-04-22 Hungarian Open
# 65 -0.83 <- 2019-04-29 BMW Open by FWU
# 67 -0.40 <- 2019-04-29 Millennium Estoril Open
# 62 -1.12 <- Mutua Madrid Open
# 52 -2.88 <- added round as variable
# 58 -2.32 <- italia
# 61 -1.57 <- geneva
# 56 -1.58 <- parc auvergne
# 54 -1.41 <- roland garros 2019
# 54 -1.29 <- partial roland garros 2019


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

    # loop through scenes
    for i, event in enumerate(DATA):
        bet_size = max(sum(payouts), 200) // 20
        is_training = i < cutoff
        if not is_training:
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
                    win2_prob,
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
                    win1_prob,
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
                if not reg:
                    reg = get_regressor(training_data, label_data, scaler)

                scaled_match_data = scaler.transform(match_data)
                pred1, pred2 = reg.predict(scaled_match_data)

                # testing outcome
                correct = 0
                multi = 1
                # multi = 2 if pred1 - pred2 > 0.25 else 1
                # multi *= 2 if pred1 - pred2 > 0.4 else 1
                payout = -bet_size * multi
                if pred1 > pred2:
                    correct = 1
                    payout += f1_odds * bet_size
                payouts.append(round(payout, 2))
                accuracy = (accuracy[0] + correct, accuracy[1] + 1)

                # actual outcome
                if 'bet' in match:
                    raise NotImplementedError('todo')
                    is_actual_correct = match['prediction'] == fw
                    actual = (actual[0] + is_actual_correct, actual[1] + 1)
                    payout = -match['bet']
                    if is_actual_correct:
                        w_odds = f1_odds if is_win_1 else f2_odds
                        payout += w_odds * match['bet']
                    tab.append(round(payout, 2))

                logger.info(f'[{sum(payouts):.0f}|{payout:.0f}] [{pred1 * 100:.0f}% vs {pred2 * 100:.0f}%] {p1} {match["score"]} {p2} [{ratings[p1].mu:.0f} vs {ratings[p2].mu:.0f}]')

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

    # out_wins = np.array([round(w, 1) for w in out_to_preds[1]])
    # out_loss = np.array([round(l, 1) for l in out_to_preds[0]])
    # outcomes = OrderedDict()
    # for w in out_wins:
    #     if w not in outcomes:
    #         outcomes[w] = 0
    #     outcomes[w] += 1
    # for l in out_loss:
    #     if l not in outcomes:
    #         outcomes[l] = 0
    #     outcomes[l] -= 1
    # for o, v in outcomes.items():
    #     logger.info(f'{o} => {v}')
    # logger.info(f'correct mean {out_wins.mean()} upset mean {out_loss.mean()}')
    # logger.info(f'correct percentiles: {np.percentile(out_wins, [10, 30, 50, 70, 90])}')
    # logger.info(f'upset percentiles: {np.percentile(out_loss, [10, 30, 50, 70, 90])}')

    # # do predictions
    # for scene in PREDICTIONS:
    #     logger.info('')
    #     logger.info(f'{scene["date"]} {scene["name"]}')
    #     for fight in scene['fights']:
    #         # skip if no odds:
    #         if 'odds' not in fight or not fight['odds']:
    #             continue
    #
    #         f1 = fight['fighters'][0]['name']
    #         f2 = fight['fighters'][1]['name']
    #
    #         win1_prob = win_probability([ratings[f1]], [ratings[f2]])
    #         win2_prob = win_probability([ratings[f2]], [ratings[f1]])
    #
    #         f1_odds = fight['odds'][f1]
    #         f2_odds = fight['odds'][f2]
    #
    #         # regressor betting
    #         scaled_data = scaler.transform([
    #             [
    #                 win1_prob,
    #                 win2_prob,
    #                 to_implied_odds(f1_odds),
    #                 to_implied_odds(f2_odds),
    #                 ratings[f1].mu,
    #                 ratings[f2].mu,
    #                 ratings[f1].sigma,
    #                 ratings[f2].sigma,
    #             ],
    #             [
    #                 win2_prob,
    #                 win1_prob,
    #                 to_implied_odds(f2_odds),
    #                 to_implied_odds(f1_odds),
    #                 ratings[f2].mu,
    #                 ratings[f1].mu,
    #                 ratings[f2].sigma,
    #                 ratings[f1].sigma,
    #             ]
    #         ])
    #         pred1, pred2 = reg.predict(scaled_data)
    #         if pred1 > pred2:
    #             logger.info(f'Bet on {f1} [{pred1*100:.0f}% {f1_odds}] (against {f2} [{pred2*100:.0f}% {f2_odds}])')
    #         else:
    #             logger.info(f'Bet on {f2} [{pred2*100:.0f}% {f2_odds}] (against {f1} [{pred1*100:.0f}% {f1_odds}])')

    logger.info('Done')


if __name__ == '__main__':
    main()
