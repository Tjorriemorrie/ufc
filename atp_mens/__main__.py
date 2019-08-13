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
from .data_2019_06 import DATA_2019_06


def win_probability(team1, team2):
    delta_mu = sum(r.mu for r in team1) - sum(r.mu for r in team2)
    sum_sigma = sum(r.sigma ** 2 for r in chain(team1, team2))
    size = len(team1) + len(team2)
    denom = sqrt(size * (BETA * BETA) + sum_sigma)
    ts = global_env()
    return ts.cdf(delta_mu / denom)


def get_regressor(X_train, y_train, X_test=None, y_test=None, **params):
    """get regressor"""
    #logger.info('')
    #logger.info('Training model...')

    eval_set = [(np.array(X_train), y_train)]
    if X_test and y_test:
        eval_set.append((np.array(X_test), y_test))

    reg = XGBRegressor(objective='reg:squarederror', n_jobs=4, **params)
    reg = reg.fit(X_train, y_train, eval_set=eval_set, eval_metric='rmse', verbose=0)

    return reg


def main(hyper_params, bet_params, train=''):
    #logger.info('Starting main training')

    all_data = DATA_2018_10 + DATA_2019_01 + DATA_2019_02 + DATA_2019_03 + DATA_2019_04 + DATA_2019_05 + DATA_2019_06 + DATA

    upsets_cutoff, whitewashes_cutoff, \
        estimators, max_depth, gamma, min_child_weight, learning_rate, scale_pos_weight = hyper_params
    upsets_cutoff = int(round(upsets_cutoff))
    whitewashes_cutoff = int(round(whitewashes_cutoff))
    reg_params = {
        'estimators': int(round(estimators * 100)),
        'max_depth': int(round(max_depth)),
        'gamma': gamma,
        'min_child_weight': int(round(min_child_weight)),
        'learning_rate': learning_rate,
        'scale_pos_weight': scale_pos_weight,
    }

    bet_pred_a, bet_pred_b, bet_pred_c, \
        bet_odds_a, bet_odds_b, bet_odds_c = bet_params

    # init
    reg = None
    scaler = MinMaxScaler()
    cutoff = int(len(all_data) * 0.7)
    start_date = None
    ratings = defaultdict(lambda: Rating())
    upsets = defaultdict(lambda: [])
    whitewashes = defaultdict(lambda: [])
    X_train = []
    y_train = []
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
    for i, event in enumerate(all_data):
        bet_size = 1
        is_training = i < cutoff
        if not is_training:
            if not reg:
                start_date = datetime.strptime(event['date'], '%Y-%m-%d')
                # scale
                scaler.partial_fit(X_train)
                X_train = scaler.transform(X_train)
                reg = get_regressor(X_train, y_train, **reg_params)
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

            # comebacks
            p1_whitewashes = sum(whitewashes[p1])
            p2_whitewashes = sum(whitewashes[p2])

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
                    p1_scaled_odds,
                    p1_odds,
                    p2_odds,
                    ratings[p1].mu,
                    ratings[p2].mu,
                    ratings[p1].sigma,
                    ratings[p2].sigma,
                    match['round'],
                    p1_upsets,
                    p2_upsets,
                    p1_whitewashes,
                    p2_whitewashes,
                ],
                [
                    win2_prob,
                    p2_scaled_odds,
                    p2_odds,
                    p1_odds,
                    ratings[p2].mu,
                    ratings[p1].mu,
                    ratings[p2].sigma,
                    ratings[p1].sigma,
                    match['round'],
                    p2_upsets,
                    p1_upsets,
                    p2_whitewashes,
                    p1_whitewashes,
                ]
            ]

            #########################################
            # update here as next sections can skip ahead
            if 'score' in match:

                # update whitewashes
                # if not match.get('retired'):
                whitewash = all(g[0] > g[1] for g in match['score'])
                whitewashes[p1] = whitewashes[p1][-whitewashes_cutoff:] + [1 if whitewash else 0]
                whitewashes[p2] = whitewashes[p2][-whitewashes_cutoff:] + [-1 if whitewash else 0]

                # update upsets
                upset = win2_prob > 0.50
                upsets[p1] = upsets[p1][-upsets_cutoff:] + [1 if upset else 0]
                upsets[p2] = upsets[p2][-upsets_cutoff:] + [-1 if upset else 0]

                # update ratings
                ratings[p1], ratings[p2] = rate_1vs1(ratings[p1], ratings[p2])

            ###################################
            # train
            if is_training:
                X_train.extend(match_data)
                y_train.extend([1, 0])

            ###################################
            # test
            else:
                scaled_match_data = scaler.transform(match_data)
                p1_pred, p2_pred = reg.predict(scaled_match_data)

                ###############################
                # bet scaling
                bet_multi = 1

                # pred
                pred_max = max(p1_pred, p2_pred)
                bet_pred_multi = np.polyval([bet_pred_a, bet_pred_b, bet_pred_c], [pred_max])[0]
                bet_pred_multi = int(min(max(round(bet_pred_multi), 0), 3))
                bet_multi += bet_pred_multi
                bet_multis_cat.append(f'bet_pred_multi-{bet_pred_multi}')

                # odds
                odds_diff = abs(1 / p1_odds - 1 / p2_odds)
                bet_odds_multi = np.polyval([bet_odds_a, bet_odds_b, bet_odds_c], [odds_diff])[0]
                bet_odds_multi = int(min(max(round(bet_odds_multi), 0), 3))
                bet_multi += bet_odds_multi
                bet_multis_cat.append(f'bet_odds_multi-{bet_odds_multi}')

                bet_amt = bet_size * bet_multi
                bet_amts.append(bet_amt)
                bet_multis.append(bet_multi)
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
    # reg = get_regressor(X_train, y_train, X_test, y_test, **reg_params)
    reg_score = reg.evals_result()
    params = reg.get_params()
    #logger.info(f'Num estimators: {params["n_estimators"]}')
    #logger.info(f'Learning rate: {params["learning_rate"]:.2f}')
    #logger.info(f'Max depth: {params["max_depth"]}')
    #logger.info(f'Accuracy: training={reg_score["validation_0"]["rmse"][-1]:.4f}% testing={reg_score["validation_1"]["rmse"][-1]:.4f}%')
    feature_names = [
        'win%', 'odds_scaled',
        'odds', '~odds',
        'mu', '~mu', 'sigma', '~sigma',
        'round',
        'upsets', '~upsets',
        'whitewashes', '~whitewashes',
    ]
    features = {k: round(v * 100) for k, v in zip(feature_names, reg.feature_importances_)}
    #logger.info(f'Features: {features}')

    if accuracy[1]:
        payouts = np.array(payouts)
        #logger.info('')
        #logger.info('Testing:')
        #logger.info(f'Accuracy {accuracy[0]}/{accuracy[1]} = {accuracy[0]/accuracy[1]*100:.1f}%')
        #logger.info(f'ROI {sum(payouts) / sum(bet_amts) * 100:.1f}%  Profit ${sum(payouts):.0f}')
        days = (datetime.now() - start_date).days
        #logger.info(f'Profit: per day: ${sum(payouts) / days:.2f}  per bet ${payouts.mean():.2f}')
        #logger.info(f'Common multis: {Counter(bet_multis).most_common(5)}')
        #logger.info(f'cat multis: {Counter(bet_multis_cat).most_common()}')

    if actual[1]:
        tab = np.array(tab)
        #logger.info('')
        #logger.info('Actual:')
        #logger.info(f'Accuracy {actual[0]}/{actual[1]} = {actual[0]/actual[1] * 100:.1f}%')
        #logger.info(f'ROI {sum(tab) / sum(tab_amts) * 100:.2f}%  Profit ${sum(tab):.0f}')
        days = (datetime.now() - datetime(2019, 7, 24)).days
        #logger.info(f'Profit: per day: ${sum(tab) / days:.2f}  per bet ${tab.mean():.2f}')

    if train == 'hyper':
        print(f'ROI {sum(payouts) / sum(bet_amts) * 100:.1f}%  Profit ${sum(payouts):.0f}')
        return -(sum(payouts) / sum(bet_amts))
        # rmse_train = reg_score['validation_0']['rmse'][-1]
        # rmse_test = reg_score['validation_1']['rmse'][-1]
        # print(f'RMSE: train={rmse_train:.4f} test={rmse_test:.4f}')
        # return rmse_test + rmse_train / 10
    elif train == 'bet':
        print(f'ROI {sum(payouts) / sum(bet_amts) * 100:.1f}%  Profit ${sum(payouts):.0f}')
        return -(sum(payouts) / sum(bet_amts))


