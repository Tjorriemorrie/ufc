from collections import Counter, defaultdict
from datetime import datetime
from itertools import chain
from random import random

import numpy as np
from cma import CMAEvolutionStrategy, CMAOptions
from loguru import logger
from math import sqrt
from scipy.optimize import minimize
from scipy.stats import linregress
from sklearn.preprocessing import MinMaxScaler
from sortedcontainers import SortedDict
from trueskill import BETA, global_env, rate_1vs1, Rating
from xgboost import XGBRegressor

from .data import DATA
from .data_2018_09 import DATA_2018_09
from .data_2018_10 import DATA_2018_10
from .data_2019_01 import DATA_2019_01
from .data_2019_02 import DATA_2019_02
from .data_2019_03 import DATA_2019_03
from .data_2019_04 import DATA_2019_04
from .data_2019_05 import DATA_2019_05
from .data_2019_06 import DATA_2019_06
from .data_2019_07 import DATA_2019_07


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

    all_data = DATA_2018_09 + DATA_2018_10 + \
               DATA_2019_01 + DATA_2019_02 + DATA_2019_03 + DATA_2019_04 + DATA_2019_05 + DATA_2019_06 + \
               DATA_2019_07 + DATA

    # subsample, scale_pos_weight = hyper_params
    # estimators, learning_rate = hyper_params
    # max_depth, max_delta_step = hyper_params
    # subsample, learning_rate = hyper_params
    # reg_lambda, reg_alpha = hyper_params
    # estimators, gamma, min_child_weight = hyper_params
    reg_params = {
        'n_estimators': 100 if train else 1000,
        # 'learning_rate': 0.402827003661913,     # 0.3472250034933531,     # 0.38318976066403954,  # 0.2598862779876376
        # 'gamma': gamma,  # 0.14608241519136247, #0.0009620232968908353,  # 0.028048213377950385,  # 0.1480916400109764,  # 1.0931334779261526,
        # 'max_depth': int(round(3.9313821817355126)),  # 2.6177648638879334)),     # 5.504350192703311)),  # 4.59282984572512)),  # 2.605884221401324)),
        # 'min_child_weight': min_child_weight,   # 0.9643745172377024,  # 7.326173754497638,  # 1.0956345040972018,  # 0.86383038291261,
        # 'max_delta_step': 0.48953774895625707,  # 0.5421241640022615,       # 0.18550905863181466,  # 0.5808271528189928,  # 0.19995566873577586,
        # 'subsample': 0.6711062988659313,        # 1,                         # 0.838276910827906,  # 0.8792477583008574,  # 0.9922978010805564,
        # 'scale_pos_weight': 0.518193649602282,  # 0.9489016265397816,   # 0.49606238825608306,  # 0.8825017324048802,
        # 'reg_lambda': 1.0499025606723298,       # 0.34072125219503746,  # 3.7690405921484866,  # 3.2648130839099574
        # 'reg_alpha': 0.0009004937089283338,     # 0.173213152549902,    # 3.4166438754657866,  # 1.9485388354932445
        # 'colsample_bytree': 0.999790544478916,
        # 'colsample_bylevel': 0.9999562489678556,
        # 'colsample_bynode': 0.98799098337194,
    }

    # bet_pred_a, bet_pred_b = hyper_params
    # 358:651
    bet_pred_a = 3.7065474117806234     
    bet_pred_b = -0.6653074665192613
    # 11.3  # -28.73  # 1.80  # 0.6856235616721187     # 15.016285526993597
    # -1.8  # -49.87  # 4.04  # -6.498159274389197     # 1.9283642764714313

    # bet_odds_a, bet_odds_b = hyper_params
    # 624:385
    bet_odds_a = -1.1773645865149387
    bet_odds_b = 0.5945570693866703
    # bet_odds_a = -12.8459097236531    # 81.18   # 0.898754194586949      # -5.3909710759304055
    # bet_odds_b = 1.4676149747678495   # -15.86  # -1.8030234836015318    # 34.207734246228185

    # bet_wnl_a, bet_wnl_b = hyper_params
    # 1009:0
    bet_wnl_a = 0.5654514217142471
    bet_wnl_b = -1.4060917645166904
    # bet_wnl_a = 9.311648663592006     # -37.06  # -0.4929481517139193   # 6.370072182738196
    # bet_wnl_b = 10.575328756404938    # -69.59  # -0.1611129331251365   # -1.5568193398609196

    # bet_ts_a, bet_ts_b = hyper_params
    # 647:362
    bet_ts_a = -1.1148195880251917
    bet_ts_b = 0.09548175556292751
    # bet_ts_a = -7.406374954672103
    # bet_ts_b = 9.511462858950916

    # bet_spd_a, bet_spd_b = hyper_params
    # 0.8   896:127   26.5(963) -> 27.3(1025)
    bet_spd_a = -3.02823569575999
    bet_spd_b = -0.397569194062298
    # bet_spd_a = -7.938008692553112   # 10.56  # -1.0934665990307584  # 5.673874020818951
    # bet_spd_b = -3.355911663762627   # -6.84  # -1.8911000017334616  # -1.7829575567634168

    # bet_drs_a, bet_drs_b = hyper_params
    # 0.7   866:157   21.5(765) -> 22.2(825)
    bet_drs_a = -1.500885012950977
    bet_drs_b = 0.2582469626944018
    # bet_drs_a = 9.764003899248907    # 0.50   # 2.93881738898117     # -5.512606284208406
    # bet_drs_b = -3.7139970039337182  # -16.57  # -3.7681698240703465  # -1.5899553334356054

    # bet_tma_a, bet_tma_b = hyper_params
    # 0.4   762:261   24.9(821) -> 25.3(899)
    bet_tma_a = -2.578165297188432
    bet_tma_b = -4.173401422622542
    # bet_tma_a = -14.141558321834657
    # bet_tma_b = 4.8358084053299715

    # bet_tmi_a, bet_tmi_b = hyper_params
    # 0.1   696:327   25.2(813) -> 25.3(899)
    bet_tmi_a = -2.291653188662517
    bet_tmi_b = -1.7927916772609696
    # bet_tmi_a = -6.613483852552951
    # bet_tmi_b = 4.885771442053525

    # bet_sfc_a, bet_sfc_b = hyper_params
    # 0.0   1023:0   25.3(954) -> 25.3(954)
    bet_sfc_a = -1.1049253843439304
    bet_sfc_b = -2.07704694249136
    # bet_sfc_a = 16.151022486277647   # -0.33   # -1.5656463020300377   # 1.6333141987438788
    # bet_sfc_b = -1.1635041360264686  # -0.15  # -0.5308780245959728   # -1.2662003413643186

    # bet_set_a, bet_set_b, bet_gms_a, bet_gms_b = hyper_params
    bet_set_a = -50.24863019301904   # 3.60  # 9.164289878026928   # 0.782462521879341
    bet_set_b = -16.45858096616354   # 22.35  # 1.5797297743260086  # -0.7848240797607134
    bet_gms_a = -3.609425158741926   # -4.11    # -7.595500659696808  # -0.09150815566456832
    bet_gms_b = -53.424625099684064  # 0.40  # 11.477758336728444  # -6.762735375844737

    # bet_tie_a, bet_tie_b, bet_ups_a, bet_ups_b = hyper_params
    bet_tie_a = 6.567282919522458    # 29.16      # 57.50193827879752   # -2.883405239397985      # 0.4172972634262
    bet_tie_b = 0.49068927011783753  # -81.77    # 104.97860195306609  # 0.46135229384319754     # -0.09979683170330936
    bet_ups_a = 6.065608099428523    # 3.77   # 30.354441474757888  # -15.3330836557841
    bet_ups_b = -1.1235452608356777  # 8.94    # 43.594727875509385  # -4.5704529715566675

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
    sets = defaultdict(lambda: [])
    games = defaultdict(lambda: [0])
    ties = defaultdict(lambda: [])
    upsets = defaultdict(lambda: [])
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
    odds_outcomes = []

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

            # trueskill data
            p1_ts = ratings[p1].mu
            p1_sigma = ratings[p1].sigma
            p2_ts = ratings[p2].mu
            p2_sigma = ratings[p2].sigma
            p1_ts_min = p1_ts - p1_sigma * 2
            p2_ts_min = p2_ts - p2_sigma * 2
            p1_ts_max = p1_ts + p1_sigma * 2
            p2_ts_max = p2_ts + p2_sigma * 2

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

            # scaled odds
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

            # games
            p1_games = np.average(games[p1])
            p2_games = np.average(games[p2])

            # ties
            p1_ties = Counter(ties[p1])
            p1_ties_wins = p1_ties[1]
            p1_ties_losses = p1_ties[-1]
            p1_ties_winrate = p1_ties[1] / max(1, len(ties[p1]))
            p2_ties = Counter(ties[p2])
            p2_ties_wins = p2_ties[1]
            p2_ties_losses = p2_ties[-1]
            p2_ties_winrate = p2_ties[1] / max(1, len(ties[p2]))

            # upsets
            p1_upsets = Counter(upsets[p1])
            p1_upsets_wins = p1_upsets[1]
            p1_upsets_losses = p1_upsets[-1]
            p1_upsets_win_avg = p1_upsets[1] / max(1, len(upsets[p1]))
            p1_upsets_los_avg = p1_upsets[-1] / max(1, len(upsets[p1]))
            p2_upsets = Counter(upsets[p2])
            p2_upsets_wins = p2_upsets[1]
            p2_upsets_losses = p2_upsets[-1]
            p2_upsets_win_avg = p2_upsets[1] / max(1, len(upsets[p2]))
            p2_upsets_los_avg = p2_upsets[-1] / max(1, len(upsets[p2]))

            match_data = [
                [
                    win1_prob,
                    p1_scaled_odds,
                    p1_odds,
                    p2_odds,
                    p1_ts,
                    p2_ts,
                    p1_sigma,
                    p2_sigma,
                    p1_ts_min - p2_ts_min,
                    p1_ts - p2_ts,
                    p1_ts_max - p2_ts_max,
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
                    p1_surface_wins,
                    p1_surface_losses,
                    p1_surface_winrate,
                    p2_surface_wins,
                    p2_surface_losses,
                    p2_surface_winrate,
                    p1_speed_lin.slope,
                    p2_speed_lin.slope,
                    p1_sets_wins,
                    p1_sets_losses,
                    p1_sets_winrate,
                    p2_sets_wins,
                    p2_sets_losses,
                    p2_sets_winrate,
                    p1_games,
                    p2_games,
                    p1_ties_wins,
                    p1_ties_losses,
                    p1_ties_winrate,
                    p2_ties_wins,
                    p2_ties_losses,
                    p2_ties_winrate,
                    p1_upsets_wins,
                    p1_upsets_losses,
                    p1_upsets_win_avg,
                    p1_upsets_los_avg,
                    p2_upsets_wins,
                    p2_upsets_losses,
                    p2_upsets_win_avg,
                    p2_upsets_los_avg,
                ],
                [
                    win2_prob,
                    p2_scaled_odds,
                    p2_odds,
                    p1_odds,
                    p2_ts,
                    p1_ts,
                    p2_sigma,
                    p1_sigma,
                    p2_ts_min - p1_ts_min,
                    p2_ts - p1_ts,
                    p2_ts_max - p1_ts_max,
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
                    p2_surface_wins,
                    p2_surface_losses,
                    p2_surface_winrate,
                    p1_surface_wins,
                    p1_surface_losses,
                    p1_surface_winrate,
                    p2_speed_lin.slope,
                    p1_speed_lin.slope,
                    p2_sets_wins,
                    p2_sets_losses,
                    p2_sets_winrate,
                    p1_sets_wins,
                    p1_sets_losses,
                    p1_sets_winrate,
                    p2_games,
                    p1_games,
                    p2_ties_wins,
                    p2_ties_losses,
                    p2_ties_winrate,
                    p1_ties_wins,
                    p1_ties_losses,
                    p1_ties_winrate,
                    p2_upsets_wins,
                    p2_upsets_losses,
                    p2_upsets_win_avg,
                    p2_upsets_los_avg,
                    p1_upsets_wins,
                    p1_upsets_losses,
                    p1_upsets_win_avg,
                    p1_upsets_los_avg,
                ]
            ]

            #########################################
            # update here as next sections can skip ahead
            if 'score' in match:

                # update ratings
                ratings[p1], ratings[p2] = rate_1vs1(ratings[p1], ratings[p2])

                # update wins losses
                wins_losses[p1] += [1]
                wins_losses[p2] += [-1]

                # update sets
                sets[p1] += [1 if v[0] > v[1] else -1 for v in match['score']]
                sets[p2] += [1 if v[1] > v[0] else -1 for v in match['score']]

                # update games
                games[p1] += [sum(v[0] - v[1] for v in match['score'])]
                games[p2] += [sum(v[1] - v[0] for v in match['score'])]

                # update doors
                doors[p1] += [match_door]
                doors[p2] += [-match_door]

                # update surface
                surfaces[p1] += [match_surface]
                surfaces[p2] += [-match_surface]

                # update speeds
                speeds[p1] += [match_speed]
                speeds[p2] += [-match_speed]

                # update ties
                ties[p1] += [1 if v[0] == 7 else -1 for v in match['score'] if 7 in v]
                ties[p2] += [1 if v[1] == 7 else -1 for v in match['score'] if 7 in v]

                # update upsets
                upset = win2_prob > 0.50
                upsets[p1] += [1 if upset else 0]
                upsets[p2] += [-1 if upset else 0]

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
                log_pred = f'[{p1_pred * 100:.0f}% vs {p2_pred * 100:.0f}%]'
                log_odds = f'[{p1_odds:.2f} vs {p2_odds:.2f}]'
                log_trueskill = f'[{ratings[p1].mu:.0f}.{ratings[p1].sigma:.0f} vs {ratings[p2].mu:.0f}.{ratings[p2].sigma:.0f}]'

                ###############################
                # bet scaling
                bet_multi = 1

                # pred   945:0
                if p1_pred > p2_pred:
                    p_pred = p1_pred - p2_pred
                else:
                    p_pred = p2_pred - p1_pred
                bet_pred_multi = np.polyval([bet_pred_a, bet_pred_b], [p_pred])[0]
                bet_pred_multi = round(min(1, max(0, bet_pred_multi)))
                bet_multi += bet_pred_multi
                bet_multis_cat.append(f'pred:{bet_pred_multi:.0f}')

                # odds  695:247
                if p1_pred > p2_pred:
                    p_odds = 1 / p1_odds - 1 / p2_odds
                else:
                    p_odds = 1 / p2_odds - 1 / p1_odds
                bet_odds_multi = np.polyval([bet_odds_a, bet_odds_b], [p_odds])[0]
                bet_odds_multi = round(min(1, max(0, bet_odds_multi)))
                bet_multi += bet_odds_multi
                bet_multis_cat.append(f'odds:{bet_odds_multi:.0f}')

                # wins and losses  945:0
                if p1_pred > p2_pred:
                    p_wnl = p1_wnl_winrate - p2_wnl_winrate
                else:
                    p_wnl = p2_wnl_winrate - p1_wnl_winrate
                bet_wnl_multi = np.polyval([bet_wnl_a, bet_wnl_b], [p_wnl])[0]
                bet_wnl_multi = round(min(1, max(0, bet_wnl_multi)))
                bet_multi += bet_wnl_multi
                bet_multis_cat.append(f'wnl:{bet_wnl_multi:.0f}')

                # trueskill mu
                if p1_pred > p2_pred:
                    f_ts = p1_ts - p2_ts
                else:
                    f_ts = p2_ts - p1_ts
                bet_ts_multi = np.polyval([bet_ts_a, bet_ts_b], [f_ts])[0]
                bet_ts_multi = round(min(1, max(0, bet_ts_multi)))
                bet_multi += bet_ts_multi
                bet_multis_cat.append(f'ts:{bet_ts_multi:.0f}')

                # trueskill min
                if p1_pred > p2_pred:
                    f_ts_min = p1_ts_min - p2_ts_min
                else:
                    f_ts_min = p2_ts_min - p1_ts_min
                bet_tmi_multi = np.polyval([bet_tmi_a, bet_tmi_b], [f_ts_min])[0]
                bet_tmi_multi = round(min(1, max(0, bet_tmi_multi)))
                bet_multi += bet_tmi_multi
                bet_multis_cat.append(f'tmi:{bet_tmi_multi:.0f}')

                # trueskill max
                if p1_pred > p2_pred:
                    f_ts_max = p1_ts_max - p2_ts_max
                else:
                    f_ts_max = p2_ts_max - p1_ts_max
                bet_tma_multi = np.polyval([bet_tma_a, bet_tma_b], [f_ts_max])[0]
                bet_tma_multi = round(min(1, max(0, bet_tma_multi)))
                bet_multi += bet_tma_multi
                bet_multis_cat.append(f'tma:{bet_tma_multi:.0f}')

                # doors
                if p1_pred > p2_pred:
                    p_drs = p1_doors_winrate - p2_doors_winrate
                else:
                    p_drs = p2_doors_winrate - p1_doors_winrate
                bet_drs_multi = np.polyval([bet_drs_a, bet_drs_b], [p_drs])[0]
                bet_drs_multi = round(min(1, max(0, bet_drs_multi)))
                bet_multi += bet_drs_multi
                bet_multis_cat.append(f'drs:{bet_drs_multi:.0f}')

                # surface
                if p1_pred > p2_pred:
                    p_sfc = p1_surface_winrate - p2_surface_winrate
                else:
                    p_sfc = p2_surface_winrate - p1_surface_winrate
                bet_sfc_multi = np.polyval([bet_sfc_a, bet_sfc_b], [p_sfc])[0]
                bet_sfc_multi = round(min(1, max(0, bet_sfc_multi)))
                bet_multi += bet_sfc_multi
                bet_multis_cat.append(f'sfc:{bet_sfc_multi:.0f}')

                # speed
                p1_speed = p1_speed_lin.intercept + p1_speed_lin.slope * match_speed
                p2_speed = p2_speed_lin.intercept + p2_speed_lin.slope * match_speed
                if p1_pred > p2_pred:
                    p_spd = p1_speed - p2_speed
                else:
                    p_spd = p2_speed - p1_speed
                bet_spd_multi = np.polyval([bet_spd_a, bet_spd_b], [p_spd])[0]
                bet_spd_multi = round(min(1, max(0, bet_spd_multi)))
                bet_multi += bet_spd_multi
                bet_multis_cat.append(f'spd:{bet_spd_multi:.0f}')

                # sets   906:39
                if p1_pred > p2_pred:
                    p_set = p1_sets_winrate - p2_sets_winrate
                else:
                    p_set = p2_sets_winrate - p1_sets_winrate
                bet_set_multi = np.polyval([bet_set_a, bet_set_b], [p_set])[0]
                bet_set_multi = round(min(1, max(0, bet_set_multi)))
                bet_multi += bet_set_multi
                bet_multis_cat.append(f'set:{bet_set_multi:.0f}')

                # games   945:
                if p1_pred > p2_pred:
                    p_gms = p1_games - p2_games
                else:
                    p_gms = p2_games - p1_games
                bet_gms_multi = np.polyval([bet_gms_a, bet_gms_b], [p_gms])[0]
                bet_gms_multi = round(min(1, max(0, bet_gms_multi)))
                bet_multi += bet_gms_multi
                bet_multis_cat.append(f'gms:{bet_gms_multi:.0f}')

                # ties  655:14:237
                if p1_pred > p2_pred:
                    p_tie = p1_ties_winrate - p2_ties_winrate
                else:
                    p_tie = p2_ties_winrate - p2_ties_winrate
                bet_tie_multi = np.polyval([bet_tie_a, bet_tie_b], [p_tie])[0]
                bet_tie_multi = round(min(1, max(0, bet_tie_multi)))
                bet_multi += bet_tie_multi
                bet_multis_cat.append(f'tie:{bet_tie_multi:.0f}')

                # upsets   840:50:16
                if p1_pred > p2_pred:
                    p_upset = p1_upsets_win_avg - p2_upsets_win_avg
                else:
                    p_upset = p2_upsets_win_avg - p1_upsets_win_avg
                bet_ups_multi = np.polyval([bet_ups_a, bet_ups_b], [p_upset])[0]
                bet_ups_multi = round(min(1, max(0, bet_ups_multi)))
                bet_multi += bet_ups_multi
                bet_multis_cat.append(f'ups:{bet_ups_multi:.0f}')

                log_players = f'x{round(bet_multi):.0f} {p1} {match.get("score")} {p2}'
                bet_amt = round(bet_size * bet_multi)
                assert bet_amt >= 1, f'bet multi is fucked: {bet_multi}'
                bet_amts.append(bet_amt)
                bet_multis.append(int(round(bet_multi)))
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
                    logger.warning(f'[{predw*100:.0f}% vs {predl*100:.0f}%] Bet x{round(bet_multi):.0f} on {pw} to beat {pl} [{ratings[pw].mu:.0f} vs {ratings[pl].mu:.0f}]')
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
                odds_outcomes.append(1 if p1_odds < p2_odds else -1)
                payouts.append(round(payout, 2))
                accuracy = (accuracy[0] + correct, accuracy[1] + 1)
                log_balance = f'[{sum(payouts):.0f}|{payout:.0f}]'

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
                    actual_debug.append(f'${match["bet"]} {pred_odds:.2f}: {cash:.2f} {match["prediction"]} {event["location"]["name"]}:{match["round"]}')

                logger.info(f'{log_balance} {log_pred} {log_players} {log_odds} {log_trueskill}')

    if train:
        total_payouts = sum(payouts)
        roi = total_payouts / sum(bet_amts)
        res = -roi - (total_payouts / 5000)
        print(f'Score: {-res*100:.2f}  ROI {roi * 100:.1f}%  Profit ${total_payouts:.0f} {hyper_params}')
        return res
    else:
        summary(reg, accuracy, payouts, bet_amts, start_date, actual, tab, tab_amts, bet_multis, bet_multis_cat, actual_debug, odds_outcomes)


