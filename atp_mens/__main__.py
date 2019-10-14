from collections import Counter, defaultdict
from datetime import datetime
from itertools import chain
from random import random
from time import time

import numpy as np
from cma import CMAEvolutionStrategy, CMAOptions
from loguru import logger
from math import sqrt
from scipy.stats import linregress
from trueskill import BETA, global_env, quality_1vs1, rate_1vs1, Rating

from meta import get_age_months
from .data import DATA
from .data_2018_07 import DATA_2018_07
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
from .data_2019_08 import DATA_2019_08


def win_probability(team1, team2):
    delta_mu = sum(r.mu for r in team1) - sum(r.mu for r in team2)
    sum_sigma = sum(r.sigma ** 2 for r in chain(team1, team2))
    size = len(team1) + len(team2)
    denom = sqrt(size * (BETA * BETA) + sum_sigma)
    ts = global_env()
    return ts.cdf(delta_mu / denom)


def up_multi_bet(bet_multi, bet_multis_cat, x, y, wrd):
    global big_multis
    bet_max_limit = big_multis[wrd]
    bet_min_limit = 0
    bet_single_multi = np.polyval(x, [y])[0]
    bet_single_multi = min(bet_max_limit, max(bet_min_limit, bet_single_multi))
    bet_single_multi = int(round(bet_single_multi))
    if bet_single_multi > 0:
        bet_multi += bet_single_multi
        bet_multis_cat.append(f'{wrd}')
    return bet_multi


