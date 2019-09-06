from collections import Counter, defaultdict
from datetime import datetime
from itertools import chain
from random import random

import numpy as np
from cma import CMAEvolutionStrategy, CMAOptions
from loguru import logger
from math import sqrt
from scipy.optimize import minimize, optimize
from scipy.stats import linregress
from sklearn.preprocessing import MinMaxScaler
from sortedcontainers import SortedDict
from trueskill import BETA, global_env, rate_1vs1, Rating, quality_1vs1
from xgboost import XGBRegressor

from meta import get_default_metas, get_born_at, get_age_months
from .data import DATA
from .data_2018_08 import DATA_2018_08
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


def main(hyper_params, train=0):
    #logger.info('Starting main training')

    all_data = DATA_2018_08 + DATA_2018_09 + DATA_2018_10 + \
               DATA_2019_01 + DATA_2019_02 + DATA_2019_03 + DATA_2019_04 + DATA_2019_05 + DATA_2019_06 + \
               DATA_2019_07 + DATA

    bet_tie_a, bet_tie_b, bet_setl_a, bet_setl_b, bet_wnll_a, bet_wnll_b = hyper_params
    # bet_tie_a = -66.83841653329148
    # bet_tie_b = -0.6272935511522855
    # bet_setl_a = 0.04360223593863776
    # bet_setl_b = -0.9288976023906416
    # bet_wnll_a = -0.3706527497871045
    # bet_wnll_b = -6.2244458067985

    # bet_drs_a, bet_drs_b, bet_age_a, bet_age_b = hyper_params
    bet_drs_a = 1.0397837766941564
    bet_drs_b = -1.4623384804962545
    bet_age_a = 0.2378829769081588
    bet_age_b = -1.4531134826915657

    # bet_tmi_a, bet_tmi_b, bet_drsw_a, bet_drsw_b, bet_sfcr_a, bet_sfcr_b = hyper_params
    bet_tmi_a = -4.9836881760742795
    bet_tmi_b = -83.21627196734147
    bet_drsw_a = -0.33411091329941744
    bet_drsw_b = -44.72764481035757
    bet_sfcr_a = -12.151480501436353
    bet_sfcr_b = -22.64642661176115

    # bet_gms_a, bet_gms_b, bet_setr_a, bet_setr_b, bet_tiew_a, bet_tiew_b = hyper_params
    bet_gms_a = -3.8288091653165734
    bet_gms_b = -23.664831924786334
    bet_setr_a = -18.2224169871176
    bet_setr_b = -14.18205195710263
    bet_tiew_a = 0.03636999084159087
    bet_tiew_b = -13.548412214852432

    # bet_sfcw_a, bet_sfcw_b, bet_tiel_a, bet_tiel_b, bet_upsw_a, bet_upsw_b = hyper_params
    bet_sfcw_a = 0.0633931433258635
    bet_sfcw_b = -4.407522326360301
    bet_tiel_a = -0.10102810507592701
    bet_tiel_b = -5.742082050005401
    bet_upsw_a = 0.7524006328776914
    bet_upsw_b = -7.252910131937457

    # bet_rnd_a, bet_rnd_b, bet_drsl_a, bet_drsl_b, bet_setw_a, bet_setw_b = hyper_params
    bet_rnd_a = 1.134189196854935
    bet_rnd_b = -1.8500249233845811
    bet_drsl_a = 0.06232326808128575
    bet_drsl_b = -3.73083515586576
    bet_setw_a = 0.0025952108844216094
    bet_setw_b = -5.1313314203242335

    # bet_tma_a, bet_tma_b, bet_tsq_a, bet_tsq_b, bet_upsl_a, bet_upsl_b = hyper_params
    bet_tma_a = -0.12292354147404629
    bet_tma_b = -7.113081815527231
    bet_tsq_a = 3.191207414510027
    bet_tsq_b = -2.3510382290268295
    bet_upsl_a = 0.10758415760091548
    bet_upsl_b = -2.622094121730521

    # bet_ts_a, bet_ts_b, bet_wnlr_a, bet_wnlr_b = hyper_params
    bet_ts_a = 0.0031541287913705307
    bet_ts_b = -3.5492258522971833
    bet_wnlr_a = 1.4026834651266886
    bet_wnlr_b = -2.3517493344027858

    # bet_odds_a, bet_odds_b, bet_wnlw_a, bet_wnlw_b, = hyper_params
    bet_odds_a = 0.44881449558624775
    bet_odds_b = -0.39275703724074107
    bet_wnlw_a = 0.09036263843928133
    bet_wnlw_b = -4.730437486783929

    # bet_spd_a, bet_spd_b, bet_ups_a, bet_ups_b = hyper_params
    bet_spd_a = -30.48193843233892
    bet_spd_b = -33.47440361099498
    bet_ups_a = -57.8203284494355
    bet_ups_b = -20.423068608834054

    # init
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
    payouts = []
    bet_amts = []
    accuracy = []
    trueskill = []
    matches = 0
    tab = []
    tab_amts = []
    actual = (0, 0)
    actual_debug = []
    bet_multis = []
    bet_multis_cat = []

    # loop through scenes
    for i, event in enumerate(all_data):
        bet_size = 1
        if not start_date:
            start_date = datetime.strptime(event['date'], '%Y-%m-%d')
        #logger.info('')
        #logger.info(f'{event["date"]} {event["location"]["name"]}')

        for match in event['matches']:
            # skip if no odds:
            if 'odds' not in match:
                continue
            matches += 1

            p1, p2 = match['players']

            # odds data
            p1_odds = match['odds'][p1]
            p2_odds = match['odds'][p2]
            if not -40 < p1_odds < 40 or not -40 < p2_odds < 40:
                raise ValueError(f'surely these odds are wrong? {p1_odds} {p2_odds}')

            # trueskill data
            p1_ts = ratings[p1].mu
            p2_ts = ratings[p2].mu
            p1_sigma = ratings[p1].sigma
            p2_sigma = ratings[p2].sigma

            # trueskill min data
            p1_ts_min = p1_ts - p1_sigma * 2
            p2_ts_min = p2_ts - p2_sigma * 2

            # trueskill max data
            p1_ts_max = p1_ts + p1_sigma * 2
            p2_ts_max = p2_ts + p2_sigma * 2

            # trueskill match quality
            ts_quality = quality_1vs1(ratings[p1], ratings[p2])

            # wins losses
            p1_wins_losses = Counter(wins_losses[p1])
            p1_wins = p1_wins_losses[1]
            p1_losses = p1_wins_losses[-1]
            p1_wnl_winrate = p1_wins / max(1, len(wins_losses[p1]))
            p2_wins_losses = Counter(wins_losses[p2])
            p2_wins = p2_wins_losses[1]
            p2_losses = p2_wins_losses[-1]
            p2_wnl_winrate = p2_wins / max(1, len(wins_losses[p2]))

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
            p2_surface = Counter(surfaces[p2])
            p2_surface_wins = p2_surface[match_surface]
            p2_surface_losses = p2_surface[-match_surface]
            p2_surface_winrate = p2_surface_wins / max(1, p2_surface_wins + p2_surface_losses)

            # speed
            match_speed = event['location']['speed']
            p1_speed_prs = [(abs(v), 1 if v > 0 else -1) for v in speeds[p1]]
            p1_speed_lin = linregress([v[0] for v in p1_speed_prs], [v[1] for v in p1_speed_prs])
            p2_speed_prs = [(abs(v), 1 if v > 0 else -1) for v in speeds[p2]]
            p2_speed_lin = linregress([v[0] for v in p2_speed_prs], [v[1] for v in p2_speed_prs])

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
            p1_gms_avg = np.average(games[p1])
            p2_gms_avg = np.average(games[p2])

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
            p2_upsets = Counter(upsets[p2])
            p2_upsets_wins = p2_upsets[1]
            p2_upsets_losses = p2_upsets[-1]
            p2_upsets_win_avg = p2_upsets[1] / max(1, len(upsets[p2]))

            # age
            p1_age = get_age_months(p1)
            p2_age = get_age_months(p2)

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
                upset = p2_odds < p1_odds
                upsets[p1] += [1 if upset else 0]
                upsets[p2] += [-1 if upset else 0]

            log_odds = f'[{p1_odds:.2f} vs {p2_odds:.2f}]'
            log_trueskill = f'[{p1_ts:.0f}.{p1_sigma:.0f} vs {p2_ts:.0f}.{p2_sigma:.0f}]'

            ###############################
            # bet scaling
            bet_multi = 1

            # odds
            if p1_odds < p2_odds:
                p_odds = 1 / p1_odds - 1 / p2_odds
            else:
                p_odds = 1 / p2_odds - 1 / p1_odds
            bet_odds_multi = np.polyval([bet_odds_a, bet_odds_b], [p_odds])[0]
            bet_odds_multi = min(2, max(-.03, bet_odds_multi))
            bet_multi += bet_odds_multi
            bet_multis_cat.append(f'odds:{round(abs(bet_odds_multi)):.0f}')

            # trueskill mu
            if p1_odds < p2_odds:
                f_ts = p1_ts - p2_ts
            else:
                f_ts = p2_ts - p1_ts
            bet_ts_multi = np.polyval([bet_ts_a, bet_ts_b], [f_ts])[0]
            bet_ts_multi = min(2, max(-.03, bet_ts_multi))
            bet_multi += bet_ts_multi
            bet_multis_cat.append(f'ts:{round(abs(bet_ts_multi)):.0f}')

            # trueskill min
            if p1_odds < p2_odds:
                f_ts_min = p1_ts_min - p2_ts_min
            else:
                f_ts_min = p2_ts_min - p1_ts_min
            bet_tmi_multi = np.polyval([bet_tmi_a, bet_tmi_b], [f_ts_min])[0]
            bet_tmi_multi = min(2, max(-.03, bet_tmi_multi))
            bet_multi += bet_tmi_multi
            bet_multis_cat.append(f'tmi:{round(abs(bet_tmi_multi)):.0f}')

            # trueskill max
            if p1_odds < p2_odds:
                f_ts_max = p1_ts_max - p2_ts_max
            else:
                f_ts_max = p2_ts_max - p1_ts_max
            bet_tma_multi = np.polyval([bet_tma_a, bet_tma_b], [f_ts_max])[0]
            bet_tma_multi = min(2, max(-.03, bet_tma_multi))
            bet_multi += bet_tma_multi
            bet_multis_cat.append(f'tma:{round(abs(bet_tma_multi)):.0f}')

            # trueskill match quality
            bet_tsq_multi = np.polyval([bet_tsq_a, bet_tsq_b], [ts_quality])[0]
            bet_tsq_multi = min(2, max(-.03, bet_tsq_multi))
            bet_multi += bet_tsq_multi
            bet_multis_cat.append(f'tsq:{round(abs(bet_tsq_multi)):.0f}')

            # wins and losses wins
            if p1_odds < p2_odds:
                p_wnlw = p1_wins - p2_wins
            else:
                p_wnlw = p2_wins - p1_wins
            bet_wnlw_multi = np.polyval([bet_wnlw_a, bet_wnlw_b], [p_wnlw])[0]
            bet_wnlw_multi = min(2, max(-.03, bet_wnlw_multi))
            bet_multi += bet_wnlw_multi
            bet_multis_cat.append(f'wnlw:{round(abs(bet_wnlw_multi)):.0f}')

            # wins and losses lost
            if p1_odds < p2_odds:
                p_wnll = p2_losses - p1_losses
            else:
                p_wnll = p1_losses - p2_losses
            bet_wnll_multi = np.polyval([bet_wnll_a, bet_wnll_b], [p_wnll])[0]
            bet_wnll_multi = min(3, max(-.04, bet_wnll_multi))
            bet_multi += bet_wnll_multi
            bet_multis_cat.append(f'wnll:{round(abs(bet_wnll_multi)):.0f}')

            # wins and losses winrate
            if p1_odds < p2_odds:
                p_wnlr = p1_wnl_winrate - p2_wnl_winrate
            else:
                p_wnlr = p2_wnl_winrate - p1_wnl_winrate
            bet_wnlr_multi = np.polyval([bet_wnlr_a, bet_wnlr_b], [p_wnlr])[0]
            bet_wnlr_multi = min(2, max(-.03, bet_wnlr_multi))
            bet_multi += bet_wnlr_multi
            bet_multis_cat.append(f'wnlr:{round(abs(bet_wnlr_multi)):.0f}')

            # round
            bet_rnd_multi = np.polyval([bet_rnd_a, bet_rnd_b], [1 / match['round']])[0]
            bet_rnd_multi = min(2, max(-.03, bet_rnd_multi))
            bet_multi += bet_rnd_multi
            bet_multis_cat.append(f'rnd:{round(abs(bet_rnd_multi)):.0f}')
            
            # doors wins
            if p1_odds < p2_odds:
                p_drsw = p1_doors_wins - p2_doors_wins
            else:
                p_drsw = p2_doors_wins - p1_doors_wins
            bet_drsw_multi = np.polyval([bet_drsw_a, bet_drsw_b], [p_drsw])[0]
            bet_drsw_multi = min(2, max(-.03, bet_drsw_multi))
            bet_multi += bet_drsw_multi
            bet_multis_cat.append(f'drsw:{round(abs(bet_drsw_multi)):.0f}')

            # doors losses
            if p1_odds < p2_odds:
                p_drsl = p2_doors_losses - p1_doors_losses
            else:
                p_drsl = p1_doors_losses - p2_doors_losses
            bet_drsl_multi = np.polyval([bet_drsl_a, bet_drsl_b], [p_drsl])[0]
            bet_drsl_multi = min(2, max(-.03, bet_drsl_multi))
            bet_multi += bet_drsl_multi
            bet_multis_cat.append(f'drsl:{round(abs(bet_drsl_multi)):.0f}')

            # doors winrate
            if p1_odds < p2_odds:
                p_drs = p1_doors_winrate - p2_doors_winrate
            else:
                p_drs = p2_doors_winrate - p1_doors_winrate
            bet_drs_multi = np.polyval([bet_drs_a, bet_drs_b], [p_drs])[0]
            bet_drs_multi = min(2, max(-.03, bet_drs_multi))
            bet_multi += bet_drs_multi
            bet_multis_cat.append(f'drs:{round(abs(bet_drs_multi)):.0f}')

            # surface wins
            if p1_odds < p2_odds:
                p_sfcw = p1_surface_wins - p2_surface_wins
            else:
                p_sfcw = p2_surface_wins - p1_surface_wins
            bet_sfcw_multi = np.polyval([bet_sfcw_a, bet_sfcw_b], [p_sfcw])[0]
            bet_sfcw_multi = min(2, max(-.03, bet_sfcw_multi))
            bet_multi += bet_sfcw_multi
            bet_multis_cat.append(f'sfcw:{round(abs(bet_sfcw_multi)):.0f}')

            # surface winrate
            if p1_odds < p2_odds:
                p_sfcr = p1_surface_winrate - p2_surface_winrate
            else:
                p_sfcr = p2_surface_winrate - p1_surface_winrate
            bet_sfcr_multi = np.polyval([bet_sfcr_a, bet_sfcr_b], [p_sfcr])[0]
            bet_sfcr_multi = min(2, max(-.03, bet_sfcr_multi))
            bet_multi += bet_sfcr_multi
            bet_multis_cat.append(f'sfcr:{round(abs(bet_sfcr_multi)):.0f}')

            # speed
            p1_speed = p1_speed_lin.intercept + p1_speed_lin.slope * match_speed
            p2_speed = p2_speed_lin.intercept + p2_speed_lin.slope * match_speed
            if p1_odds < p2_odds:
                p_spd = p1_speed - p2_speed
            else:
                p_spd = p2_speed - p1_speed
            bet_spd_multi = np.polyval([bet_spd_a, bet_spd_b], [p_spd])[0]
            bet_spd_multi = min(1, max(-.032, bet_spd_multi))
            bet_multi += bet_spd_multi
            bet_multis_cat.append(f'spd:{round(abs(bet_spd_multi)):.0f}')

            # sets wins
            if p1_odds < p2_odds:
                p_setw = p1_sets_wins - p2_sets_wins
            else:
                p_setw = p2_sets_wins - p1_sets_wins
            bet_setw_multi = np.polyval([bet_setw_a, bet_setw_b], [p_setw])[0]
            bet_setw_multi = min(2, max(-.03, bet_setw_multi))
            bet_multi += bet_setw_multi
            bet_multis_cat.append(f'setw:{round(abs(bet_setw_multi)):.0f}')

            # sets losses
            if p1_odds < p2_odds:
                p_setl = p2_sets_losses - p1_sets_losses
            else:
                p_setl = p1_sets_losses - p2_sets_losses
            bet_setl_multi = np.polyval([bet_setl_a, bet_setl_b], [p_setl])[0]
            bet_setl_multi = min(3, max(-.04, bet_setl_multi))
            bet_multi += bet_setl_multi
            bet_multis_cat.append(f'setl:{round(abs(bet_setl_multi)):.0f}')

            # sets winrate
            if p1_odds < p2_odds:
                p_setr = p1_sets_winrate - p2_sets_winrate
            else:
                p_setr = p2_sets_winrate - p1_sets_winrate
            bet_setr_multi = np.polyval([bet_setr_a, bet_setr_b], [p_setr])[0]
            bet_setr_multi = min(2, max(-.03, bet_setr_multi))
            bet_multi += bet_setr_multi
            bet_multis_cat.append(f'setr:{round(abs(bet_setr_multi)):.0f}')

            # games
            if p1_odds < p2_odds:
                p_gms = p1_gms_avg - p2_gms_avg
            else:
                p_gms = p2_gms_avg - p1_gms_avg
            bet_gms_multi = np.polyval([bet_gms_a, bet_gms_b], [p_gms])[0]
            bet_gms_multi = min(2, max(-.03, bet_gms_multi))
            bet_multi += bet_gms_multi
            bet_multis_cat.append(f'gms:{round(abs(bet_gms_multi)):.0f}')

            # ties wins
            if p1_odds < p2_odds:
                p_tiew = p1_ties_wins - p2_ties_wins
            else:
                p_tiew = p2_ties_wins - p1_ties_wins
            bet_tiew_multi = np.polyval([bet_tiew_a, bet_tiew_b], [p_tiew])[0]
            bet_tiew_multi = min(2, max(-.03, bet_tiew_multi))
            bet_multi += bet_tiew_multi
            bet_multis_cat.append(f'tiew:{round(abs(bet_tiew_multi)):.0f}')

            # ties losses
            if p1_odds < p2_odds:
                p_tiel = p2_ties_losses - p1_ties_losses
            else:
                p_tiel = p1_ties_losses - p2_ties_losses
            bet_tiel_multi = np.polyval([bet_tiel_a, bet_tiel_b], [p_tiel])[0]
            bet_tiel_multi = min(2, max(-.03, bet_tiel_multi))
            bet_multi += bet_tiel_multi
            bet_multis_cat.append(f'tiel:{round(abs(bet_tiel_multi)):.0f}')

            # ties winrate
            if p1_odds < p2_odds:
                p_tie = p1_ties_winrate - p2_ties_winrate
            else:
                p_tie = p2_ties_winrate - p2_ties_winrate
            bet_tie_multi = np.polyval([bet_tie_a, bet_tie_b], [p_tie])[0]
            bet_tie_multi = min(3, max(-.04, bet_tie_multi))
            bet_multi += bet_tie_multi
            bet_multis_cat.append(f'tie:{round(abs(bet_tie_multi)):.0f}')

            # upsets wins
            if p1_odds < p2_odds:
                p_upsw = p1_upsets_wins - p2_upsets_wins
            else:
                p_upsw = p2_upsets_wins - p1_upsets_wins
            bet_upsw_multi = np.polyval([bet_upsw_a, bet_upsw_b], [p_upsw])[0]
            bet_upsw_multi = min(2, max(-.03, bet_upsw_multi))
            bet_multi += bet_upsw_multi
            bet_multis_cat.append(f'upsw:{round(abs(bet_upsw_multi)):.0f}')

            # upsets losess
            if p1_odds < p2_odds:
                p_upsl = p2_upsets_losses - p1_upsets_losses
            else:
                p_upsl = p1_upsets_losses - p2_upsets_losses
            bet_upsl_multi = np.polyval([bet_upsl_a, bet_upsl_b], [p_upsl])[0]
            bet_upsl_multi = min(2, max(-.03, bet_upsl_multi))
            bet_multi += bet_upsl_multi
            bet_multis_cat.append(f'upsl:{round(abs(bet_upsl_multi)):.0f}')

            # upsets winrate
            if p1_odds < p2_odds:
                p_upset = p1_upsets_win_avg - p2_upsets_win_avg
            else:
                p_upset = p2_upsets_win_avg - p1_upsets_win_avg
            bet_ups_multi = np.polyval([bet_ups_a, bet_ups_b], [p_upset])[0]
            bet_ups_multi = min(1, max(-.03, bet_ups_multi))
            bet_multi += bet_ups_multi
            bet_multis_cat.append(f'ups:{round(abs(bet_ups_multi)):.0f}')

            # age
            if p1_odds < p2_odds:
                p_age = p1_age - p2_age
            else:
                p_age = p2_age - p1_age
            bet_age_multi = np.polyval([bet_age_a, bet_age_b], [p_age])[0]
            bet_age_multi = min(2, max(-.03, bet_age_multi))
            bet_multi += bet_age_multi
            bet_multis_cat.append(f'age:{round(abs(bet_age_multi)):.0f}')

            log_players = f'x{round(bet_multi):.0f} {p1} {match.get("score")} {p2}'
            bet_amt = round(bet_size * bet_multi)
            ###############################

            # make prediction
            if 'prediction' in match and match['prediction'] is None:
                # no positive bet
                if bet_amt < 1:
                    #logger.warning(f'No bet!  {p1} vs {p2} {log_odds} {log_trueskill}')
                    continue
                if p1_odds < p2_odds:
                    w_odds = p1_odds
                    w = p1
                    l_odds = p2_odds
                    l = p2
                else:
                    w_odds = p2_odds
                    w = p2
                    l_odds = p1_odds
                    l = p1
                #logger.warning(f'[{w_odds:.2f} vs {l_odds:.2f}] Bet x{round(bet_multi):.0f} on {w} to beat {l} [{ratings[w].mu:.0f} vs {ratings[l].mu:.0f}]')
                continue

            # prediction bet on
            if 'score' not in match:
                #logger.warning(f'Pending {p1} vs {p2}')
                continue

            if bet_amt < 1:
                #logger.info(f'No bet!  {log_players} {log_odds} {log_trueskill}')
                continue

            # testing outcome
            payout = -bet_amt
            if p1_odds < p2_odds:
                payout += p1_odds * bet_amt

            accuracy.append(1 if p1_odds < p2_odds else -1)
            trueskill.append(1 if p1_ts > p2_ts else -1)
            bet_amts.append(bet_amt)
            bet_multis.append(int(round(bet_multi)))
            payouts.append(round(payout, 2))
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

            #logger.info(f'{log_balance} {log_players} {log_odds} {log_trueskill}')

    if train:
        total_payouts = sum(payouts)
        roi = total_payouts / sum(bet_amts)
        res = -roi - (total_payouts / 10000)
        print(f'Score: {-res*100:.2f}  ROI {roi * 100:.1f}%  Profit ${total_payouts:.0f} {hyper_params}')
        return res
    else:
        summary(accuracy, payouts, bet_amts, start_date, actual, tab, tab_amts, bet_multis, bet_multis_cat, actual_debug, matches, trueskill)