def summary(reg, accuracy, payouts, bet_amts, start_date, actual, tab, tab_amts, bet_multis, bet_multis_cat, actual_debug, odds_outcomes):
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
        'ts', '~ts', 'sigma', '~sigma',
        'ts_min_diff', 'ts_diff', 'ts_max_diff',
        'round',
        'wins', 'losses', 'winrate',
        '~wins', '~losses', '~winrate',
        'drs_wins', 'drs_losses', 'drs_wr',
        '~drs_wins', '~drs_losses',
        'sfc_wins', 'sfc_losses', 'sfc_wr',
        '~sfc_wins', '~sfc_losses', '~sfc_wr',
        'slope', '~slope',
        'sets_wins', 'sets_losses', 'sets_wr',
        '~sets_wins', '~sets_losses', '~sets_wr',
        'games', '~games',
        'ties_wins', 'ties_losses', 'ties_wr',
        '~ties_wins', '~ties_losses', '~ties_wr',
        'upsets_wins', 'upsets_losses', 'upsets_wr', 'upsets_lr',
        '~upsets_wins', '~upsets_losses', '~upsets_wr', '~upsets_lr',
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
        logger.info(f'ROI {sum(tab) / sum(tab_amts) * 100:.2f}%  Profit ${sum(tab):.2f}')
        days = (datetime.now() - datetime(2019, 7, 24)).days
        logger.info(f'Profit: per day: ${sum(tab) / days:.2f}  per bet ${tab.mean():.2f}')
        # sheet = -37.81
        # if abs(sum(tab) - sheet) > 0.01:
        #     for l in actual_debug:
        #         logger.warning(l)
        #     logger.error(f'debug! {sheet:.2f} != {sum(tab):.2f} diff {sum(tab) - sheet:.2f}')


