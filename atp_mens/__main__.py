from collections import Counter, defaultdict
from datetime import datetime
from itertools import chain

import numpy as np
from cma import CMAEvolutionStrategy
from loguru import logger
from math import sqrt
from scipy.stats import linregress
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


def get_regressor(X_train, y_train, X_test=None, y_test=None, **reg_params):
    """get regressor"""
    logger.info('')
    logger.info('Training model...')

    eval_set = [(np.array(X_train), y_train)]
    if X_test and y_test:
        eval_set.append((np.array(X_test), y_test))

    reg = XGBRegressor(
        objective='reg:squarederror', n_jobs=4,

        # Step size shrinkage used in update to prevents overfitting. After each boosting step, we
        # can directly get the weights of new features, and eta shrinks the feature weights to make
        # the boosting process more conservative.
        # learning_rate=0.3,

        # Minimum loss reduction required to make a further partition on a leaf node of the tree. The larger gamma is,
        # the more conservative the algorithm will be.
        # gamma=0,

        # Maximum depth of a tree. Increasing this value will make the model more complex and more
        # likely to overfit. 0 is only accepted in lossguided growing policy when tree_method is
        # set as hist and it indicates no limit on depth. Beware that XGBoost aggressively consumes
        # memory when training a deep tree.
        # max_depth=3,

        # Minimum sum of instance weight (hessian) needed in a child. If the tree partition step
        # results in a leaf node with the sum of instance weight less than min_child_weight, then
        # the building process will give up further partitioning. In linear regression task, this
        # simply corresponds to minimum number of instances needed to be in each node. The larger
        # min_child_weight is, the more conservative the algorithm will be.
        # min_child_weight=1,

        # Maximum delta step we allow each leaf output to be. If the value is set to 0, it means
        # there is no constraint. If it is set to a positive value, it can help making the update
        # step more conservative. Usually this parameter is not needed, but it might help in
        # logistic regression when class is extremely imbalanced. Set it to value of 1-10 might
        # help control the update.
        # max_delta_step=0,

        # Subsample ratio of the training instances. Setting it to 0.5 means that XGBoost would
        # randomly sample half of the training data prior to growing trees. and this will prevent
        # overfitting. Subsampling will occur once in every boosting iteration.
        # subsample=1,

        # Control the balance of positive and negative weights, useful for unbalanced classes. A
        # typical value to consider: sum(negative instances) / sum(positive instances).
        # scale_pos_weight=1,

        ############################################
        # Regularization

        # L2 regularization term on weights. Increasing this value will make model more conservative.
        # reg_lambda=1,

        # L1 regularization term on weights. Increasing this value will make model more conservative.
        # reg_alpha=0,

        ############################################
        # This is a family of parameters for subsampling of columns.. colsample_by* parameters
        # work cumulatively

        # is the subsample ratio of columns when constructing each tree. Subsampling occurs once
        # for every tree constructed.
        # colsample_bytree=1,

        # is the subsample ratio of columns for each level. Subsampling occurs once for every new
        # depth level reached in a tree. Columns are subsampled from the set of columns chosen for
        # the current tree.
        # colsample_bylevel=1,

        # is the subsample ratio of columns for each node (split). Subsampling occurs once every
        # time a new split is evaluated. Columns are subsampled from the set of columns chosen for
        # the current level.
        # colsample_bynode=1,

        **reg_params)
    reg = reg.fit(X_train, y_train, eval_set=eval_set, eval_metric='rmse', verbose=0)

    return reg