if __name__ == '__main__':
    # add
    # age
    # court surface
    # serve strength
    # rested
    # weather
    hyper_flag = 1
    hyper_names = ['upsets cutoff', 'whitewashes_cutoff', 'estimators',  # size  100
                   'max_depth', 'gamma', 'min_child_weight',  # overfitting  3, 0, 1,
                   'learning_rate/eta', 'scale_pos_weight'  # noise robustness  0.1, 1
                   ]
    [9.042564756925078, 15.542885368208834, 1.5639593104751492, 6.835386084613393,
     1.2964123313731617, 8.211606571200019, 0.9281251435466975, 2.942233168900167]
    hyper_params = [9.705877804071598, 13.233952458847869, 2.0816843771245583, 6.5953568386070645, 4.3182143716209085, 6.842954977459012, 0.6793899674698676, 1.000948313799765]
    hyper_bounds = [[0, 0, 0.01, 1, 0, 0, 0, 0],
                    [100, 100, 10, 10, 10, 10, 1, 10]]
    assert len(hyper_params) == len(hyper_names)

    bet_flag = 0
    bet_names = ['pred a', 'pred b', 'pred c',
                 'odds a', 'odds b', 'odds c']
    bet_params = [47.40052102580894, -28.754717986288373, -32.57767911821454, -21.09265569173918, -66.15453983752992, 9.085218344300873]
    bet_bounds = [[-100], [100]]
    assert len(bet_params) == len(bet_names)

    if hyper_flag:
        es = CMAEvolutionStrategy(hyper_params, 0.5, {'bounds': hyper_bounds})
        while not es.stop():
            solutions = es.ask()
            fitness = [main(x, bet_params, train='hyper') for x in solutions]
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
    elif bet_flag:
        es = CMAEvolutionStrategy(bet_params, 1, {'bounds': bet_bounds})
        while not es.stop():
            solutions = es.ask()
            fitness = [main(hyper_params, x, train='bet') for x in solutions]
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
    else:
        main(hyper_params, bet_params)
