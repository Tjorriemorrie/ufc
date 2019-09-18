from collections import Counter, defaultdict
from datetime import datetime
from functools import partial
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


def up_multi_bet(bet_multi, bet_multis_cat, x, y, wrd):
    bet_max_limit = 3
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

    all_data = DATA_2018_08 + DATA_2018_09 + DATA_2018_10 + \
               DATA_2019_01 + DATA_2019_02 + DATA_2019_03 + DATA_2019_04 + DATA_2019_05 + DATA_2019_06 + \
               DATA_2019_07 + DATA

    # bet_sfcr_a, bet_sfcr_b, bet_tiel_a, bet_tiel_b, bet_odds_a, bet_odds_b = hyper_params  
    bet_sfcr_a = 0.7623189877557279
    bet_sfcr_b = -5.155356822591676
    bet_tiel_a = -0.6535248444648468
    bet_tiel_b = -9.112779650829586
    bet_odds_a = 1.296120560959868
    bet_odds_b = -0.7131891179415546

    # bet_setl_a, bet_setl_b, bet_spd_a, bet_spd_b, bet_sfcw_a, bet_sfcw_b = hyper_params
    bet_setl_a = -0.059698580182552086
    bet_setl_b = -3.8428966510116593
    bet_spd_a = -0.4824098921960916
    bet_spd_b = -2.6696510671902365
    bet_sfcw_a = 0.1401149129313789
    bet_sfcw_b = -3.1079709159288775

    # bet_tsq_a, bet_tsq_b, bet_wnlw_a, bet_wnlw_b, bet_tma_a, bet_tma_b = hyper_params
    bet_tsq_a = -2.8589498777316775
    bet_tsq_b = -4.924031881458693
    bet_wnlw_a = -0.06797848250654259
    bet_wnlw_b = -4.842108321113209
    bet_tma_a = 0.2014330917734471
    bet_tma_b = -2.2016967696045695

    # bet_tiew_a, bet_tiew_b, bet_drsw_a, bet_drsw_b, bet_upsl_a, bet_upsl_b = hyper_params
    bet_tiew_a = -0.11518459439882577
    bet_tiew_b = -0.7752477104626799
    bet_drsw_a = -0.013968408637777072
    bet_drsw_b = 3.614418763199512e-05
    bet_upsl_a = 0.01902227468827618
    bet_upsl_b = -0.09036876762636295

    # bet_drs_a, bet_drs_b, bet_setw_a, bet_setw_b, bet_gms_a, bet_gms_b = hyper_params
    bet_drs_a = -4.045889829207174
    bet_drs_b = -6.357867007169345
    bet_setw_a = 0.23052922741125306
    bet_setw_b = -11.142249543232088
    bet_gms_a = -3.5307222893638857
    bet_gms_b = -13.45877377226569

    # bet_upsw_a, bet_upsw_b, bet_age_a, bet_age_b, bet_ts_a, bet_ts_b = hyper_params
    bet_upsw_a = 0.3031381023089167
    bet_upsw_b = -1.0593941425588922
    bet_age_a = 0.4674739422679419
    bet_age_b = 0.36106840973843424
    bet_ts_a = -0.2151557311301319
    bet_ts_b = -3.9726416933893276

    # bet_setr_a, bet_setr_b, bet_rnd_a, bet_rnd_b, bet_tmi_a, bet_tmi_b = hyper_params
    bet_setr_a = 15.67471796049661
    bet_setr_b = -8.089598387254687
    bet_rnd_a = -12.75956458166796
    bet_rnd_b = -30.66603732997164
    bet_tmi_a = -2.3076274429983696
    bet_tmi_b = -39.12394622919414

    # bet_drsl_a, bet_drsl_b, bet_wnll_a, bet_wnll_b, bet_tier_a, bet_tier_b = hyper_params
    bet_drsl_a = -2.273897913321413
    bet_drsl_b = -2.1664058079692095
    bet_wnll_a = 0.878681350031623
    bet_wnll_b = -0.07840025437711573
    bet_tier_a = 4.556752747212292
    bet_tier_b = 0.19786211838545698

    # bet_upsr_a, bet_upsr_b = hyper_params
    bet_upsr_a = -0.17413977493185512
    bet_upsr_b = -1.5822828381171026

    # bet_wnlr_a, bet_wnlr_b = hyper_params
    bet_wnlr_a = 0.6153821452215078
    bet_wnlr_b = -1.4081844335505949

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
        logger.info('')
        logger.info(f'{event["date"]} {event["location"]["name"]}')

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

            if train and random() > 0.80:
                continue

            log_odds = f'[{p1_odds:.2f} vs {p2_odds:.2f}]'
            log_trueskill = f'[{p1_ts:.0f}.{p1_sigma:.0f} vs {p2_ts:.0f}.{p2_sigma:.0f}]'

            ###############################
            # bet scaling
            bet_multi = -2

            # odds
            if p1_odds < p2_odds:
                p_odds = 1 / p1_odds - 1 / p2_odds
            else:
                p_odds = 1 / p2_odds - 1 / p1_odds
            bet_multi = up_multi_bet(bet_multi, bet_multis_cat, [bet_odds_a, bet_odds_b], p_odds, 'odds')

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
        res = -roi - (total_payouts / 10000)
        print(f'Score: {-res*100:.2f}  ROI {roi * 100:.1f}%  Profit ${total_payouts:.0f} {[round(p, 1) for p in hyper_params]}')
        return res
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
# TOLX set to 0.3
# BET MULTI INIT = 0
# TOLX set to 0.4

