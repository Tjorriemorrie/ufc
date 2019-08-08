from collections import Counter, defaultdict
from datetime import datetime
from itertools import chain

import numpy as np
from cma import CMAEvolutionStrategy
from loguru import logger
from math import sqrt
from sklearn.preprocessing import MinMaxScaler
from trueskill import BETA, global_env, rate_1vs1, Rating
from xgboost import XGBRegressor

from .data import DATA
from .data_2018_10 import DATA_2018_10
from .data_2019_01 import DATA_2019_01
from .data_2019_02 import DATA_2019_02
from .data_2019_03 import DATA_2019_03
from .data_2019_04 import DATA_2019_04
from .data_2019_05 import DATA_2019_05


def win_probability(team1, team2):
    delta_mu = sum(r.mu for r in team1) - sum(r.mu for r in team2)
    sum_sigma = sum(r.sigma ** 2 for r in chain(team1, team2))
    size = len(team1) + len(team2)
    denom = sqrt(size * (BETA * BETA) + sum_sigma)
    ts = global_env()
    return ts.cdf(delta_mu / denom)


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
    # score = reg.score(X_test, )
    # #logger.info(f'Accuracy score: {accuracy*100:.0f}%')
    # mse = mean_squared_error(y_test, y_pred)
    # #logger.info(f'MSE: {mse:.2f}')
    # sleep(3)
    # pyplot.bar(range(len(model.feature_importances_)), model.feature_importances_)
    # pyplot.show()

    return reg


