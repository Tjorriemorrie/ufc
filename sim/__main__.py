from collections import Counter, defaultdict, OrderedDict
from itertools import chain

import numpy as np
from loguru import logger
from math import sqrt
from sklearn.preprocessing import MinMaxScaler
from trueskill import BETA, global_env, rate_1vs1, Rating
from xgboost import XGBRegressor

from data import DATA


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
        'last', '~last', 'early', '~early',
        'wins', '~wins', 'losses', '~losses',
        'track', '~track']
    for name, val in zip(feature_names, reg.feature_importances_):
        logger.info(f'{name}: {val}')

    return reg


def main():
    logger.info('Starting main training')

    # init
    out_to_preds = {
        0: [],
        1: [],
    }
    reg = None
    scaler = MinMaxScaler()
    cutoff = int(len(DATA) * 0.7)
    ratings = defaultdict(lambda: Rating())
    early_fights = defaultdict(lambda: 0.5)
    last_fights = defaultdict(lambda: 0.5)
    training_data = []
    label_data = []
    payouts = []
    accuracy = (0, 0)
    tab = []
    actual = (0, 0)

    # loop through scenes
    for i, scene in enumerate(DATA):
        bet_size = max(sum(payouts), 200) // 20
        is_training = i < cutoff
        if not is_training:
            logger.info('')
            logger.info(f'{scene["date"]} {scene["name"]}')

        for fight in scene['fights']:
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

            # get winner
            fw = fight['winner']['fighter']
            is_win_1 = fw == f1
            fl = f2 if is_win_1 else f1
            if not is_win_1 and fw != f2 and fw is not None:
                raise ValueError(f'unknown winner {fw}')
            drawn = fw is None

            # wins and losses
            wins_and_losses_1 = fight['fighters'][0]['stats'].split('-')
            wins_and_losses_2 = fight['fighters'][1]['stats'].split('-')

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
                    win1_prob,
                    1 / f2_odds,
                    1 / f1_odds,
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

            ###################################
            # train
            if is_training:
                training_data.extend(fight_data)
                label_data.extend([is_win_1, not is_win_1])

            ###################################
            # test
            else:
                if not reg:
                    reg = get_regressor(training_data, label_data, scaler)

                scaled_fight_data = scaler.transform(fight_data)
                pred1, pred2 = reg.predict(scaled_fight_data)
                if is_win_1:
                    predw = pred1
                    predl = pred2
                    out_to_preds[1].append(round(pred1 - pred2, 2))
                else:
                    predw = pred2
                    predl = pred1
                    out_to_preds[0].append(round(pred2 - pred1, 2))

                # testing outcome
                correct = 0
                multi = 2 if pred1 - pred2 > 0.25 else 1
                multi *= 2 if pred1 - pred2 > 0.4 else 1
                payout = -bet_size * multi
                if is_win_1 and pred1 > pred2:
                    correct = 1
                    payout += f1_odds * bet_size * multi
                elif not is_win_1 and pred2 > pred1:
                    correct = 1
                    payout += f2_odds * bet_size * multi
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

                logger.info(f'[{sum(payouts):.0f}|{payout:.0f}] [{predw * 100:.0f}% vs {predl * 100:.0f}%] {fw} {fight["winner"]["by"]} {fl} [{ratings[fw].mu:.0f} vs {ratings[fl].mu:.0f}]')

            # update ratings
            ratings[fw], ratings[fl] = rate_1vs1(ratings[fw], ratings[fl], drawn=drawn)

            # update fights
            early_fights[fw] = last_fights[fw]
            early_fights[fl] = last_fights[fl]
            last_fights[fw] = 1
            last_fights[fl] = 0

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


# from trueskill import Rating, quality_1vs1, rate_1vs1
# alice, bob = Rating(25), Rating(30)  # assign Alice and Bob's ratings
# if quality_1vs1(alice, bob) < 0.50:
#     print('This match seems to be not so fair')
# alice, bob = rate_1vs1(alice, bob)  # update the ratings after the match