def main(hyper_params, train=0):
    logger.info('Starting main training')

    all_data = DATA_2018_10 + DATA_2019_01 + DATA_2019_02 + DATA_2019_03 + DATA_2019_04 + DATA_2019_05 + DATA_2019_06 + DATA

    # reg_lambda, reg_alpha, \

    # estimators, learning_rate = hyper_params
    # gamma, max_depth, min_child_weight = hyper_params
    # max_delta_step, subsample, scale_pos_weight = hyper_params
    reg_params = {
        'n_estimators': int(round(2.1788282223375672 * 100)),
        'learning_rate': 0.31052718461617523,
        'gamma': 0.1480916400109764,  # 1.0931334779261526,
        'max_depth': int(round(4.59282984572512)),  # 2.605884221401324)),
        'min_child_weight': 1.0956345040972018,  # 0.86383038291261,
        'max_delta_step': 0.5808271528189928,  # 0.19995566873577586,
        'subsample': 0.8792477583008574,  # 0.9922978010805564,
        'scale_pos_weight': 0.49606238825608306,  # 0.8825017324048802,
        'reg_lambda': 0.7106544893592536,
        'reg_alpha': 0.010303112390348092,
        'colsample_bytree': 0.999790544478916,
        'colsample_bylevel': 0.9999562489678556,
        'colsample_bynode': 0.98799098337194,
    }

    # upsets_cutoff, whitewashes_cutoff, doors_cutoff, surface_cutoff, wnl_cutoff = hyper_params
    upsets_cutoff = int(round(1.3627577408735392 * 10))
    whitewashes_cutoff = int(round(1.568914833462892 * 10))

    # bet_pred_a, bet_pred_b, bet_pred_c, bet_odds_a, bet_odds_b, bet_odds_c = hyper_params
    bet_pred_a = -57.72765234484444
    bet_pred_b = -35.12339940099521
    bet_pred_c = 42.20397841611924
    bet_odds_a = -6.625846643088274
    bet_odds_b = -44.60842535679358
    bet_odds_c = 9.50444367073803

    # bet_wnl_a, bet_wnl_b, bet_wnl_c, wnl_cutoff = hyper_params
    bet_wnl_a = 112.93331722962265
    bet_wnl_b = -274.4787183334988
    bet_wnl_c = -5.239133097906791
    wnl_cutoff = int(round(184.7912281857989 * 10))

    # bet_drs_a, bet_drs_b, bet_drs_c, doors_cutoff = hyper_params
    bet_drs_a = -21.440152399884028
    bet_drs_b = 9.162822051826854
    bet_drs_c = -15.863824751108206
    doors_cutoff = int(round(0.3588956879099647 * 10))

    # bet_sfc_a, bet_sfc_b, bet_sfc_c, surface_cutoff = hyper_params
    bet_sfc_a = 0.6653265485318403
    bet_sfc_b = -0.9177815683601153
    bet_sfc_c = 1.036855102957022
    surface_cutoff = int(round(4.5970976121640295 * 10))  # 2.192441090904198

    # bet_spd_a, bet_spd_b, bet_spd_c, speed_cutoff = hyper_params
    bet_spd_a = 3.3990105003184974
    bet_spd_b = -7.193927630039531
    bet_spd_c = -1.9732000152355365
    speed_cutoff = int(round(20.18577871958604 * 10))

    # bet_set_a, bet_set_b, bet_set_c, sets_cutoff = hyper_params
    bet_set_a = 5.693199788273852
    bet_set_b = -2.326855621895103
    bet_set_c = 0.2513640348838548, 
    sets_cutoff = int(round(10.683875218378896 * 10))

    # init
    reg = None
    scaler = MinMaxScaler()
    cutoff = int(len(all_data) * 0.7)
    start_date = None
    ratings = defaultdict(lambda: Rating())
    wins_losses = defaultdict(lambda: [])
    doors = defaultdict(lambda: [])
    surfaces = defaultdict(lambda: [])
    speeds = defaultdict(lambda: [100, 0])
    upsets = defaultdict(lambda: [])
    whitewashes = defaultdict(lambda: [0])
    sets = defaultdict(lambda: [])
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
            logger.info('')
        logger.info(f'{event["date"]} {event["location"]["name"]}')

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

            # wins losses
            p1_wins_losses = Counter(wins_losses[p1])
            p1_wnl_winrate = p1_wins_losses[1] / max(1, len(wins_losses[p1]))
            p2_wins_losses = Counter(wins_losses[p2])
            p2_wnl_winrate = p2_wins_losses[1] / max(1, len(wins_losses[p2]))

            # outdoors
            match_door = event['location']['outdoor']
            p1_doors = Counter(doors[p1])
            p1_doors_wins = p1_doors[match_door]
            p1_doors_losses = p1_doors[-match_door]
            p1_doors_winrate = p1_doors_wins / max(1, len(doors[p1]))
            p2_doors = Counter(doors[p2])
            p2_doors_wins = p2_doors[match_door]
            p2_doors_losses = p2_doors[-match_door]
            p2_doors_winrate = p2_doors_wins / max(1, len(doors[p2]))

            # surface
            match_surface = event['location']['surface']
            p1_surface = Counter(surfaces[p1])
            p1_surface_wins = p1_surface[match_surface]
            p1_surface_losses = p1_surface[-match_surface]
            p1_surface_winrate = p1_surface_wins / max(1, p1_surface_wins + p1_surface_losses)
            p2_surface = Counter(surfaces[p1])
            p2_surface_wins = p2_surface[match_surface]
            p2_surface_losses = p2_surface[-match_surface]
            p2_surface_winrate = p2_surface_wins / max(1, p2_surface_wins + p2_surface_losses)

            # speed
            match_speed = event['location']['speed']
            p1_speed_prs = [(abs(v), 1 if v > 0 else -1) for v in speeds[p1]]
            p1_speed_lin = linregress([v[0] for v in p1_speed_prs], [v[1] for v in p1_speed_prs])
            p2_speed_prs = [(abs(v), 1 if v > 0 else -1) for v in speeds[p2]]
            p2_speed_lin = linregress([v[0] for v in p2_speed_prs], [v[1] for v in p2_speed_prs])

            # whitewashes
            p1_whitewashes = sum(whitewashes[p1])
            p2_whitewashes = sum(whitewashes[p2])

            # upsets
            p1_upsets = sum(upsets[p1])
            p2_upsets = sum(upsets[p2])

            # evs
            odds_sum = p1_odds + p2_odds
            p1_scaled_odds = p1_odds / odds_sum
            p2_scaled_odds = p2_odds / odds_sum

            # sets
            p1_sets = Counter(sets[p1])
            p1_sets_wins = p1_sets[1]
            p1_sets_losses = p1_sets[-1]
            p1_sets_winrate = p1_sets[1] / max(1, len(sets[p1]))
            p2_sets = Counter(sets[p2])
            p2_sets_wins = p2_sets[1]
            p2_sets_losses = p2_sets[-1]
            p2_sets_winrate = p2_sets[1] / max(1, len(sets[p2]))

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
                    p1_wins_losses[1],
                    p1_wins_losses[-1],
                    p1_wnl_winrate,
                    p2_wins_losses[1],
                    p2_wins_losses[-1],
                    p2_wnl_winrate,
                    p1_doors_wins,
                    p1_doors_losses,
                    p1_doors_winrate,
                    p2_doors_wins,
                    p2_doors_losses,
                    p2_doors_winrate,
                    p1_surface_wins,
                    p1_surface_losses,
                    p1_surface_winrate,
                    p2_surface_wins,
                    p2_surface_losses,
                    p2_surface_winrate,
                    p1_upsets,
                    p2_upsets,
                    p1_whitewashes,
                    p2_whitewashes,
                    p1_speed_lin.slope,
                    p2_speed_lin.slope,
                    p1_sets_wins,
                    p1_sets_losses,
                    p1_sets_winrate,
                    p2_sets_wins,
                    p2_sets_losses,
                    p2_sets_winrate,
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
                    p2_wins_losses[1],
                    p2_wins_losses[-1],
                    p2_wnl_winrate,
                    p1_wins_losses[1],
                    p1_wins_losses[-1],
                    p1_wnl_winrate,
                    p2_doors_wins,
                    p2_doors_losses,
                    p2_doors_winrate,
                    p1_doors_wins,
                    p1_doors_losses,
                    p1_doors_winrate,
                    p2_surface_wins,
                    p2_surface_losses,
                    p2_surface_winrate,
                    p1_surface_wins,
                    p1_surface_losses,
                    p1_surface_winrate,
                    p2_upsets,
                    p1_upsets,
                    p2_whitewashes,
                    p1_whitewashes,
                    p2_speed_lin.slope,
                    p1_speed_lin.slope,
                    p2_sets_wins,
                    p2_sets_losses,
                    p2_sets_winrate,
                    p1_sets_wins,
                    p1_sets_losses,
                    p1_sets_winrate,
                ]
            ]

            #########################################
            # update here as next sections can skip ahead
            if 'score' in match:

                # update wins losses
                wins_losses[p1] = wins_losses[p1][-wnl_cutoff:] + [1]
                wins_losses[p2] = wins_losses[p2][-wnl_cutoff:] + [-1]

                # update doors
                doors[p1] = doors[p1][-doors_cutoff:] + [match_door]
                doors[p2] = doors[p2][-doors_cutoff:] + [-match_door]

                # update surface
                surfaces[p1] = surfaces[p1][-surface_cutoff:] + [match_surface]
                surfaces[p2] = surfaces[p2][-surface_cutoff:] + [-match_surface]

                # update speeds
                speeds[p1] = speeds[p1][-speed_cutoff:] + [match_speed]
                speeds[p2] = speeds[p2][-speed_cutoff:] + [-match_speed]

                # update whitewashes
                whitewash = all(g[0] > g[1] for g in match['score'])
                whitewashes[p1] = whitewashes[p1][-whitewashes_cutoff:] + [1 if whitewash else 0]
                whitewashes[p2] = whitewashes[p2][-whitewashes_cutoff:] + [-1 if whitewash else 0]

                # update upsets
                upset = win2_prob > 0.50
                upsets[p1] = upsets[p1][-upsets_cutoff:] + [1 if upset else 0]
                upsets[p2] = upsets[p2][-upsets_cutoff:] + [-1 if upset else 0]
                
                # update sets
                sets[p1] = sets[p1][-sets_cutoff:] + [1 if v[0] > v[1] else -1 for v in match['score']]
                sets[p2] = sets[p2][-sets_cutoff:] + [1 if v[1] > v[0] else -1 for v in match['score']]

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

                # wins and losses
                if p1_pred > p2_pred:
                    p_wnl = p1_wnl_winrate - p2_wnl_winrate
                else:
                    p_wnl = p2_wnl_winrate - p1_wnl_winrate
                bet_wnl_multi = np.polyval([bet_wnl_a, bet_wnl_b, bet_wnl_c], [p_wnl])[0]
                bet_wnl_multi = int(min(max(round(bet_wnl_multi), 0), 2))
                bet_multi += bet_wnl_multi
                bet_multis_cat.append(f'bet_wnl_multi-{bet_wnl_multi}')

                # doors
                if p1_pred > p2_pred:
                    p_drs = p1_doors_winrate - p2_doors_winrate
                else:
                    p_drs = p2_doors_winrate - p1_doors_winrate
                bet_drs_multi = np.polyval([bet_drs_a, bet_drs_b, bet_drs_c], [p_drs])[0]
                bet_drs_multi = int(min(max(round(bet_drs_multi), 0), 1))
                bet_multi += bet_drs_multi
                bet_multis_cat.append(f'bet_drs_multi-{bet_drs_multi}')

                # surface
                if p1_pred > p2_pred:
                    p_sfc = p1_surface_winrate - p2_surface_winrate
                else:
                    p_sfc = p2_surface_winrate - p1_surface_winrate
                bet_sfc_multi = np.polyval([bet_sfc_a, bet_sfc_b, bet_sfc_c], [p_sfc])[0]
                bet_sfc_multi = int(min(max(round(bet_sfc_multi), 0), 1))
                bet_multi += bet_sfc_multi
                bet_multis_cat.append(f'bet_sfc_multi-{bet_sfc_multi}')

                # speed
                p1_speed = p1_speed_lin.intercept + p1_speed_lin.slope * match_speed
                p2_speed = p2_speed_lin.intercept + p2_speed_lin.slope * match_speed
                if p1_pred > p2_pred:
                    p_spd = p1_speed - p2_speed
                else:
                    p_spd = p2_speed - p1_speed
                bet_spd_multi = np.polyval([bet_spd_a, bet_spd_b, bet_spd_c], [p_spd])[0]
                bet_spd_multi = int(min(max(round(bet_spd_multi), 0), 1))
                bet_multi += bet_spd_multi
                bet_multis_cat.append(f'bet_spd_multi-{bet_spd_multi}')

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

                # sets
                if p1_pred > p2_pred:
                    p_set = p1_sets_winrate - p2_sets_winrate
                else:
                    p_set = p2_sets_winrate - p1_sets_winrate
                bet_set_multi = np.polyval([bet_set_a, bet_set_b, bet_set_c], [p_set])[0]
                bet_set_multi = int(min(max(round(bet_set_multi), 0), 1))
                bet_multi += bet_set_multi
                bet_multis_cat.append(f'bet_set_multi-{bet_set_multi}')

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
                    logger.warning(f'[{predw*100:.0f}% vs {predl*100:.0f}%] Bet x{bet_multi} on {pw} to beat {pl} [{ratings[pw].mu:.0f} vs {ratings[pl].mu:.0f}]')
                    continue

                # prediction bet on
                elif 'score' not in match:
                    logger.warning(f'Pending {p1} vs {p2}')
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
                    pred_odds = p2_odds
                    if is_actual_correct:
                        pred_odds = p1_odds
                        cash += p1_odds * match['bet']
                    tab.append(round(cash, 2))
                    tab_amts.append(match['bet'])
                    actual_debug.append(f'{match["prediction"]} {match["bet"]} {pred_odds:.2f}: {cash:.2f}')

                log_balance = f'[{sum(payouts):.0f}|{payout:.0f}]'
                log_pred = f'[{p1_pred * 100:.0f}% vs {p2_pred * 100:.0f}%]'
                log_players = f'x{bet_multi} {p1} {match.get("score")} {p2}'
                log_odds = f'[{p1_odds:.2f} vs {p2_odds:.2f}]'
                log_trueskill = f'[{ratings[p1].mu:.0f}.{ratings[p1].sigma:.0f} vs {ratings[p2].mu:.0f}.{ratings[p2].sigma:.0f}]'
                logger.info(f'{log_balance} {log_pred} {log_players} {log_odds} {log_trueskill}')

    if train:
        print(f'ROI {sum(payouts) / sum(bet_amts) * 100:.1f}%  Profit ${sum(payouts):.0f}')
        return -(sum(payouts) / sum(bet_amts))
    else:
        summary(reg, accuracy, payouts, bet_amts, start_date, actual, tab, tab_amts, bet_multis, bet_multis_cat, actual_debug)