def main(bet_params=None):
    #logger.info('Starting main training')

    all_data = DATA_2018_10 + DATA_2019_01 + DATA_2019_02 + DATA_2019_03 + DATA_2019_04 + DATA_2019_05 + DATA
    # all_data = DATA_2019_01 + DATA_2019_02 + DATA_2019_03 + DATA_2019_04 + DATA_2019_05 + DATA
    estimators, max_depth, upsets_cutoff, \
        bet_pred_bot_a, bet_pred_bot_b, bet_pred_top_a, bet_pred_top_b, \
        bet_rnd_bot_a, bet_rnd_bot_b, bet_rnd_top_a, bet_rnd_top_b, \
        bet_upset_bot_a, bet_upset_bot_b, bet_upset_top_a, bet_upset_top_b, = bet_params
    estimators = int(round(estimators * 100))
    max_depth = int(round(max_depth))
    upsets_cutoff = int(round(upsets_cutoff))

    # init
    reg = None
    scaler = MinMaxScaler()
    cutoff = int(len(all_data) * 0.7)
    start_date = None
    ratings = defaultdict(lambda: Rating())
    upsets = defaultdict(lambda: [])
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

    # loop through scenes
    for i, event in enumerate(all_data):
        bet_size = 1
        is_training = i < cutoff
        if not is_training:
            if not reg:
                start_date = datetime.strptime(event['date'], '%Y-%m-%d')
                reg = get_regressor(training_data, label_data, scaler, estimators=estimators, max_depth=max_depth)
            #logger.info('')
        #logger.info(f'{event["date"]} {event["name"]}')

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

            # upsets
            p1_upsets = sum(upsets[p1])
            p2_upsets = sum(upsets[p2])

            # evs
            odds_sum = p1_odds + p2_odds
            p1_scaled_odds = p1_odds / odds_sum
            p2_scaled_odds = p2_odds / odds_sum

            match_data = [
                [
                    win1_prob,
                    p1_odds,
                    p2_odds,
                    ratings[p1].mu,
                    ratings[p2].mu,
                    ratings[p1].sigma,
                    ratings[p2].sigma,
                    match['round'],
                    p1_upsets,
                    p2_upsets,
                    p1_scaled_odds,
                ],
                [
                    win2_prob,
                    p2_odds,
                    p1_odds,
                    ratings[p2].mu,
                    ratings[p1].mu,
                    ratings[p2].sigma,
                    ratings[p1].sigma,
                    match['round'],
                    p2_upsets,
                    p1_upsets,
                    p2_scaled_odds,
                ]
            ]

            #########################################
            # update here as next sections can skip ahead
            if 'score' in match:

                # update upsets
                upset = win2_prob > 0.50
                upsets[p1] = upsets[p1][-upsets_cutoff:] + [1 if upset else 0]
                upsets[p2] = upsets[p2][-upsets_cutoff:] + [-1 if upset else 0]

                # update ratings
                ratings[p1], ratings[p2] = rate_1vs1(ratings[p1], ratings[p2])

            ###################################
            # cannot bet on qualifiers
            # if match['round'] >= 256:
            #     continue

            ###################################
            # train
            if is_training:
                training_data.extend(match_data)
                label_data.extend([1, 0])

            ###################################
            # test
            else:
                scaled_match_data = scaler.transform(match_data)
                p1_pred, p2_pred = reg.predict(scaled_match_data)

                ###############################
                # bet scaling
                bet_multi = 1

                # pred
                bet_pred_bot_multi = np.polyval([bet_pred_bot_a, bet_pred_bot_b], [p1_pred])[0]
                bet_pred_bot_adj = min(max(round(bet_pred_bot_multi), 0), 3)
                bet_pred_top_multi = np.polyval([bet_pred_top_a, bet_pred_top_b], [p1_pred])[0]
                bet_pred_top_adj = min(max(round(bet_pred_top_multi), 0), 3)
                if not bet_pred_bot_adj or not bet_pred_top_adj:
                    bet_multi += bet_pred_bot_adj
                    bet_multi += bet_pred_top_adj

                # round
                rnd = 1 / match['round']
                bet_rnd_bot_multi = np.polyval([bet_rnd_bot_a, bet_rnd_bot_b], [rnd])[0]
                bet_rnd_bot_adj = min(max(round(bet_rnd_bot_multi), 0), 3)
                bet_rnd_top_multi = np.polyval([bet_rnd_top_a, bet_rnd_top_b], [rnd])[0]
                bet_rnd_top_adj = min(max(round(bet_rnd_top_multi), 0), 3)
                if not bet_rnd_bot_adj or not bet_rnd_top_adj:
                    bet_multi += bet_rnd_bot_adj
                    bet_multi += bet_rnd_top_adj

                # upset
                total_upsets = sum(upsets[p1]) + sum(upsets[p2])
                bet_upset_bot_multi = np.polyval([bet_upset_bot_a, bet_upset_bot_b], [total_upsets])[0]
                bet_upset_bot_adj = min(max(round(bet_upset_bot_multi), 0), 3)
                bet_upset_top_multi = np.polyval([bet_upset_top_a, bet_upset_top_b], [total_upsets])[0]
                bet_upset_top_adj = min(max(round(bet_upset_top_multi), 0), 3)
                if not bet_upset_bot_adj or not bet_upset_top_adj:
                    bet_multi += bet_upset_bot_adj
                    bet_multi += bet_upset_top_adj

                bet_multis.append(bet_multi)
                bet_amt = bet_size * bet_multi
                bet_amts.append(bet_amt)
                ###############################

                if 'prediction' in match and match['prediction'] is None:
                    if p1_pred > p2_pred:
                        predw = p1_pred
                        pw = p1
                        predl = p2_pred
                        pl = p2
                    else:
                        predw = p2_pred
                        pw = p2
                        predl = p1_pred
                        pl = p1
                    #logger.warning(f'[{predw*100:.0f}% vs {predl*100:.0f}%] Bet x{bet_multi} on {pw} to beat {pl} [{ratings[pw].mu:.0f} vs {ratings[pl].mu:.0f}]')
                    continue

                # prediction bet on
                elif 'score' not in match:
                    #logger.warning(f'Pending {p1} vs {p2}')
                    continue

                # add data for test of classifier
                X_test.extend(scaled_match_data)
                y_test.extend([1, 0])

                # testing outcome
                correct = 0
                payout = -bet_amt
                if p1_pred > p2_pred:
                    correct = 1
                    payout += p1_odds * bet_amt
                payouts.append(round(payout, 2))
                accuracy = (accuracy[0] + correct, accuracy[1] + 1)

                # actual outcome
                if 'bet' in match and 'score' in match:
                    is_actual_correct = match['prediction'] == p1
                    actual = (actual[0] + is_actual_correct, actual[1] + 1)
                    cash = -match['bet']
                    if is_actual_correct:
                        cash += p1_odds * match['bet']
                    tab.append(round(cash, 2))
                    tab_amts.append(match['bet'])

                log_balance = f'[{sum(payouts):.0f}|{payout:.0f}]'
                log_pred = f'[{p1_pred * 100:.0f}% vs {p2_pred * 100:.0f}%]'
                log_players = f'x{bet_multi} {p1} {match.get("score")} {p2}'
                log_odds = f'[{p1_odds:.2f} vs {p2_odds:.2f}]'
                log_trueskill = f'[{ratings[p1].mu:.0f}.{ratings[p1].sigma:.0f} vs {ratings[p2].mu:.0f}.{ratings[p2].sigma:.0f}]'
                #logger.info(f'{log_balance} {log_pred} {log_players} {log_odds} {log_trueskill}')

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
        'win%', 'odds', '~odds',
        'mu', '~mu', 'sigma', '~sigma',
        'round',
        'upsets', '~upsets',
        'odds_scaled',
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
        #logger.info(f'Common multis: {Counter(bet_multis).most_common(5)}')

    if actual[1]:
        tab = np.array(tab)
        #logger.info('')
        #logger.info('Actual:')
        #logger.info(f'Accuracy {actual[0]}/{actual[1]} = {actual[0]/actual[1] * 100:.1f}%')
        #logger.info(f'ROI {sum(tab) / sum(tab_amts) * 100:.2f}%  Profit ${sum(tab):.0f}')
        days = (datetime.now() - datetime(2019, 7, 24)).days
        #logger.info(f'Profit: per day: ${sum(tab) / days:.2f}  per bet ${tab.mean():.2f}')

    return -(sum(payouts) / sum(bet_amts))