def summary(accuracy, payouts, bet_amts, start_date, actual, tab, tab_amts, bet_multis, bet_multis_cat, actual_debug, matches, trueskill):
    if accuracy:
        payouts = np.array(payouts)
        #logger.info('')
        #logger.info('Testing:')
        accuracy_wins = sum([t for t in accuracy if t > 0])
        trueskill_wins = sum([t for t in trueskill if t > 0])
        #logger.info(f'Accuracy {accuracy_wins}/{len(accuracy)} = {accuracy_wins/len(accuracy)*100:.1f}% [ts:{trueskill_wins/max(1, len(trueskill))*100:.0f}%]   Matches: {len(accuracy)/max(1, matches)*100:.1f}%')
        #logger.info(f'ROI {sum(payouts) / sum(bet_amts) * 100:.1f}%  Profit ${sum(payouts):.0f}')
        days = (datetime.now() - start_date).days
        #logger.info(f'Profit: per day: ${sum(payouts) / days:.2f}  per bet ${payouts.mean():.2f}')
        #logger.info(f'Common multis: {Counter(bet_multis).most_common(4)}')
        #logger.info(f'cat multis: {Counter(bet_multis_cat).most_common()}')

    if actual[1]:
        tab = np.array(tab)
        #logger.info('')
        #logger.info('Actual:')
        #logger.info(f'Accuracy {actual[0]}/{actual[1]} = {actual[0]/actual[1] * 100:.1f}%')
        #logger.info(f'ROI {sum(tab) / sum(tab_amts) * 100:.2f}%  Profit ${sum(tab):.2f}')
        days = (datetime.now() - datetime(2019, 7, 24)).days
        #logger.info(f'Profit: per day: ${sum(tab) / days:.2f}  per bet ${tab.mean():.2f}')
        # sheet = -74.59
        # if abs(sum(tab) - sheet) > 0.01:
        #     for l in actual_debug:
        #         #logger.warning(l)
        #     #logger.error(f'debug! {sheet:.2f} != {sum(tab):.2f} diff {sum(tab) - sheet:.2f}')