def main(hyper_params, train=0):
    logger.info('Starting main training')

    all_data = DATA_2018_07 + DATA_2018_08 + DATA_2018_09 + DATA_2018_10 + \
               DATA_2019_01 + DATA_2019_02 + DATA_2019_03 + DATA_2019_04 + DATA_2019_05 + DATA_2019_06 + \
               DATA_2019_07 + DATA_2019_08 + DATA

    # bet_setl_a, bet_setl_b, bet_tsq_a, bet_tsq_b, bet_tier_a, bet_tier_b = hyper_params
    bet_setl_a = 0.003547243116299857
    bet_setl_b = -3.861896378376332
    bet_tsq_a = 5.479267992440732
    bet_tsq_b = -9.648866514452548
    bet_tier_a = 6.5307593880792885
    bet_tier_b = 0.4000578535352791

    # bet_upsr_a, bet_upsr_b, bet_gms_a, bet_gms_b, bet_rnd_a, bet_rnd_b = hyper_params
    bet_upsr_a = -1.971821163969833
    bet_upsr_b = -2.714993826912822
    bet_gms_a = -0.07081530381648547
    bet_gms_b = -0.6464413057857362
    bet_rnd_a = 0.04630758154678022
    bet_rnd_b = -1.3081222313175223

    # bet_drsw_a, bet_drsw_b, bet_upsl_a, bet_upsl_b, bet_lati_a, bet_lati_b = hyper_params 
    bet_drsw_a = -0.07726263693379504
    bet_drsw_b = -6.180112171558808
    bet_upsl_a = 0.13867003909369277
    bet_upsl_b = -3.077443981704128
    bet_lati_a = -14.869394041039122
    bet_lati_b = 0.3868115567700346

    # bet_sfcw_a, bet_sfcw_b, bet_tiel_a, bet_tiel_b, bet_ts_a, bet_ts_b = hyper_params
    bet_sfcw_a = 0.029922516882589754
    bet_sfcw_b = -2.156517395176721
    bet_tiel_a = 0.006657055419871865
    bet_tiel_b = -2.0930223396596217
    bet_ts_a = -0.08501472140848632
    bet_ts_b = -3.325327782403146

    # bet_wnlr_a, bet_wnlr_b, bet_tmi_a, bet_tmi_b, bet_spd_a, bet_spd_b = hyper_params 
    bet_wnlr_a = 5.037100709561853
    bet_wnlr_b = -4.727011637976734
    bet_tmi_a = -0.3299530415897716
    bet_tmi_b = -7.50324328203788
    bet_spd_a = 2.8823103952222815
    bet_spd_b = -4.799463638782232

    # bet_wnll_a, bet_wnll_b, bet_drsl_a, bet_drsl_b, bet_setw_a, bet_setw_b = hyper_params
    bet_wnll_a = 0.4585441889372742
    bet_wnll_b = 3.5651650781577064
    bet_drsl_a = -0.48518572776814883
    bet_drsl_b = -1.830294398000765
    bet_setw_a = 3.5380337239586708
    bet_setw_b = 3.84880579581161

    # bet_age_a, bet_age_b, bet_wnlw_a, bet_wnlw_b, bet_odds_a, bet_odds_b = hyper_params
    bet_age_a = 0.014508866742424182
    bet_age_b = -17.90556862056867
    bet_wnlw_a = -5.395799209143199
    bet_wnlw_b = -8.26319978507212
    bet_odds_a = -18.133520553408545 
    bet_odds_b = -0.019926303519551603

    # bet_tma_a, bet_tma_b, bet_drs_a, bet_drs_b, bet_upsw_a, bet_upsw_b = hyper_params
    bet_tma_a = -0.22441169149864815
    bet_tma_b = -8.853123514772761
    bet_drs_a = 1.4907554725488155
    bet_drs_b = -5.995045379683105
    bet_upsw_a = 0.04649809384613163
    bet_upsw_b = -4.8265137267641745

    # bet_sfcr_a, bet_sfcr_b, bet_tiew_a, bet_tiew_b, 
    bet_sfcr_a = -186.99651516374132
    bet_sfcr_b = -155.28818282681394
    bet_tiew_a = 24.264625576798657
    bet_tiew_b = -911.0818839108558

    # bet_setr_a, bet_setr_b,  
    bet_setr_a = 2.5601067834350024
    bet_setr_b = -2.5643017427402435

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
    last_ties = defaultdict(lambda: [])
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
        logger.info('')
        logger.info(f'{event["date"]} {event["location"]["name"]}')

        for match in event['matches']:
            # skip if no odds:
            if 'odds' not in match:
                continue

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

            # last ties
            p1_lati = Counter(last_ties[p1])
            p1_lati_winrate = p1_lati[1] / max(1, len(last_ties[p1]))
            p2_lati = Counter(last_ties[p2])
            p2_lati_winrate = p2_lati[1] / max(1, len(last_ties[p2]))

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
                ties[p1] += [1 if v[0] == 7 else -1 for v in match['score'] if 7 in v and 6 in v]
                ties[p2] += [1 if v[1] == 7 else -1 for v in match['score'] if 7 in v and 6 in v]

                # update last ties
                if match['score'] and 7 in match['score'][-1] and 6 in match['score'][-1]:
                    last_ties[p1].append(1 if match['score'][-1][0] == 7 else -1)
                    last_ties[p2].append(1 if match['score'][-1][1] == 7 else -1)

                # update upsets
                upset = p2_odds < p1_odds
                upsets[p1] += [1 if upset else 0]
                upsets[p2] += [-1 if upset else 0]

            if train and random() > 0.80:
                continue
            matches += 1

            log_odds = f'[{p1_odds:.2f} vs {p2_odds:.2f}]'
            log_trueskill = f'[{p1_ts:.0f}.{p1_sigma:.0f} vs {p2_ts:.0f}.{p2_sigma:.0f}]'

            ###############################
            # bet scaling
            bet_multi = -4

            # odds
            if p1_odds < p2_odds:
                f_odds = p1_odds
            else:
                f_odds = p2_odds
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_odds_a, bet_odds_b], f_odds, 'odds')

            # trueskill mu
            if p1_odds < p2_odds:
                f_ts = p1_ts - p2_ts
            else:
                f_ts = p2_ts - p1_ts
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_ts_a, bet_ts_b], f_ts, 'ts')

            # trueskill min
            if p1_odds < p2_odds:
                f_ts_min = p1_ts_min - p2_ts_min
            else:
                f_ts_min = p2_ts_min - p1_ts_min
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_tmi_a, bet_tmi_b], f_ts_min, 'tmi')

            # trueskill max
            if p1_odds < p2_odds:
                f_ts_max = p1_ts_max - p2_ts_max
            else:
                f_ts_max = p2_ts_max - p1_ts_max
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_tma_a, bet_tma_b], f_ts_max, 'tma')

            # trueskill match quality
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_tsq_a, bet_tsq_b], ts_quality, 'tsq')

            # wins and losses wins
            if p1_odds < p2_odds:
                p_wnlw = p1_wins - p2_wins
            else:
                p_wnlw = p2_wins - p1_wins
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_wnlw_a, bet_wnlw_b], p_wnlw, 'wnlw')

            # wins and losses lost
            if p1_odds < p2_odds:
                p_wnll = p2_losses - p1_losses
            else:
                p_wnll = p1_losses - p2_losses
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_wnll_a, bet_wnll_b], p_wnll, 'wnll')

            # wins and losses winrate
            if p1_odds < p2_odds:
                p_wnlr = p1_wnl_winrate - p2_wnl_winrate
            else:
                p_wnlr = p2_wnl_winrate - p1_wnl_winrate
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_wnlr_a, bet_wnlr_b], p_wnlr, 'wnlr')

            # round
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_rnd_a, bet_rnd_b], 1 / match['round'], 'rnd')

            # doors wins
            if p1_odds < p2_odds:
                p_drsw = p1_doors_wins - p2_doors_wins
            else:
                p_drsw = p2_doors_wins - p1_doors_wins
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_drsw_a, bet_drsw_b], p_drsw, 'drsw')

            # doors losses
            if p1_odds < p2_odds:
                p_drsl = p2_doors_losses - p1_doors_losses
            else:
                p_drsl = p1_doors_losses - p2_doors_losses
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_drsl_a, bet_drsl_b], p_drsl, 'drsl')

            # doors winrate
            if p1_odds < p2_odds:
                p_drs = p1_doors_winrate - p2_doors_winrate
            else:
                p_drs = p2_doors_winrate - p1_doors_winrate
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_drs_a, bet_drs_b], p_drs, 'drs')

            # surface wins
            if p1_odds < p2_odds:
                p_sfcw = p1_surface_wins - p2_surface_wins
            else:
                p_sfcw = p2_surface_wins - p1_surface_wins
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_sfcw_a, bet_sfcw_b], p_sfcw, 'sfcw')

            # surface winrate
            if p1_odds < p2_odds:
                p_sfcr = p1_surface_winrate - p2_surface_winrate
            else:
                p_sfcr = p2_surface_winrate - p1_surface_winrate
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_sfcr_a, bet_sfcr_b], p_sfcr, 'sfcr')

            # speed
            p1_speed = p1_speed_lin.intercept + p1_speed_lin.slope * match_speed
            p2_speed = p2_speed_lin.intercept + p2_speed_lin.slope * match_speed
            if p1_odds < p2_odds:
                p_spd = p1_speed - p2_speed
            else:
                p_spd = p2_speed - p1_speed
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_spd_a, bet_spd_b], p_spd, 'spd')

            # sets wins
            if p1_odds < p2_odds:
                p_setw = p1_sets_wins - p2_sets_wins
            else:
                p_setw = p2_sets_wins - p1_sets_wins
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_setw_a, bet_setw_b], p_setw, 'setw')

            # sets losses
            if p1_odds < p2_odds:
                p_setl = p2_sets_losses - p1_sets_losses
            else:
                p_setl = p1_sets_losses - p2_sets_losses
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_setl_a, bet_setl_b], p_setl, 'setl')

            # sets winrate
            if p1_odds < p2_odds:
                p_setr = p1_sets_winrate - p2_sets_winrate
            else:
                p_setr = p2_sets_winrate - p1_sets_winrate
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_setr_a, bet_setr_b], p_setr, 'setr')

            # games
            if p1_odds < p2_odds:
                p_gms = p1_gms_avg - p2_gms_avg
            else:
                p_gms = p2_gms_avg - p1_gms_avg
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_gms_a, bet_gms_b], p_gms, 'gms')

            # ties wins
            if p1_odds < p2_odds:
                p_tiew = p1_ties_wins - p2_ties_wins
            else:
                p_tiew = p2_ties_wins - p1_ties_wins
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_tiew_a, bet_tiew_b], p_tiew, 'tiew')

            # ties losses
            if p1_odds < p2_odds:
                p_tiel = p2_ties_losses - p1_ties_losses
            else:
                p_tiel = p1_ties_losses - p2_ties_losses
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_tiel_a, bet_tiel_b], p_tiel, 'tiel')

            # ties winrate
            if p1_odds < p2_odds:
                p_tier = p1_ties_winrate - p2_ties_winrate
            else:
                p_tier = p2_ties_winrate - p2_ties_winrate
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_tier_a, bet_tier_b], p_tier, 'tier')

            # last ties winrate
            if p1_odds < p2_odds:
                p_lati = p1_lati_winrate - p2_lati_winrate
            else:
                p_lati = p2_lati_winrate - p2_lati_winrate
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_lati_a, bet_lati_b], p_lati, 'lati')

            # upsets wins
            if p1_odds < p2_odds:
                p_upsw = p1_upsets_wins - p2_upsets_wins
            else:
                p_upsw = p2_upsets_wins - p1_upsets_wins
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_upsw_a, bet_upsw_b], p_upsw, 'upsw')

            # upsets losess
            if p1_odds < p2_odds:
                p_upsl = p2_upsets_losses - p1_upsets_losses
            else:
                p_upsl = p1_upsets_losses - p2_upsets_losses
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_upsl_a, bet_upsl_b], p_upsl, 'upsl')

            # upsets winrate
            if p1_odds < p2_odds:
                p_upsr = p1_upsets_win_avg - p2_upsets_win_avg
            else:
                p_upsr = p2_upsets_win_avg - p1_upsets_win_avg
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_upsr_a, bet_upsr_b], p_upsr, 'upsr')

            # age
            if p1_odds < p2_odds:
                p_age = p1_age - p2_age
            else:
                p_age = p2_age - p1_age
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_age_a, bet_age_b], p_age, 'age')

            log_players = f'x{bet_multi:.0f} {p1} {match.get("score")} {p2}'
            bet_amt = round(bet_size * bet_multi)
            ###############################

            # make prediction
            if 'prediction' in match and match['prediction'] is None:
                # no positive bet
                if bet_amt < 1:
                    logger.warning(f'No bet!  {p1} vs {p2} {log_odds} {log_trueskill}')
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
                logger.warning(f'[{w_odds:.2f} vs {l_odds:.2f}] Bet x{round(bet_multi):.0f} on {w} to beat {l} [{ratings[w].mu:.0f} vs {ratings[l].mu:.0f}]')
                continue

            # prediction bet on
            if 'score' not in match:
                logger.warning(f'Pending {p1} vs {p2}')
                continue

            if bet_amt < 1:
                logger.info(f'no bet {log_players} {log_odds} {log_trueskill}')
                continue

            # testing outcome
            payout = -bet_amt
            if p1_odds < p2_odds:
                payout += p1_odds * bet_amt

            accuracy.append(1 if p1_odds < p2_odds else -1)
            trueskill.append(1 if p1_ts > p2_ts else -1)
            bet_amts.append(bet_amt)
            bet_multis.append(bet_multi)
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

            logger.info(f'{log_balance} {log_players} {log_odds} {log_trueskill}')

    if train:
        total_payouts = sum(payouts)
        roi = total_payouts / sum(bet_amts)
        participation = len(accuracy) / max(1, matches)
        # res = roi + participation / 4 + total_payouts / 100000
        res = roi * participation
        print(f'Score: {res*100:.2f}  ROI: {roi * 100:.1f}%  Part: {participation*100:.1f}%  Profit: ${total_payouts:.0f} {[round(p, 1) for p in hyper_params]}')
        return -res
    else:
        summary(accuracy, payouts, bet_amts, start_date, actual, tab, tab_amts, bet_multis, bet_multis_cat, actual_debug, matches, trueskill)