def run():
    train = 0

    names = [
        # 'bet_wnlr_a', 'bet_wnlr_b',  # 563     -     -     -     -
        # TOLX set to 0.5

        # 99.6  24.7    44.4    1303

        # TOLX set to 0.6

        # 97.9  25.8    43.4    1302
        # 'bet_upsr_a', 'bet_upsr_b',  # 479     -     -     -     -

        # TOLX set to 0.5
        # BET MULTI INIT = -2

        # 72.8  54.0    10.8    359
        # 'bet_drsl_a', 'bet_drsl_b',  # 420     4     -     -  1302
        # 'bet_wnll_a', 'bet_wnll_b',  # 507    25     -     -  1458
        # 'bet_tier_a', 'bet_tier_b',  # 575   952  1397   968  1163

        # 72.7  54.4    11.3    391
        # 'bet_setr_a', 'bet_setr_b',  # 675    26     -     -    80
        # 'bet_rnd_a', 'bet_rnd_b',    # 810     -     -     -     -
        # 'bet_tmi_a', 'bet_tmi_b',    # 919     6     -    20    21

        # 69.1  75.8    3.9     334
        # 'bet_upsw_a', 'bet_upsw_b',  # 417    28    77     1   286
        # 'bet_age_a', 'bet_age_b',    # 528  1933     -     -  2002
        # 'bet_ts_a', 'bet_ts_b',      # 563     -    28     -     -

        # 69.1  76.6    3.9     364
        # 'bet_drs_a', 'bet_drs_b',    # 536     -     -     -     -
        # 'bet_setw_a', 'bet_setw_b',  # 726    22     -     -   224
        # 'bet_gms_a', 'bet_gms_b',    # 804    20     -     3    55

        # 69.1  76.6    3.9     366
        # 'bet_tiew_a', 'bet_tiew_b',  # 566     2     4     -    64
        # 'bet_drsw_a', 'bet_drsw_b',  # 601     -     -     -     -
        # 'bet_upsl_a', 'bet_upsl_b',  # 698     -     -     -     -

        # 69.1  76.7    3.9     365
        # 'bet_tsq_a', 'bet_tsq_b',    # 564     -     -     -     -
        # 'bet_wnlw_a', 'bet_wnlw_b',  # 681     -     -     -     -
        # 'bet_tma_a', 'bet_tma_b',    # 778     4     5     -    33

        # DROPOUT 20% ADDED & DYNAMIC TOLX

        # 69.1  76.8    4.0     372
        # 'bet_setl_a', 'bet_setl_b',  # 404    44     -    59     2
        # 'bet_spd_a', 'bet_spd_b',    # 498    15     -     -     -
        # 'bet_sfcw_a', 'bet_sfcw_b',  # 513     -     -     -    45

        # 69.1  76.8    3.9     375
        'bet_sfcr_a', 'bet_sfcr_b',  # 684     -     -     -     -
        'bet_tiel_a', 'bet_tiel_b',  # 711   229     8     -    81
        'odds_a', 'odds_b',          # 780  1540  2778     -    18

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
            es.opts['tolx'] = es.result[3] / 2E3
            if es.result[3] > 1000:
                print('limit of 1000 reached')
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