# serve strength
# weather
# rested
# days since last played?
# 1st serve conversion rate

def run():
    train = 1
    
    names = [
        # 76    69     14.7     616
        # 76    68      11.8    399
        # 76    68      11.8    407
        # 81.9  31.8    -       220
        # 74.1  73.1    8.8     497
        # 74.0  73.3    9.1     730
        # 73.9  73.3    9.2     718
        # 75.1  69.4    12.6    1009
        # 75.3  69.2    11.5    801
        # 75.1  69.5    11.5    808
        # 72.3  77.5    8.9     843
        # 81.5  55.3    21.4    957
        # 83.0  52.5    23.5    943
        # !! significant profit drop, changing max limit to 2

        # 90.5  14.7    23.9    210
        # 'bet_spd_a', 'bet_spd_b',  # 3655:2
        # 'bet_ups_a', 'bet_ups_b',  # 3432:225

        # !! min limited to -0.10 (giving 45% matches) [done all changed immediately]

        # 77.7  44.7    15.4    356
        # 'odds_a', 'odds_b',  # 3657:
        # 'bet_wnlw_a', 'bet_wnlw_b',  # 3657:

        # 77.9  44.8    15.6    365
        # 'bet_ts_a', 'bet_ts_b',  # 3657::
        # 'bet_wnlr_a', 'bet_wnlr_b',  # 3657::

        # 76.9  46.2    15.7    388
        # 'bet_tma_a', 'bet_tma_b',  # 3657::
        # 'bet_tsq_a', 'bet_tsq_b',  # 3172:485:
        # 'bet_upsl_a', 'bet_upsl_b',  # 3657::

        # 69.0  66.2    7.0     266
        # 'bet_rnd_a', 'bet_rnd_b',  # 3659::
        # 'bet_drsl_a', 'bet_drsl_b',  # 3659::
        # 'bet_setw_a', 'bet_setw_b',  # 3659::

        # !! min limited to -0.05 (giving 66% matches) [done all changed immediately]

        # 71.1  58.9    11.3    327
        # 'bet_sfcw_a', 'bet_sfcw_b',  # 3659:
        # 'bet_tiel_a', 'bet_tiel_b',  # 3659:
        # 'bet_upsw_a', 'bet_upsw_b',  # 3624:10:25

        # 71.4  59.6    11.5    351
        # 'bet_gms_a', 'bet_gms_b',  # 3730:1:3
        # 'bet_setr_a', 'bet_setr_b',  # 3722:2:10
        # 'bet_tiew_a', 'bet_tiew_b',  # 3734::

        # !! min limited to -0.03 (giving 51% matches) [done all changed immediately]

        # 73.0  51.4    13.9    356
        # 'bet_tmi_a', 'bet_tmi_b',  # 3716:3:15
        # 'bet_drsw_a', 'bet_drsw_b',  # 3734
        # 'bet_sfcr_a', 'bet_sfcr_b',  # 3734

        # 70.2  74.0    2.7     161
        # 'bet_age_a', 'bet_age_b',  # 3655:
        # 'bet_drs_a', 'bet_drs_b',  # 3657:

        'bet_tie_a', 'bet_tie_b',  # 2777:880
        'bet_setl_a', 'bet_setl_b',  # 3617:38:2
        'bet_wnll_a', 'bet_wnll_b',  # 3610:17:30
    ]
    params = [0, 0, 0, 0, 0, 0]
    bounds = [
        [-np.inf],
        [np.inf]
    ]
    assert len(params) == len(names)
    # assert len(params) == len(bounds)

    if train:
        sigma = 1
        opts = CMAOptions()
        opts['tolx'] = 0.6
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

        # pmin = -20
        # pmax = 20
        # step = (pmax - pmin) / 10
        # rranges = [
        #     slice(pmin, pmax, step),
        #     slice(pmin, pmax, step),
        # ]
        # res = optimize.brute(main, rranges, (train,), finish=None)
        # print(res)
        # return

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