def summary(reg, accuracy, payouts, bet_amts, start_date, actual, tab, tab_amts, bet_multis, bet_multis_cat, actual_debug):
    logger.info('')
    logger.info('Tree info:')
    reg_score = reg.evals_result()
    params = reg.get_params()
    logger.info(f'Num estimators: {params["n_estimators"]}')
    logger.info(f'Learning rate: {params["learning_rate"]:.2f}')
    logger.info(f'Gamma: {params["gamma"]}')
    logger.info(f'Max depth: {params["max_depth"]}')
    logger.info(f'Scale pos weight: {params["scale_pos_weight"]:.2f}')
    logger.info(f'Accuracy: training={reg_score["validation_0"]["rmse"][-1]:.4f}')
    feature_names = [
        'win%', 'odds_scaled',
        'odds', '~odds',
        'mu', '~mu', 'sigma', '~sigma',
        'round',
        'wins', 'losses', 'winrate',
        '~wins', '~losses', '~winrate',
        'drs_wins', 'drs_losses', 'drs_wr',
        '~drs_wins', '~drs_losses', '~drs_wr',
        'sfc_wins', 'sfc_losses', 'sfc_wr',
        '~sfc_wins', '~sfc_losses', '~sfc_wr',
        'upsets', '~upsets',
        'whitewashes', '~whitewashes',
        'slope', '~slope',
    ]
    features = {k: round(v * 100) for k, v in zip(feature_names, reg.feature_importances_)}
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
        logger.info(f'ROI {sum(tab) / sum(tab_amts) * 100:.2f}%  Profit ${sum(tab):.2f}')
        days = (datetime.now() - datetime(2019, 7, 24)).days
        logger.info(f'Profit: per day: ${sum(tab) / days:.2f}  per bet ${tab.mean():.2f}')
        # sheet = -4.4
        # if abs(sum(tab) - sheet) > 0.01:
        #     for l in actual_debug:
        #         logger.warning(l)
        #     logger.error(f'debug! {sheet:.2f} != {sum(tab):.2f} diff {sum(tab) - sheet:.2f}')


