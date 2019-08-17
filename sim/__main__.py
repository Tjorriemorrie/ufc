from datetime import datetime
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
    reg_params = {
        'n_estimators': int(round(2.1418721633783804 * 100)),  # 0.8844565933947343
        'learning_rate': 0.09426181829690375,  # 0.24678854038938264
        'gamma': 0.1860088097748791,  # 0.0012826703538762253,
        'max_depth': int(round(2.1956102758009424)),  # 2.5506573766936533)),
        'min_child_weight': 3.5802932556001426,
    }

    # bet_wnl_a, bet_wnl_b, bet_wnl_c, wnl_cutoff = hyper_params
    bet_wnl_a = -8.012210880048535
    bet_wnl_b = 2.5088843631312976
    bet_wnl_c = 7.9520665992548185
    wnl_cutoff = int(round(11.139996105926942 * 10))

    # bet_pred_a, bet_pred_b, bet_pred_c, bet_odds_a, bet_odds_b, bet_odds_c = hyper_params
    bet_pred_a = -3.5593760484773904
    bet_pred_b = -17.93424439517361
    bet_pred_c = -2.7073747762723555
    bet_odds_a = -12.444287120215446
    bet_odds_b = -16.179599063909983
    bet_odds_c = 3.8586041364734887

    # init
    reg = None
    scaler = MinMaxScaler()
    cutoff = int(len(all_data) * 0.7)
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
    bet_multis = []
    bet_multis_cat = []
    preds_flipped = []

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

            f1_odds = fight['odds'][f1]
            f2_odds = fight['odds'][f2]
            if not -50 < f1_odds < 50 or not -50 < f2_odds < 50:
                raise ValueError(f'surely these odds are wrong? {f1_odds} {f2_odds}')

            win1_prob = win_probability([ratings[f1]], [ratings[f2]])
            win2_prob = win_probability([ratings[f2]], [ratings[f1]])

            # wins losses
            f1_wins_losses = Counter(wins_losses[f1])
            f1_wnl_winrate = f1_wins_losses[1] / max(1, len(wins_losses[f1]))
            f2_wins_losses = Counter(wins_losses[f2])
            f2_wnl_winrate = f2_wins_losses[1] / max(1, len(wins_losses[f2]))

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
                    ratings[f2].mu,
                    ratings[f1].mu,
                    ratings[f2].sigma,
                    ratings[f1].sigma,
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
                wins_losses[f1] = wins_losses[f1][-wnl_cutoff:] + [1]
                wins_losses[f2] = wins_losses[f2][-wnl_cutoff:] + [-1]

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
                pred1, pred2 = reg.predict(scaled_fight_data)

                #############################
                # bet scaling
                bet_multi = 1

                # wins and losses
                if pred1 > pred2:
                    p_wnl = f1_wnl_winrate - f2_wnl_winrate
                else:
                    p_wnl = f2_wnl_winrate - f1_wnl_winrate
                bet_wnl_multi = np.polyval([bet_wnl_a, bet_wnl_b, bet_wnl_c], [p_wnl])[0]
                bet_wnl_multi = int(min(max(round(bet_wnl_multi), 0), 2))
                bet_multi += bet_wnl_multi
                bet_multis_cat.append(f'bet_wnl_multi-{bet_wnl_multi}')

                # pred max
                pred_max = max(pred1, pred2)
                bet_pred_multi = np.polyval([bet_pred_a, bet_pred_b, bet_pred_c], [pred_max])[0]
                bet_pred_multi = int(min(max(round(bet_pred_multi), 0), 3))
                bet_multi += bet_pred_multi
                bet_multis_cat.append(f'bet_pred_multi-{bet_pred_multi}')

                # odds diff
                odds_diff = abs(1 / f1_odds - 1 / f2_odds)
                bet_odds_multi = np.polyval([bet_odds_a, bet_odds_b, bet_odds_c], [odds_diff])[0]
                bet_odds_multi = int(min(max(round(bet_odds_multi), 0), 3))
                bet_multi += bet_odds_multi
                bet_multis_cat.append(f'bet_odds_multi-{bet_odds_multi}')

                bet_multis.append(bet_multi)
                bet_size *= bet_multi
                bet_amts.append(bet_size)
                #############################

                # prediction made
                if 'prediction' in fight and fight['prediction'] is None:
                    if pred1 > pred2:
                        exp_winner = f1
                        pred_exp_winner = pred1
                        exp_loser = f2
                        pred_exp_loser = pred2
                    else:
                        exp_winner = f2
                        pred_exp_winner = pred2
                        exp_loser = f1
                        pred_exp_loser = pred1
                    logger.warning(f'[{pred_exp_winner * 100:.0f}% vs {pred_exp_loser * 100:.0f}%] Bet x{bet_multi} on {exp_winner} to beat {exp_loser} [{ratings[exp_winner].mu:.0f} vs {ratings[exp_loser].mu:.0f}]')
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

                # add test data
                X_test.extend(scaled_fight_data)
                y_test.extend([is_win_1, not is_win_1])

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
                pred_flipped = False
                if 'bet' in fight:
                    is_actual_correct = fight['prediction'] == fw
                    actual = (actual[0] + is_actual_correct, actual[1] + 1)
                    cash = -fight['bet']
                    if is_actual_correct:
                        fw_odds = f1_odds if is_win_1 else f2_odds
                        cash += fw_odds * fight['bet']
                    tab.append(round(cash, 2))
                    tab_amts.append(fight['bet'])
                    # pred flipped?
                    pred_flipped = (pred1 > pred2 and fight['prediction'] != f1) or (
                        pred2 > pred1 and fight['prediction'] != f2)
                preds_flipped.append(int(pred_flipped))

                log_balance = f'{"!!" if pred_flipped else "  "}[{sum(payouts):.0f}|{payout:.0f}]'
                log_pred = f'[{fw_pred * 100:.0f}% vs {fl_pred * 100:.0f}%]'
                log_fight = f'x{bet_multi} {fw} {fight["winner"]["by"]} {fl}'
                log_ratings = f'[{ratings[fw].mu:.0f} vs {ratings[fl].mu:.0f}]'
                logger.info(f'{log_balance} {log_pred} {log_fight} {log_ratings}')

    if train:
        print(f'ROI {sum(payouts) / sum(bet_amts) * 100:.1f}%  Profit ${sum(payouts):.0f}')
        return -(sum(payouts) / sum(bet_amts))
    else:
        summary(reg, accuracy, payouts, start_date, bet_amts, bet_multis, bet_multis_cat, actual, tab, tab_amts)