# age
# serve strength
# weather
# rested
# days since last played?
# 1st serve conversion rate

def run():
    train = 0

    names = [
        # 'pred_a', 'pred_b',
        # 'odds_a', 'odds_b',
        # 'bet_wnl_a', 'bet_wnl_b',
        # 'bet_ts_a', 'bet_ts_b',
        'bet_spd_a', 'bet_spd_b',
        # 'bet_drs_a', 'bet_drs_b',
        # 'bet_tma_a', 'bet_tma_b',
        # 'bet_tmi_a', 'bet_tmi_b',
        # 'bet_sfc_a', 'bet_sfc_b',

        # 'bet_set_a', 'bet_set_b', 'bet_gms_a', 'bet_gms_b',
        # 'bet_tie_a', 'bet_tie_b', 'bet_ups_a', 'bet_ups_b',
    ]
    params = [
        0,
        0
    ]
    bounds = [
        [-np.inf], 
        [np.inf]
    ]
    assert len(params) == len(names)
    assert len(params) == len(bounds)

    if train:
        sigma = 1
        opts = CMAOptions()
        # opts['tolx'] = 1E-2
        opts['bounds'] = bounds
        es = CMAEvolutionStrategy(params, sigma, inopts=opts)
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

        # res = minimize(main, params, (train,), bounds=bounds)
        # print('')
        # print(f'{res.nit} iterations')
        # print(f'Success: {res.success} {res.message}')
        # print(f'Solution: {res.x}')
        # return

    else:
        main(params)


if __name__ == '__main__':
    run()