def run():
    # age
    # serve strength
    # weather
    # rested
    # days since last played?
    # games and set record
    # tie-break record
    # 1st serve conversion rate
    # FIX EVs

    train = 0

    names = [
        # 'reg_lambda', 'reg_alpha',
        # 'upsets cutoff', 'whitewashes_cutoff',
        # 'pred a', 'pred b', 'pred c',
        # 'odds a', 'odds b', 'odds c',
        # 'bet_wnl_a', 'bet_wnl_b', 'bet_wnl_c', 'wnl_cutoff',
        # 'bet_drs_a', 'bet_drs_b', 'bet_drs_c', 'doors_cutoff',
        # 'estimators', 'learning_rate'
        # 'bet_sfc_a', 'bet_sfc_b', 'bet_sfc_c', 'surface_cutoff',
        # 'gamma', 'max_depth', 'min_child_weight',
        # 'bet_spd_a', 'bet_spd_b', 'bet_spd_c', 'speed_cutoff',
        # 'max_delta_step', 'subsample', 'scale_pos_weight',  # 0-0-i 0-1-1 0-1-i
        'bet_set_a', 'bet_set_b', 'bet_set_c', 'sets_cutoff',
    ]
    params = [
        0, 0, 0, 10
    ]
    bounds = [[-np.inf, -np.inf, -np.inf, 0],
              [np.inf,  np.inf,  np.inf,  np.inf]]
    assert len(params) == len(names)
    # assert len(params) == len(bounds[0])

    if train:
        es = CMAEvolutionStrategy(params, 1, {'bounds': bounds})
        while not es.stop():
            solutions = es.ask()
            try:
                fitness = [main(x, train) for x in solutions]
            except ValueError as exc:
                print(str(exc))
                continue
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
        main(params)


if __name__ == '__main__':
    run()