def summary(accuracy, payouts, bet_amts, start_date, actual, tab, tab_amts, bet_multis, bet_multis_cat, actual_debug, matches, trueskill):
    if accuracy:
        payouts = np.array(payouts)
        logger.info('')
        logger.info('Testing:')
        accuracy_wins = sum([t for t in accuracy if t > 0])
        trueskill_wins = sum([t for t in trueskill if t > 0])
        logger.info(f'Matches: {len(accuracy)}/{matches} = {len(accuracy)/max(1, matches)*100:.1f}%')
        logger.info(f'Accuracy {accuracy_wins}/{len(accuracy)} = {accuracy_wins/len(accuracy)*100:.1f}% [ts:{trueskill_wins/max(1, len(trueskill))*100:.0f}%]')
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
        # sheet = -74.59
        # if abs(sum(tab) - sheet) > 0.01:
        #     for l in actual_debug:
        #         logger.warning(l)
        #     logger.error(f'debug! {sheet:.2f} != {sum(tab):.2f} diff {sum(tab) - sheet:.2f}')


# serve strength
# weather
# rested
# days since last played?
# 1st serve conversion rate

# bet multi set to -1 !!
# GO ANOTHER ROUND WITH -1 AND SEE IF IT STABILISES
# THE ISSUE SEEMS TO BE FIXED BY MAKING REWARD MORE PROFIT WEIGHT 10000
# BET MULTI INIT = 0
# TOLX set to 0.5
# TOLX set to 0.6
# TOLX set to 0.5
# BET MULTI INIT = -2
# DROPOUT 20% ADDED & DYNAMIC TOLX
# TOLX SET TO 2500
# DROP OUT SET TO 25%
# DROP OUT SET TO 20%
# SCORE SET TO ROI * PART
# TOLX SET TO 3000
# BET MULTI CHANGED TO -3
# TOLX set to 2500 (ran for more than 2 hours)
# BET MULTI CHANGED TO -4

