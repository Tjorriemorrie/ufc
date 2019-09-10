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

    bet_gms_a, bet_gms_b, bet_age_a, bet_age_b, bet_tmi_a, bet_tmi_b = hyper_params
    # bet_gms_a = -0.10804200106369631
    # bet_gms_b = -0.7957416708458603
    # bet_age_a = -0.016270655187989494
    # bet_age_b = -4.6375754627339285
    # bet_tmi_a = -23.27888343256329
    # bet_tmi_b = -390.3108751667699

    # bet_wnlw_a, bet_wnlw_b, bet_odds_a, bet_odds_b, bet_spd_a, bet_spd_b = hyper_params
    bet_wnlw_a = 0.09123251259436502
    bet_wnlw_b = -13.558089455589954
    bet_odds_a = 0.09318635268765679
    bet_odds_b = -0.05190902706463822
    bet_spd_a = -6.407271332720497
    bet_spd_b = -6.2377755218971425

    # bet_sfcr_a, bet_sfcr_b, bet_wnlr_a, bet_wnlr_b, bet_tiew_a, bet_tiew_b = hyper_params
    bet_sfcr_a = 0.11306265353913632
    bet_sfcr_b = 0.19119392985930203
    bet_wnlr_a = 0.20401809519496003
    bet_wnlr_b = 0.248885614250008
    bet_tiew_a = 0.019032029441890898
    bet_tiew_b = 0.20984338993698262

    # bet_upsr_a, bet_upsr_b, bet_rnd_a, bet_rnd_b, bet_ts_a, bet_ts_b = hyper_params
    bet_upsr_a = 0.6398814296730124
    bet_upsr_b = -2.5826759528151584
    bet_rnd_a = 0.08967312258194254
    bet_rnd_b = -2.327914375469589
    bet_ts_a = -0.30052916768808335
    bet_ts_b = -4.579610627865042

    # bet_tsq_a, bet_tsq_b, bet_setl_a, bet_setl_b, bet_upsw_a, bet_upsw_b = hyper_params
    bet_tsq_a = -4.259707005037631
    bet_tsq_b = -9.776706755704124
    bet_setl_a = -0.030208919160333345
    bet_setl_b = -7.8106766825327565
    bet_upsw_a = 0.03718734235381525
    bet_upsw_b = -4.369071480440376

    # bet_drsw_a, bet_drsw_b, bet_setw_a, bet_setw_b, bet_tier_a, bet_tier_b = hyper_params
    bet_drsw_a = 93.20086103163615
    bet_drsw_b = -4542.981562310063
    bet_setw_a = -0.9282518064658616
    bet_setw_b = -150.29835086176513
    bet_tier_a = 1794.3318767613787
    bet_tier_b = -5.198936104804425

    # bet_sfcw_a, bet_sfcw_b, bet_wnll_a, bet_wnll_b, bet_drs_a, bet_drs_b = hyper_params
    bet_sfcw_a = 0.013578573815945523
    bet_sfcw_b = -4.051435657177985
    bet_wnll_a = -0.18163963085294682
    bet_wnll_b = -3.8603065928427815
    bet_drs_a = -4.143602367496206
    bet_drs_b = -3.871644397011016

    # bet_tiel_a, bet_tiel_b, bet_upsl_a, bet_upsl_b = hyper_params
    bet_tiel_a = 0.0679376588285391
    bet_tiel_b = -0.6581047239883145
    bet_upsl_a = 0.25005020691694646
    bet_upsl_b = -0.5140010044130777

    # bet_tma_a, bet_tma_b, bet_drsl_a, bet_drsl_b = hyper_params
    bet_tma_a = -0.10555036017107794
    bet_tma_b = -1.1714235100518284
    bet_drsl_a = 0.06051960302189707
    bet_drsl_b = -0.642515386959391

    # bet_setr_a, bet_setr_b = hyper_params
    bet_setr_a = 2.51573145418509
    bet_setr_b = -3.6066735570897173

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
            bet_multi = 0
            bet_max_limit = 3
            bet_min_limit = 0

            # odds
            if p1_odds < p2_odds:
                p_odds = 1 / p1_odds - 1 / p2_odds
            else:
                p_odds = 1 / p2_odds - 1 / p1_odds
            bet_odds_multi = np.polyval([bet_odds_a, bet_odds_b], [p_odds])[0]
            bet_odds_multi = min(bet_max_limit, max(bet_min_limit, bet_odds_multi))
            bet_odds_multi = int(round(bet_odds_multi))
            if bet_odds_multi > 0:
                bet_multi += bet_odds_multi
                bet_multis_cat.append(f'odds:{bet_odds_multi}')

            # trueskill mu
            if p1_odds < p2_odds:
                f_ts = p1_ts - p2_ts
            else:
                f_ts = p2_ts - p1_ts
            bet_ts_multi = np.polyval([bet_ts_a, bet_ts_b], [f_ts])[0]
            bet_ts_multi = min(bet_max_limit, max(bet_min_limit, bet_ts_multi))
            bet_multi += int(round(bet_ts_multi))
            if round(bet_ts_multi) > 0:
                bet_multis_cat.append(f'ts:{round(abs(bet_ts_multi)):.0f}')

            # trueskill min
            if p1_odds < p2_odds:
                f_ts_min = p1_ts_min - p2_ts_min
            else:
                f_ts_min = p2_ts_min - p1_ts_min
            bet_tmi_multi = np.polyval([bet_tmi_a, bet_tmi_b], [f_ts_min])[0]
            bet_tmi_multi = min(bet_max_limit, max(bet_min_limit, bet_tmi_multi))
            bet_tmi_multi = int(round(bet_tmi_multi))
            if bet_tmi_multi > 0:
                bet_multi += bet_tmi_multi
                bet_multis_cat.append(f'tmi:{bet_tmi_multi}')

            # trueskill max
            if p1_odds < p2_odds:
                f_ts_max = p1_ts_max - p2_ts_max
            else:
                f_ts_max = p2_ts_max - p1_ts_max
            bet_tma_multi = np.polyval([bet_tma_a, bet_tma_b], [f_ts_max])[0]
            bet_tma_multi = min(bet_max_limit, max(bet_min_limit, bet_tma_multi))
            bet_multi += int(round(bet_tma_multi))
            if round(bet_tma_multi) > 0:
                bet_multis_cat.append(f'tma:{round(abs(bet_tma_multi)):.0f}')

            # trueskill match quality
            bet_tsq_multi = np.polyval([bet_tsq_a, bet_tsq_b], [ts_quality])[0]
            bet_tsq_multi = min(bet_max_limit, max(bet_min_limit, bet_tsq_multi))
            bet_multi += int(round(bet_tsq_multi))
            if round(bet_tsq_multi) > 0:
                bet_multis_cat.append(f'tsq:{round(abs(bet_tsq_multi)):.0f}')

            # wins and losses wins
            if p1_odds < p2_odds:
                p_wnlw = p1_wins - p2_wins
            else:
                p_wnlw = p2_wins - p1_wins
            bet_wnlw_multi = np.polyval([bet_wnlw_a, bet_wnlw_b], [p_wnlw])[0]
            bet_wnlw_multi = min(bet_max_limit, max(bet_min_limit, bet_wnlw_multi))
            bet_wnlw_multi = int(round(bet_wnlw_multi))
            if bet_wnlw_multi > 0:
                bet_multi += bet_wnlw_multi
                bet_multis_cat.append(f'wnlw:{bet_wnlw_multi}')

            # wins and losses lost
            if p1_odds < p2_odds:
                p_wnll = p2_losses - p1_losses
            else:
                p_wnll = p1_losses - p2_losses
            bet_wnll_multi = np.polyval([bet_wnll_a, bet_wnll_b], [p_wnll])[0]
            bet_wnll_multi = min(bet_max_limit, max(bet_min_limit, bet_wnll_multi))
            bet_multi += int(round(bet_wnll_multi))
            if round(bet_wnll_multi) > 0:
                bet_multis_cat.append(f'wnll:{round(abs(bet_wnll_multi)):.0f}')

            # wins and losses winrate
            if p1_odds < p2_odds:
                p_wnlr = p1_wnl_winrate - p2_wnl_winrate
            else:
                p_wnlr = p2_wnl_winrate - p1_wnl_winrate
            bet_wnlr_multi = np.polyval([bet_wnlr_a, bet_wnlr_b], [p_wnlr])[0]
            bet_wnlr_multi = min(bet_max_limit, max(bet_min_limit, bet_wnlr_multi))
            bet_multi += int(round(bet_wnlr_multi))
            if round(bet_wnlr_multi) > 0:
                bet_multis_cat.append(f'wnlr:{round(abs(bet_wnlr_multi)):.0f}')

            # round
            bet_rnd_multi = np.polyval([bet_rnd_a, bet_rnd_b], [1 / match['round']])[0]
            bet_rnd_multi = min(bet_max_limit, max(bet_min_limit, bet_rnd_multi))
            bet_multi += int(round(bet_rnd_multi))
            if round(bet_rnd_multi) > 0:
                bet_multis_cat.append(f'rnd:{round(abs(bet_rnd_multi)):.0f}')

            # doors wins
            if p1_odds < p2_odds:
                p_drsw = p1_doors_wins - p2_doors_wins
            else:
                p_drsw = p2_doors_wins - p1_doors_wins
            bet_drsw_multi = np.polyval([bet_drsw_a, bet_drsw_b], [p_drsw])[0]
            bet_drsw_multi = min(bet_max_limit, max(bet_min_limit, bet_drsw_multi))
            bet_multi += int(round(bet_drsw_multi))
            if round(bet_drsw_multi) > 0:
                bet_multis_cat.append(f'drsw:{round(abs(bet_drsw_multi)):.0f}')

            # doors losses
            if p1_odds < p2_odds:
                p_drsl = p2_doors_losses - p1_doors_losses
            else:
                p_drsl = p1_doors_losses - p2_doors_losses
            bet_drsl_multi = np.polyval([bet_drsl_a, bet_drsl_b], [p_drsl])[0]
            bet_drsl_multi = min(bet_max_limit, max(bet_min_limit, bet_drsl_multi))
            bet_multi += int(round(bet_drsl_multi))
            if round(bet_drsl_multi) > 0:
                bet_multis_cat.append(f'drsl:{round(abs(bet_drsl_multi)):.0f}')

            # doors winrate
            if p1_odds < p2_odds:
                p_drs = p1_doors_winrate - p2_doors_winrate
            else:
                p_drs = p2_doors_winrate - p1_doors_winrate
            bet_drs_multi = np.polyval([bet_drs_a, bet_drs_b], [p_drs])[0]
            bet_drs_multi = min(bet_max_limit, max(bet_min_limit, bet_drs_multi))
            bet_multi += int(round(bet_drs_multi))
            if round(bet_drs_multi) > 0:
                bet_multis_cat.append(f'drs:{round(abs(bet_drs_multi)):.0f}')

            # surface wins
            if p1_odds < p2_odds:
                p_sfcw = p1_surface_wins - p2_surface_wins
            else:
                p_sfcw = p2_surface_wins - p1_surface_wins
            bet_sfcw_multi = np.polyval([bet_sfcw_a, bet_sfcw_b], [p_sfcw])[0]
            bet_sfcw_multi = min(bet_max_limit, max(bet_min_limit, bet_sfcw_multi))
            bet_multi += int(round(bet_sfcw_multi))
            if round(bet_sfcw_multi) > 0:
                bet_multis_cat.append(f'sfcw:{round(abs(bet_sfcw_multi)):.0f}')

            # surface winrate
            if p1_odds < p2_odds:
                p_sfcr = p1_surface_winrate - p2_surface_winrate
            else:
                p_sfcr = p2_surface_winrate - p1_surface_winrate
            bet_sfcr_multi = np.polyval([bet_sfcr_a, bet_sfcr_b], [p_sfcr])[0]
            bet_sfcr_multi = min(bet_max_limit, max(bet_min_limit, bet_sfcr_multi))
            bet_multi += int(round(bet_sfcr_multi))
            if round(bet_sfcr_multi) > 0:
                bet_multis_cat.append(f'sfcr:{round(abs(bet_sfcr_multi)):.0f}')

            # speed
            p1_speed = p1_speed_lin.intercept + p1_speed_lin.slope * match_speed
            p2_speed = p2_speed_lin.intercept + p2_speed_lin.slope * match_speed
            if p1_odds < p2_odds:
                p_spd = p1_speed - p2_speed
            else:
                p_spd = p2_speed - p1_speed
            bet_spd_multi = np.polyval([bet_spd_a, bet_spd_b], [p_spd])[0]
            bet_spd_multi = min(bet_max_limit, max(bet_min_limit, bet_spd_multi))
            bet_spd_multi = int(round(bet_spd_multi))
            if bet_spd_multi > 0:
                bet_multi += bet_spd_multi
                bet_multis_cat.append(f'spd:{bet_spd_multi}')

            # sets wins
            if p1_odds < p2_odds:
                p_setw = p1_sets_wins - p2_sets_wins
            else:
                p_setw = p2_sets_wins - p1_sets_wins
            bet_setw_multi = np.polyval([bet_setw_a, bet_setw_b], [p_setw])[0]
            bet_setw_multi = min(bet_max_limit, max(bet_min_limit, bet_setw_multi))
            bet_multi += int(round(bet_setw_multi))
            if round(bet_setw_multi) > 0:
                bet_multis_cat.append(f'setw:{round(abs(bet_setw_multi)):.0f}')

            # sets losses
            if p1_odds < p2_odds:
                p_setl = p2_sets_losses - p1_sets_losses
            else:
                p_setl = p1_sets_losses - p2_sets_losses
            bet_setl_multi = np.polyval([bet_setl_a, bet_setl_b], [p_setl])[0]
            bet_setl_multi = min(bet_max_limit, max(bet_min_limit, bet_setl_multi))
            bet_multi += int(round(bet_setl_multi))
            if round(bet_setl_multi) > 0:
                bet_multis_cat.append(f'setl:{round(abs(bet_setl_multi)):.0f}')

            # sets winrate
            if p1_odds < p2_odds:
                p_setr = p1_sets_winrate - p2_sets_winrate
            else:
                p_setr = p2_sets_winrate - p1_sets_winrate
            bet_setr_multi = np.polyval([bet_setr_a, bet_setr_b], [p_setr])[0]
            bet_setr_multi = min(bet_max_limit, max(bet_min_limit, bet_setr_multi))
            bet_multi += int(round(bet_setr_multi))
            if round(bet_setr_multi) > 0:
                bet_multis_cat.append(f'setr:{round(abs(bet_setr_multi)):.0f}')

            # games
            if p1_odds < p2_odds:
                p_gms = p1_gms_avg - p2_gms_avg
            else:
                p_gms = p2_gms_avg - p1_gms_avg
            bet_gms_multi = np.polyval([bet_gms_a, bet_gms_b], [p_gms])[0]
            bet_gms_multi = min(bet_max_limit, max(bet_min_limit, bet_gms_multi))
            bet_gms_multi = int(round(bet_gms_multi))
            if bet_gms_multi > 0:
                bet_multi += bet_gms_multi
                bet_multis_cat.append(f'gms:{bet_gms_multi}')

            # ties wins
            if p1_odds < p2_odds:
                p_tiew = p1_ties_wins - p2_ties_wins
            else:
                p_tiew = p2_ties_wins - p1_ties_wins
            bet_tiew_multi = np.polyval([bet_tiew_a, bet_tiew_b], [p_tiew])[0]
            bet_tiew_multi = min(bet_max_limit, max(bet_min_limit, bet_tiew_multi))
            bet_multi += int(round(bet_tiew_multi))
            if round(bet_tiew_multi) > 0:
                bet_multis_cat.append(f'tiew:{round(abs(bet_tiew_multi)):.0f}')

            # ties losses
            if p1_odds < p2_odds:
                p_tiel = p2_ties_losses - p1_ties_losses
            else:
                p_tiel = p1_ties_losses - p2_ties_losses
            bet_tiel_multi = np.polyval([bet_tiel_a, bet_tiel_b], [p_tiel])[0]
            bet_tiel_multi = min(bet_max_limit, max(bet_min_limit, bet_tiel_multi))
            bet_multi += int(round(bet_tiel_multi))
            if round(bet_tiel_multi) > 0:
                bet_multis_cat.append(f'tiel:{round(abs(bet_tiel_multi)):.0f}')

            # ties winrate
            if p1_odds < p2_odds:
                p_tier = p1_ties_winrate - p2_ties_winrate
            else:
                p_tier = p2_ties_winrate - p2_ties_winrate
            bet_tier_multi = np.polyval([bet_tier_a, bet_tier_b], [p_tier])[0]
            bet_tier_multi = min(bet_max_limit, max(bet_min_limit, bet_tier_multi))
            bet_multi += int(round(bet_tier_multi))
            if round(bet_tier_multi) > 0:
                bet_multis_cat.append(f'tier:{round(abs(bet_tier_multi)):.0f}')

            # upsets wins
            if p1_odds < p2_odds:
                p_upsw = p1_upsets_wins - p2_upsets_wins
            else:
                p_upsw = p2_upsets_wins - p1_upsets_wins
            bet_upsw_multi = np.polyval([bet_upsw_a, bet_upsw_b], [p_upsw])[0]
            bet_upsw_multi = min(bet_max_limit, max(bet_min_limit, bet_upsw_multi))
            bet_multi += int(round(bet_upsw_multi))
            if round(bet_upsw_multi) > 0:
                bet_multis_cat.append(f'upsw:{round(abs(bet_upsw_multi)):.0f}')

            # upsets losess
            if p1_odds < p2_odds:
                p_upsl = p2_upsets_losses - p1_upsets_losses
            else:
                p_upsl = p1_upsets_losses - p2_upsets_losses
            bet_upsl_multi = np.polyval([bet_upsl_a, bet_upsl_b], [p_upsl])[0]
            bet_upsl_multi = min(bet_max_limit, max(bet_min_limit, bet_upsl_multi))
            bet_multi += int(round(bet_upsl_multi))
            if round(bet_upsl_multi) > 0:
                bet_multis_cat.append(f'upsl:{round(abs(bet_upsl_multi)):.0f}')

            # upsets winrate
            if p1_odds < p2_odds:
                p_upsr = p1_upsets_win_avg - p2_upsets_win_avg
            else:
                p_upsr = p2_upsets_win_avg - p1_upsets_win_avg
            bet_upsr_multi = np.polyval([bet_upsr_a, bet_upsr_b], [p_upsr])[0]
            bet_upsr_multi = min(bet_max_limit, max(bet_min_limit, bet_upsr_multi))
            bet_multi += int(round(bet_upsr_multi))
            if round(bet_upsr_multi) > 0:
                bet_multis_cat.append(f'ups:{round(abs(bet_upsr_multi)):.0f}')

            # age
            if p1_odds < p2_odds:
                p_age = p1_age - p2_age
            else:
                p_age = p2_age - p1_age
            bet_age_multi = np.polyval([bet_age_a, bet_age_b], [p_age])[0]
            bet_age_multi = min(bet_max_limit, max(bet_min_limit, bet_age_multi))
            bet_age_multi = int(round(bet_age_multi))
            if bet_age_multi > 0:
                bet_multi += bet_age_multi
                bet_multis_cat.append(f'age:{bet_age_multi}')

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
        print(f'Score: {-res*100:.2f}  ROI {roi * 100:.1f}%  Profit ${total_payouts:.0f} {[round(p, 1) for p in hyper_params]}')
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
        #logger.info(f'Matches: {len(accuracy)}/{matches} = {len(accuracy)/max(1, matches)*100:.1f}%')
        #logger.info(f'Accuracy {accuracy_wins}/{len(accuracy)} = {accuracy_wins/len(accuracy)*100:.1f}% [ts:{trueskill_wins/max(1, len(trueskill))*100:.0f}%]')
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
        # 99.8  35.3    37.0    1483
        # 'bet_setr_a', 'bet_setr_b',  # 252

        # 99.5  35.5    36.9    1486
        # 'bet_tma_a', 'bet_tma_b',  # 63
        # 'bet_drsl_a', 'bet_drsl_b',  # 63
        
        # 94.0  38.6    33.7    1447
        # 'bet_upsl_a', 'bet_upsl_b',  # 234
        # 'bet_tiel_a', 'bet_tiel_b',  # 375

        # 94.0  38.7    33.7    1454
        # 'bet_wnll_a', 'bet_wnll_b',  # 491
        # 'bet_drs_a', 'bet_drs_b',  # 549
        # 'bet_sfcw_a', 'bet_sfcw_b',  # 819

        # 94.0  39.1    33.6    1476
        # 'bet_setw_a', 'bet_setw_b',  # 990      -
        # 'bet_drsw_a', 'bet_drsw_b',  # 1166     -
        # 'bet_tier_a', 'bet_tier_b',  # 1281     1335

        # 94.0  39.1    33.6    1477
        # 'bet_tsq_a', 'bet_tsq_b',  # 257      -     -
        # 'bet_setl_a', 'bet_setl_b',  # 554    -     -
        # 'bet_upsw_a', 'bet_upsw_b',  # 860    -     -

        # 93.8  39.2    33.6    1473
        # 'bet_upsr_a', 'bet_upsr_b',  # 374   -   -
        # 'bet_rnd_a', 'bet_rnd_b',  # 671   -   -
        # 'bet_ts_a', 'bet_ts_b',  # 977   6   3

        # 67.1  98.8    15.7    1263
        # 'bet_sfcr_a', 'bet_sfcr_b',  # 560   -   -
        # 'bet_wnlr_a', 'bet_wnlr_b',  # 905   -   -
        # 'bet_tiew_a', 'bet_tiew_b',  # 428   -   145

        # 94.4  38.8    34.0    1500
        # 'bet_wnlw_a', 'bet_wnlw_b',  # 540   -
        # 'odds_a', 'odds_b',  # 792   -
        # 'bet_spd_a', 'bet_spd_b',  # 1017   -   5

        'bet_gms_a', 'bet_gms_b',  # 113   -
        'bet_age_a', 'bet_age_b',  # 192   -
        'bet_tmi_a', 'bet_tmi_b',  # 684   24
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
        opts['tolx'] = 0.3
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
