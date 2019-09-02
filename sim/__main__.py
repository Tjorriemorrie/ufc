from datetime import datetime
from collections import Counter, defaultdict, OrderedDict
from itertools import chain
from random import random

import numpy as np
from cma import CMAEvolutionStrategy, CMAOptions
from loguru import logger
from math import sqrt
from sklearn.preprocessing import MinMaxScaler
from sortedcontainers import SortedDict
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


def get_regressor(X_train, y_train, X_test=None, y_test=None, **reg_params):
    """get regressor"""
    logger.info('')
    logger.info('Training model...')

    eval_set = [(np.array(X_train), y_train)]
    if X_test and y_test:
        eval_set.append((np.array(X_test), y_test))

    reg = XGBRegressor(objective='reg:squarederror', n_jobs=4, **reg_params)
    reg = reg.fit(X_train, y_train, eval_set=eval_set, eval_metric='auc', verbose=0)

    return reg


def main(hyper_params, train=0):
    logger.info('Starting main training')

    all_data = DATA_2016 + DATA_2017 + DATA_2018 + DATA

    # estimators, learning_rate = hyper_params
    # gamma, max_depth, min_child_weight = hyper_params
    # max_delta_step, subsample, scale_pos_weight = hyper_params
    reg_params = {
        'n_estimators': 100 if train else 1000,
        # 'learning_rate': 0.09426181829690375,  # 0.24678854038938264
        # 'gamma': 0.1860088097748791,  # 0.0012826703538762253,
        # 'max_depth': int(round(2.1956102758009424)),  # 2.5506573766936533)),
        # 'min_child_weight': 3.5802932556001426,
        # 'max_delta_step': 0.10779250505931337,
        # 'subsample': 0.9859889452465481,
        # 'scale_pos_weight': 1.2283288967549404,
    }

    # bet_pred_a, bet_pred_b, bet_odds_a, bet_odds_b, bet_wnl_a, bet_wnl_b = hyper_params
    bet_pred_a = 1.713980438805089   # -3.55
    bet_pred_b = -4.065137791049565  # -17.93
    bet_odds_a = 3.122323263774503   # -12.44
    bet_odds_b = 0.0837110561236318  # -16.17
    bet_wnl_a = 15.100288654913749   # -3.52   # -8.01
    bet_wnl_b = -10.111913271763338  # -4.96    # 2.50

    # bet_ts_a, bet_ts_b, bet_tmi_a, bet_tmi_b, bet_tma_a, bet_tma_b = hyper_params
    bet_ts_a = -50.59979897765422  # -26.88   # -3.52   # -8.01
    bet_ts_b = -69.5794588139756   # -72.60   # -3.52   # -8.01
    bet_tmi_a = -45.94904856923797
    bet_tmi_b = -1.128236337281963
    bet_tma_a = -28.62283185173976
    bet_tma_b = -26.933801584409544
    
    # init
    reg = None
    scaler = MinMaxScaler()
    cutoff = int(len(all_data) * 0.6)
    start_date = None
    ratings = defaultdict(lambda: Rating())
    wins_losses = defaultdict(lambda: [])
    early_fights = defaultdict(lambda: 0.5)
    last_fights = defaultdict(lambda: 0.5)
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
    actual_debug = []
    bet_multis = []
    bet_multis_cat = []
    preds_flipped = []
    odds_outcomes = []

    # loop through scenes
    for i, scene in enumerate(all_data):
        is_training = i < cutoff
        if not is_training:
            if not reg:
                start_date = datetime.strptime(scene['date'], '%Y-%m-%d')
                # scale
                scaler.partial_fit(X_train)
                X_train = scaler.transform(X_train)
                reg = get_regressor(X_train, y_train, **reg_params)
            logger.info('')
        logger.info(f'{scene["date"]} {scene["name"]}')

        for fight in scene['fights']:
            bet_size = 1
            # skip if no odds:
            if 'odds' not in fight:
                continue

            f1 = fight['fighters'][0]['name']
            f2 = fight['fighters'][1]['name']

            # trueskill data
            f1_ts = ratings[f1].mu
            f1_sigma = ratings[f1].sigma
            f2_ts = ratings[f2].mu
            f2_sigma = ratings[f2].sigma
            f1_ts_min = f1_ts - f1_sigma * 2
            f2_ts_min = f2_ts - f2_sigma * 2
            f1_ts_max = f1_ts + f1_sigma * 2
            f2_ts_max = f2_ts + f2_sigma * 2

            # odds data
            f1_odds = fight['odds'][f1]
            f2_odds = fight['odds'][f2]
            if not -50 < f1_odds < 50 or not -50 < f2_odds < 50:
                raise ValueError(f'surely these odds are wrong? {f1_odds} {f2_odds}')

            win1_prob = win_probability([ratings[f1]], [ratings[f2]])
            win2_prob = win_probability([ratings[f2]], [ratings[f1]])

            # wins losses data
            f1_wins_losses = Counter(wins_losses[f1])
            f1_wnl_winrate = f1_wins_losses[1] / max(1, len(wins_losses[f1]))
            f2_wins_losses = Counter(wins_losses[f2])
            f2_wnl_winrate = f2_wins_losses[1] / max(1, len(wins_losses[f2]))

            fight_data = [
                [
                    win1_prob,
                    f1_odds,
                    f2_odds,
                    f1_ts,
                    f2_ts,
                    f1_sigma,
                    f2_sigma,
                    f1_ts_min - f2_ts_min,
                    f1_ts - f2_ts,
                    f1_ts_max - f2_ts_max,
                    last_fights[f1],
                    last_fights[f2],
                    early_fights[f1],
                    early_fights[f2],
                    f1_wins_losses[1],
                    f1_wins_losses[-1],
                    f1_wnl_winrate,
                    f2_wins_losses[1],
                    f2_wins_losses[-1],
                    f2_wnl_winrate,
                ],
                [
                    win2_prob,
                    f2_odds,
                    f1_odds,
                    f2_ts,
                    f1_ts,
                    f2_sigma,
                    f1_sigma,
                    f2_ts_min - f1_ts_min,
                    f2_ts - f1_ts,
                    f2_ts_max - f1_ts_max,
                    last_fights[f2],
                    last_fights[f1],
                    early_fights[f2],
                    early_fights[f1],
                    f2_wins_losses[1],
                    f2_wins_losses[-1],
                    f2_wnl_winrate,
                    f1_wins_losses[1],
                    f1_wins_losses[-1],
                    f1_wnl_winrate,
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

                # update wins losses
                wins_losses[f1] += [1]
                wins_losses[f2] += [-1]

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
                if 'winner' in fight:
                    X_train.extend(fight_data)
                    y_train.extend([is_win_1, not is_win_1])

            ###################################
            # test
            else:
                scaled_fight_data = scaler.transform(fight_data)
                f1_pred, f2_pred = reg.predict(scaled_fight_data)

                #############################
                # bet scaling
                bet_multi = 1

                # pred max
                if f1_pred > f2_pred:
                    f_pred = f1_pred - f2_pred
                else:
                    f_pred = f2_pred - f1_pred
                bet_pred_multi = np.polyval([bet_pred_a, bet_pred_b], [f_pred])[0]
                bet_pred_multi = round(min(1, max(0, bet_pred_multi)))
                bet_multi += bet_pred_multi
                bet_multis_cat.append(f'pred:{bet_pred_multi:.0f}')

                # odds diff
                if f1_pred > f2_pred:
                    f_odds = 1 / f1_odds - 1 / f2_odds
                else:
                    f_odds = 1 / f2_odds - 1 / f1_odds
                bet_odds_multi = np.polyval([bet_odds_a, bet_odds_b], [f_odds])[0]
                bet_odds_multi = round(min(1, max(0, bet_odds_multi)))
                bet_multi += bet_odds_multi
                bet_multis_cat.append(f'odds:{bet_odds_multi:.0f}')

                # wins and losses
                if f1_pred > f2_pred:
                    f_wnl = f1_wnl_winrate - f2_wnl_winrate
                else:
                    f_wnl = f2_wnl_winrate - f1_wnl_winrate
                bet_wnl_multi = np.polyval([bet_wnl_a, bet_wnl_b], [f_wnl])[0]
                bet_wnl_multi = round(min(1, max(0, bet_wnl_multi)))
                bet_multi += bet_wnl_multi
                bet_multis_cat.append(f'wnl:{bet_wnl_multi:.0f}')

                # trueskill mu
                if f1_pred > f2_pred:
                    f_ts = f1_ts - f2_ts
                else:
                    f_ts = f2_ts - f1_ts
                bet_ts_multi = np.polyval([bet_ts_a, bet_ts_b], [f_ts])[0]
                bet_ts_multi = round(min(1, max(0, bet_ts_multi)))
                bet_multi += bet_ts_multi
                bet_multis_cat.append(f'ts:{bet_ts_multi:.0f}')

                # trueskill min
                if f1_pred > f2_pred:
                    f_ts_min = f1_ts_min - f2_ts_min
                else:
                    f_ts_min = f2_ts_min - f1_ts_min
                bet_tmi_multi = np.polyval([bet_tmi_a, bet_tmi_b], [f_ts_min])[0]
                bet_tmi_multi = round(min(1, max(0, bet_tmi_multi)))
                bet_multi += bet_tmi_multi
                bet_multis_cat.append(f'tmi:{bet_tmi_multi:.0f}')

                # trueskill max
                if f1_pred > f2_pred:
                    f_ts_max = f1_ts_max - f2_ts_max
                else:
                    f_ts_max = f2_ts_max - f1_ts_max
                bet_tma_multi = np.polyval([bet_tma_a, bet_tma_b], [f_ts_max])[0]
                bet_tma_multi = round(min(1, max(0, bet_tma_multi)))
                bet_multi += bet_tma_multi
                bet_multis_cat.append(f'tma:{bet_tma_multi:.0f}')

                bet_size *= round(bet_multi)
                bet_amt = round(bet_size * bet_multi)
                assert bet_amt >= 1, f'bet multi is fucked: {bet_multi}'
                bet_amts.append(bet_size)
                bet_multis.append(int(round(bet_multi)))
                #############################

                # prediction made
                if 'prediction' in fight and fight['prediction'] is None:
                    if f1_pred > f2_pred:
                        exp_winner = f1
                        pred_exp_winner = f1_pred
                        exp_loser = f2
                        pred_exp_loser = f2_pred
                    else:
                        exp_winner = f2
                        pred_exp_winner = f2_pred
                        exp_loser = f1
                        pred_exp_loser = f1_pred
                    logger.warning(f'[{pred_exp_winner * 100:.0f}% vs {pred_exp_loser * 100:.0f}%] Bet x{bet_multi} on {exp_winner} to beat {exp_loser} [{ratings[exp_winner].mu:.0f} vs {ratings[exp_loser].mu:.0f}]')
                    continue

                # good luck with your bets
                elif 'winner' not in fight:
                    logger.warning(f'Pending {f1} vs {f2}')
                    continue

                if is_win_1:
                    fw_pred = f1_pred
                    fl_pred = f2_pred
                else:
                    fw_pred = f2_pred
                    fl_pred = f1_pred

                # add test data
                X_test.extend(scaled_fight_data)
                y_test.extend([is_win_1, not is_win_1])

                # testing outcome
                correct = 0
                payout = -bet_size
                if is_win_1 and f1_pred > f2_pred:
                    correct = 1
                    payout += f1_odds * bet_size
                elif not is_win_1 and f2_pred > f1_pred:
                    correct = 1
                    payout += f2_odds * bet_size
                odds_outcomes.append(int((f1_odds < f2_odds and is_win_1) or (f2_odds > f1_odds and not is_win_1)))
                payouts.append(round(payout, 2))
                accuracy = (accuracy[0] + correct, accuracy[1] + 1)

                # actual outcome
                pred_flipped = False
                if 'bet' in fight:
                    is_actual_correct = fight['prediction'] == fw
                    actual = (actual[0] + is_actual_correct, actual[1] + 1)
                    cash = -fight['bet']
                    if is_actual_correct:
                        fw_odds = f1_odds if is_win_1 else f2_odds
                        cash += fw_odds * fight['bet']
                    else:
                        fw_odds = f2_odds if is_win_1 else f1_odds
                    tab.append(round(cash, 2))
                    tab_amts.append(fight['bet'])
                    # pred flipped?
                    pred_flipped = (f1_pred > f2_pred and fight['prediction'] != f1) or (
                        f2_pred > f1_pred and fight['prediction'] != f2)
                    actual_debug.append(f'${fight["bet"]} {fw_odds:.2f}: {cash:.2f} {fight["prediction"]} {fight["date"]}')
                preds_flipped.append(int(pred_flipped))

                log_balance = f'{"!!" if pred_flipped else "  "}[{sum(payouts):.0f}|{payout:.0f}]'
                log_pred = f'[{fw_pred * 100:.0f}% vs {fl_pred * 100:.0f}%]'
                log_fight = f'x{bet_multi} {fw} {fight["winner"]["by"]} {fl}'
                log_ratings = f'[{ratings[fw].mu:.0f} vs {ratings[fl].mu:.0f}]'
                logger.info(f'{log_balance} {log_pred} {log_fight} {log_ratings}')

    if train:
        total_payouts = sum(payouts)
        roi = total_payouts / sum(bet_amts)
        res = -roi - (total_payouts / 5000)
        print(f'Score: {-res*100:.2f}  ROI {roi * 100:.1f}%  Profit ${total_payouts:.0f}')
        return res
    else:
        summary(reg, accuracy, payouts, start_date, bet_amts, bet_multis, bet_multis_cat, actual, tab, tab_amts, odds_outcomes)


def summary(reg, accuracy, payouts, start_date, bet_amts, bet_multis, bet_multis_cat, actual, tab, tab_amts, odds_outcomes):
    logger.info('')
    logger.info('Tree info:')
    # reg = get_regressor(X_train, y_train, X_test, y_test, estimators=estimators, max_depth=max_depth)
    reg_score = reg.evals_result()
    params = reg.get_params()
    logger.info(f'Num estimators: {params["n_estimators"]}')
    logger.info(f'Learning rate: {params["learning_rate"]:.2f}')
    logger.info(f'Max depth: {params["max_depth"]}')
    logger.info(f'Accuracy: training={reg_score["validation_0"]["auc"][-1]*100:.0f}%')
    feature_names = [
        'win%',
        'odds', '~odds',
        'ts', '~ts', 'sigma', '~sigma',
        'ts_min_diff', 'ts_diff', 'ts_max_diff',
        'last', '~last',
        'early', '~early',
        'wins', '~wins', 'losses', '~losses', 'winrate', '~winrate',
    ]
    assert len(feature_names) == len(reg.feature_importances_), f'{len(feature_names)} features vs {len(reg.feature_importances_)} reg values'
    logger.info('')
    logger.info(f'Features:')
    features = SortedDict({v: k for k, v in zip(feature_names, reg.feature_importances_)})
    for k in features.keys():
        logger.info(f'{features[k]}: {k*1000:.0f}')
        continue

    if accuracy[1]:
        payouts = np.array(payouts)
        logger.info('')
        logger.info('Testing:')
        odds_acc = sum([t for t in odds_outcomes if t > 0]) / len(odds_outcomes)
        logger.info(f'Accuracy {accuracy[0]}/{accuracy[1]} = {accuracy[0]/accuracy[1]*100:.1f}%  Odds: {odds_acc*100:.1f}%')
        logger.info(f'ROI {sum(payouts) / sum(bet_amts) * 100:.1f}%  Profit ${sum(payouts):.0f}')
        days = (datetime.now() - start_date).days
        logger.info(f'Profit: per day: ${sum(payouts) / days:.2f}  per bet ${payouts.mean():.2f}')
        logger.info(f'Common multis: {Counter(bet_multis).most_common(4)}')
        logger.info(f'cat multis: {Counter(bet_multis_cat).most_common()}')

    if actual[1]:
        tab = np.array(tab)
        logger.info('')
        logger.info('Actual:')
        logger.info(f'Accuracy {actual[0]}/{actual[1]} = {actual[0]/actual[1] * 100:.1f}%')
        logger.info(f'ROI {sum(tab) / sum(tab_amts) * 100:.2f}%  Profit ${sum(tab):.0f}')
        days = (datetime.now() - datetime(2019, 7, 13)).days
        logger.info(f'Profit: per day: ${sum(tab) / days:.2f}  per bet ${tab.mean():.2f}')
        sheet = -62.62
        if abs(sum(tab) - sheet) > 0.01:
            for l in actual_debug:
                logger.warning(l)
            logger.error(f'debug! {sheet:.2f} != {sum(tab):.2f} diff {sum(tab) - sheet:.2f}')



def run():
    train = 0
    
    names = [
        # 'bet_pred_a', 'bet_pred_b', 'bet_odds_a', 'bet_odds_b', 'bet_wnl_a', 'bet_wnl_b',
        'bet_ts_a', 'bet_ts_b', 'bet_tmi_a', 'bet_tmi_b', 'bet_tma_a', 'bet_tma_b',
    ]
    params = [
        0, 0, 0, 0, 0, 0
    ]
    bounds = [[-np.inf],
              [np.inf]]
    assert len(params) == len(names)
    # assert len(params) == len(bounds[0])

    if train:
        sigma = 1
        opts = CMAOptions()
        # opts['tolx'] = 1E-2
        opts['bounds'] = bounds
        es = CMAEvolutionStrategy(params, sigma, inopts=opts)
        while not es.stop():
            solutions = es.ask()
            fitness = [main(x, train=1) for x in solutions]
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

    else:
        main(params)


if __name__ == '__main__':
    run()