if __name__ == '__main__':
    bet_params_names = ['estimators', 'max_depth',
                        'upsets cutoff',
                        'pred lower a', 'pred lower b',
                        'pred highter a', 'pred highter b',
                        'round lower a', 'round higher b',
                        'round highter a', 'round higher b',
                        'upset lower a', 'upset higher b',
                        'upset highter a', 'upset higher b']
    # bet_params = [10.082903911702275, 3.869989799718258, 3.0135043965375337, -19.204300581800386, 34.812524615827286, 44.30030226384012, -21.747153788292984, -16.77053431327639, 35.23408085279844, -1.037212765476975, -22.040156421000287, -15.859656622725607, 35.12502991926313, -1.336550064750914, -22.43509022495746]
    bet_params = [9.89124304587057, 4.105711802302772, 2.7982434376798175, -16.377576805127003, 35.68277141597596, 46.9652216386256, -23.36541254071933, -11.433383785603342, 35.911703324685625, -0.6901816808222626, -22.790770222940914, -21.43798611924857, 33.615895570559985, -1.3024792529812363, -19.588972058883634]

    [10.10454848531829, 3.827530900860531, 2.9936980881801882, 80.95353368501652, -39.17896986796353, 19.29923537097806,
     -51.77454436957093, -37.56874936915167, -6.00489111651426, 52.06225544015326, -80.7288615322545,
     -55.933789170080125, 41.86255991266292, -45.346516706067504, -180.54341840304]
    [10.081026108603481, 3.926814147452584, 2.7711688582979157, 83.70153838952294, -39.91866661861638,
     15.99916892392161, -50.80535343484398, -37.277388164345616, -5.229713887641487, 46.92658295843296,
     -84.76051216531731, -59.318792241193925, 41.41766454410793, -50.72899919458938, -189.46963614649573]

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

        print(f'finished after {es.result[3]} evaluations and {es.result[4]} iterations')

        print('')
        print('best')
        print(list(es.result[0]))

        print('')
        print('xfavorite: distribution mean in "phenotype" space, to be considered as current best estimate of the optimum')
        print(list(es.result[5]))