def summary(reg, accuracy, payouts, start_date, bet_amts, bet_multis, bet_multis_cat, actual, tab, tab_amts):
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
        'mu', '~mu',
        'sigma', '~sigma',
        'last', '~last',
        'early', '~early',
        'wins', '~wins', 'losses', '~losses', 'winrate', '~winrate',
    ]
    features = {k: int(v * 100) for k, v in zip(feature_names, reg.feature_importances_)}
    logger.info(f'Features: {features}')

    if accuracy[1]:
        payouts = np.array(payouts)
        logger.info('')
        logger.info('Testing:')
        logger.info(f'Accuracy {accuracy[0]}/{accuracy[1]} = {accuracy[0]/accuracy[1]*100:.1f}%')
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


def run():
    train = 0
    
    names = [
        # 'estimators', 'learning_rate',
        # 'gamma', 'max depth',
        # 'bet_wnl_a', 'bet_wnl_b', 'bet_wnl_c', 'wnl_cutoff'
        'gamma', 'max_depth', 'min_child_weight',
    ]
    params = [
        0, 3, 1
    ]
    bounds = [[0, 0, 0],
              [np.inf,  np.inf,  np.inf]]
    assert len(params) == len(names)
    assert len(params) == len(bounds[0])

    if train:
        es = CMAEvolutionStrategy(params, 1, {'bounds': bounds})
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