big_multis = {
    'odds': 1,
    'ts': 1,
    'tsq': 1,
    'tma': 1,
    'tmi': 1,
    'wnlw': 3,
    'wnll': 2,
    'wnlr': 1,
    'drsw': 1,
    'drsl': 2,
    'drs': 1,
    'sfcw': 1,
    'sfcr': 1,
    'spd': 1,
    'rnd': 1,
    'gms': 1,
    'setw': 3,
    'setl': 1,
    'setr': 1,
    'tiew': 1,
    'tiel': 1,
    'tier': 3,
    'lati': 3,
    'upsw': 1,
    'upsl': 1,
    'upsr': 1,
    'age': 2,
}


def run():
    train = 0
    
    names = [
        # 72    88      23      2800
        # 'bet_setr_a', 'bet_setr_b',  # 1125     -     -    84     -

        # 72    88      23      2900
        # 'bet_sfcr_a', 'bet_sfcr_b',  # 1046      -     -    55    68
        # 'bet_tiew_a', 'bet_tiew_b',  # 1081   1532     -     -     -
        # MAJOR CHANGE tiew 2 -> 1

        # 73    86      26      2800
        # 'bet_tma_a', 'bet_tma_b',    # 719      -    20  1632     -
        # 'bet_drs_a', 'bet_drs_b',    # 770      -     7     -     -
        # 'bet_upsw_a', 'bet_upsw_b',  # 823      -   386     -     -

        # 72    88      25      2800
        # 'bet_age_a', 'bet_age_b',    # 1059  2234  2281     -     -
        # 'bet_wnlw_a', 'bet_wnlw_b',  # 1087  2471   893   914   928
        # 'bet_odds_a', 'bet_odds_b',  # 1271     -     -     1     -

        # 70    91      24      2900
        # 'bet_wnll_a', 'bet_wnll_b',  # 655   3949     -     -  3796
        # 'bet_drsl_a', 'bet_drsl_b',  # 801   2757     -  3921   867
        # 'bet_setw_a', 'bet_setw_b',  # 879   3251  2731  3491  3521

        # 70    91      24      2900
        # 'bet_wnlr_a', 'bet_wnlr_b',  # 703      -    12     -     -
        # 'bet_tmi_a', 'bet_tmi_b',    # 773     63   716     -     -
        # 'bet_spd_a', 'bet_spd_b',    # 774      5     -     -     -

        # 70    91      24      2900
        # 'bet_sfcw_a', 'bet_sfcw_b',  # 802      3     -    34     -
        # 'bet_tiel_a', 'bet_tiel_b',  # 899      -     2    30     -
        # 'bet_ts_a', 'bet_ts_b',      # 1161  1795   133    11     -
        # MAJOR CHANGE ts 2 -> 1

        # 71    89      20      2700
        # 'bet_drsw_a', 'bet_drsw_b',  # 639   1198     3    19     -
        # 'bet_upsl_a', 'bet_upsl_b',  # 923     37     -  1126    33
        # 'bet_lati_a', 'bet_lati_b',  # 956   1251   940   994  1028

        # 70    91      24      2800
        # 'bet_upsr_a', 'bet_upsr_b',  # 604      -     -     -     -
        # 'bet_gms_a', 'bet_gms_b',    # 729     75    77     -     -
        # 'bet_rnd_a', 'bet_rnd_b',    # 902      -     -     -     -

        # 70    90      21      2100
        'bet_setl_a', 'bet_setl_b',  # 643   1578     1     -     -
        'bet_tsq_a', 'bet_tsq_b',    # 725      -     -     -     -
        'bet_tier_a', 'bet_tier_b',  # 850   1066  1593  1615  1606
        # MAJOR CHANGE setl 2 -> 1

    ]
    tolx = 2050  # higher is slower
    params = [0, 0, 0, 0, 0, 0]
    bounds = [
        [-np.inf],
        [np.inf]
    ]
    assert len(params) == len(names)
    # assert len(params) == len(bounds)

    if train:
        time_start = time()
        sigma = 1
        opts = CMAOptions()
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
            # print(list(es.result[0]))
            print(f'tolx={es.opts["tolx"]:.3f}  sol={list(es.result[5])}')
            es.opts['tolx'] = es.result[3] / tolx
            if time() - time_start > 60 * 180:
                print('3 hour limit reached')
                break
        es.result_pretty()
        print(f'finished after {es.result[3]} evaluations and {es.result[4]} iterations')
        # print('')
        # print('best')
        # print(list(es.result[0]))
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
