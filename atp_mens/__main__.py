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
from trueskill import BETA, global_env, rate_1vs1, Rating
from xgboost import XGBRegressor

from meta import get_default_metas, get_born_at, get_age_months
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


def main(hyper_params, train=0):
    logger.info('Starting main training')

    all_data = DATA_2018_09 + DATA_2018_10 + \
               DATA_2019_01 + DATA_2019_02 + DATA_2019_03 + DATA_2019_04 + DATA_2019_05 + DATA_2019_06 + \
               DATA_2019_07 + DATA

    # bet_odds_a, bet_odds_b, bet_wnl_a, bet_wnl_b = hyper_params
    bet_odds_a = -2.796214239170189
    bet_odds_b = -7.300107783807339
    bet_wnl_a = -0.12579947286600013
    bet_wnl_b = -3.8682243443122397
    
    # bet_ts_a, bet_ts_b, bet_tmi_a, bet_tmi_b, bet_tma_a, bet_tma_b = hyper_params
    bet_ts_a = -1.017802857966253
    bet_ts_b = 0.03262547342620006
    bet_tmi_a = -0.160162559876457
    bet_tmi_b = -1.7063966289790078
    bet_tma_a = -0.01789469044693269
    bet_tma_b = -1.8455239626477637

    # bet_drs_a, bet_drs_b, bet_sfc_a, bet_sfc_b, bet_spd_a, bet_spd_b = hyper_params
    bet_drs_a = -46.69400671644745
    bet_drs_b = -43.14525464218034
    bet_sfc_a = -34.372473174370654
    bet_sfc_b = -57.464154972163016
    bet_spd_a = -78.87421094555366
    bet_spd_b = -48.02601332583326

    # bet_set_a, bet_set_b, bet_gms_a, bet_gms_b, bet_tie_a, bet_tie_b = hyper_params
    bet_set_a = -216.95617358559656
    bet_set_b = -136.3076805016745
    bet_gms_a = -12.816726572357059
    bet_gms_b = -39.668420740556186
    bet_tie_a = 270.4904778034906
    bet_tie_b = -0.5099392191447849

    # bet_ups_a, bet_ups_b = hyper_params
    # -0.2   1106:65   30.4(1293) -> 30.2(1306)
    bet_ups_a = -10.513574590238619
    bet_ups_b = -2.024895047423263
    # bet_ups_a = 6.065608099428523    # 3.77   # 30.354441474757888  # -15.3330836557841
    # bet_ups_b = -1.1235452608356777  # 8.94    # 43.594727875509385  # -4.5704529715566675
    
    # bet_age_a, bet_age_b = hyper_params
    # -2.5   557:602   36.0(1173) -> 33.5(1295)
    bet_age_a = 4.678856696313377
    bet_age_b = 6.128009228103412

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
            p1_upsets_los_avg = p1_upsets[-1] / max(1, len(upsets[p1]))
            p2_upsets = Counter(upsets[p2])
            p2_upsets_wins = p2_upsets[1]
            p2_upsets_losses = p2_upsets[-1]
            p2_upsets_win_avg = p2_upsets[1] / max(1, len(upsets[p2]))
            p2_upsets_los_avg = p2_upsets[-1] / max(1, len(upsets[p2]))
            
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
            bet_odds_multi = min(1, max(-.1, bet_odds_multi))
            bet_multi += bet_odds_multi
            bet_multis_cat.append(f'odds:{round(abs(bet_odds_multi)):.0f}')

            # wins and losses
            if p1_odds < p2_odds:
                p_wnl = p1_wnl_winrate - p2_wnl_winrate
            else:
                p_wnl = p2_wnl_winrate - p1_wnl_winrate
            bet_wnl_multi = np.polyval([bet_wnl_a, bet_wnl_b], [p_wnl])[0]
            bet_wnl_multi = min(1, max(-.1, bet_wnl_multi))
            bet_multi += bet_wnl_multi
            bet_multis_cat.append(f'wnl:{round(abs(bet_wnl_multi)):.0f}')

            # trueskill mu
            if p1_odds < p2_odds:
                f_ts = p1_ts - p2_ts
            else:
                f_ts = p2_ts - p1_ts
            bet_ts_multi = np.polyval([bet_ts_a, bet_ts_b], [f_ts])[0]
            bet_ts_multi = min(1, max(-.1, bet_ts_multi))
            bet_multi += bet_ts_multi
            bet_multis_cat.append(f'ts:{round(abs(bet_ts_multi)):.0f}')

            # trueskill min
            if p1_odds < p2_odds:
                f_ts_min = p1_ts_min - p2_ts_min
            else:
                f_ts_min = p2_ts_min - p1_ts_min
            bet_tmi_multi = np.polyval([bet_tmi_a, bet_tmi_b], [f_ts_min])[0]
            bet_tmi_multi = min(1, max(-.1, bet_tmi_multi))
            bet_multi += bet_tmi_multi
            bet_multis_cat.append(f'tmi:{round(abs(bet_tmi_multi)):.0f}')

            # trueskill max
            if p1_odds < p2_odds:
                f_ts_max = p1_ts_max - p2_ts_max
            else:
                f_ts_max = p2_ts_max - p1_ts_max
            bet_tma_multi = np.polyval([bet_tma_a, bet_tma_b], [f_ts_max])[0]
            bet_tma_multi = min(1, max(-.1, bet_tma_multi))
            bet_multi += bet_tma_multi
            bet_multis_cat.append(f'tma:{round(abs(bet_tma_multi)):.0f}')

            # doors
            if p1_odds < p2_odds:
                p_drs = p1_doors_winrate - p2_doors_winrate
            else:
                p_drs = p2_doors_winrate - p1_doors_winrate
            bet_drs_multi = np.polyval([bet_drs_a, bet_drs_b], [p_drs])[0]
            bet_drs_multi = min(1, max(-.1, bet_drs_multi))
            bet_multi += bet_drs_multi
            bet_multis_cat.append(f'drs:{round(abs(bet_drs_multi)):.0f}')

            # surface
            if p1_odds < p2_odds:
                p_sfc = p1_surface_winrate - p2_surface_winrate
            else:
                p_sfc = p2_surface_winrate - p1_surface_winrate
            bet_sfc_multi = np.polyval([bet_sfc_a, bet_sfc_b], [p_sfc])[0]
            bet_sfc_multi = min(1, max(-.1, bet_sfc_multi))
            bet_multi += bet_sfc_multi
            bet_multis_cat.append(f'sfc:{round(abs(bet_sfc_multi)):.0f}')

            # speed
            p1_speed = p1_speed_lin.intercept + p1_speed_lin.slope * match_speed
            p2_speed = p2_speed_lin.intercept + p2_speed_lin.slope * match_speed
            if p1_odds < p2_odds:
                p_spd = p1_speed - p2_speed
            else:
                p_spd = p2_speed - p1_speed
            bet_spd_multi = np.polyval([bet_spd_a, bet_spd_b], [p_spd])[0]
            bet_spd_multi = min(1, max(-.1, bet_spd_multi))
            bet_multi += bet_spd_multi
            bet_multis_cat.append(f'spd:{round(abs(bet_spd_multi)):.0f}')

            # sets
            if p1_odds < p2_odds:
                p_set = p1_sets_winrate - p2_sets_winrate
            else:
                p_set = p2_sets_winrate - p1_sets_winrate
            bet_set_multi = np.polyval([bet_set_a, bet_set_b], [p_set])[0]
            bet_set_multi = min(1, max(-.1, bet_set_multi))
            bet_multi += bet_set_multi
            bet_multis_cat.append(f'set:{round(abs(bet_set_multi)):.0f}')

            # games
            if p1_odds < p2_odds:
                p_gms = p1_gms_avg - p2_gms_avg
            else:
                p_gms = p2_gms_avg - p1_gms_avg
            bet_gms_multi = np.polyval([bet_gms_a, bet_gms_b], [p_gms])[0]
            bet_gms_multi = min(1, max(-.1, bet_gms_multi))
            bet_multi += bet_gms_multi
            bet_multis_cat.append(f'gms:{round(abs(bet_gms_multi)):.0f}')

            # ties  655:14:237
            if p1_odds < p2_odds:
                p_tie = p1_ties_winrate - p2_ties_winrate
            else:
                p_tie = p2_ties_winrate - p2_ties_winrate
            bet_tie_multi = np.polyval([bet_tie_a, bet_tie_b], [p_tie])[0]
            bet_tie_multi = min(1, max(-.1, bet_tie_multi))
            bet_multi += bet_tie_multi
            bet_multis_cat.append(f'tie:{round(abs(bet_tie_multi)):.0f}')

            # upsets   840:50:16
            if p1_odds < p2_odds:
                p_upset = p1_upsets_win_avg - p2_upsets_win_avg
            else:
                p_upset = p2_upsets_win_avg - p1_upsets_win_avg
            bet_ups_multi = np.polyval([bet_ups_a, bet_ups_b], [p_upset])[0]
            bet_ups_multi = round(min(1, max(0, bet_ups_multi)))
            bet_multi += bet_ups_multi
            bet_multis_cat.append(f'ups:{bet_ups_multi:.0f}')

            # age
            if p1_odds < p2_odds:
                p_age = p1_age - p2_age
            else:
                p_age = p2_age - p1_age
            bet_age_multi = np.polyval([bet_age_a, bet_age_b], [p_age])[0]
            bet_age_multi = round(min(1, max(0, bet_age_multi)))
            bet_multi += bet_age_multi
            bet_multis_cat.append(f'age:{bet_age_multi:.0f}')

            log_players = f'x{round(bet_multi):.0f} {p1} {match.get("score")} {p2}'
            bet_amt = round(bet_size * bet_multi)
            bet_amts.append(bet_amt)
            bet_multis.append(int(round(bet_multi)))
            ###############################

            if 'prediction' in match and match['prediction'] is None:
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
                logger.warning(f'[{w_odds*100:.0f}% vs {l_odds*100:.0f}%] Bet x{round(bet_multi):.0f} on {w} to beat {l} [{ratings[w].mu:.0f} vs {ratings[l].mu:.0f}]')
                continue

            # no positive bet
            elif bet_amt < 1:
                logger.info(f'No bet!  {log_players} {log_odds} {log_trueskill}')
                continue

            # prediction bet on
            elif 'score' not in match:
                logger.warning(f'Pending {p1} vs {p2}')
                continue

            # testing outcome
            payout = -bet_amt
            if p1_odds < p2_odds:
                payout += p1_odds * bet_amt
            accuracy.append(1 if p1_odds < p2_odds else -1)
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
        res = -roi - (total_payouts / 1000)
        print(f'Score: {-res*100:.2f}  ROI {roi * 100:.1f}%  Profit ${total_payouts:.0f} {hyper_params}')
        return res
    else:
        summary(accuracy, payouts, bet_amts, start_date, actual, tab, tab_amts, bet_multis, bet_multis_cat, actual_debug)


def summary(accuracy, payouts, bet_amts, start_date, actual, tab, tab_amts, bet_multis, bet_multis_cat, actual_debug):
    if accuracy:
        payouts = np.array(payouts)
        logger.info('')
        logger.info('Testing:')
        accuracy_wins = sum([t for t in accuracy if t > 0])
        odds_acc = accuracy_wins / len(accuracy)
        logger.info(f'Accuracy {accuracy_wins}/{len(accuracy)} = {odds_acc*100:.1f}%')
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


# age
# serve strength
# weather
# rested
# days since last played?
# 1st serve conversion rate

def run():
    train = 0
    
    names = [
        # -1.0(-108)   odds:3566:0   wnl:3566:0
        # 0.0   3566:0   -1.4(-163) -> -1.4(-163)
        # 2.1   978:193   31.6(993) -> 33.7(1125)
        # 624:385
        # 0.1   3540:26   -1.3(-138) -> -1.2(-135)
        # 1.2   923:248   31.6(993) -> 32.8(1113)
        # 1009:0
        # 'odds_a', 'odds_b', 'bet_wnl_a', 'bet_wnl_b',
    
        # 'bet_ts_a', 'bet_ts_b', 'bet_tmi_a', 'bet_tmi_b', 'bet_tma_a', 'bet_tma_b',
        # -1.5(-148)   2641:900   3510:46   3566:0
        # 3514:52   -1.0(-105)
        # 1.5   964:207   35.1(1121) -> 36.6(1243)
        # 647:362
        # 1.1   907:264   36.5(1115) -> 37.6(1249)
        # 0.1   696:327   25.2(813) -> 25.3(899)

        # 'bet_drs_a', 'bet_drs_b', 'bet_sfc_a', 'bet_sfc_b', 'bet_spd_a', 'bet_spd_b',
        # 2.8(164)   3538:28    3566:0    3490:76
        # 0.5   1003:176   37.8(1153) -> 38.3(1236)
        # 0.7   866:157   21.5(765) -> 22.2(825)
        # -0.1   1112:67   3.0(133) -> 2.9(130)
        # 0.0   1179:0   33.5(1295) -> 33.5(1295)
        # 0.0   1023:0   25.3(954) -> 25.3(954)
        # 0.8   896:127   26.5(963) -> 27.3(1025)

        'bet_set_a', 'bet_set_b', 'bet_gms_a', 'bet_gms_b', 'bet_tie_a', 'bet_tie_b',
        # 6.8(319)   3536:30     3448:118    2457:1209
        # 1.0   927:219   23.6(957) -> 24.6(1050)
        # -0.2   809:362   26.7(1227) -> 26.5(1312)
        # 4.1   831:340   21.6(935) -> 25.7(1202)


        # 'bet_ups_a', 'bet_ups_b',       # -0.2
        # 'bet_age_a', 'bet_age_b',       # -2.5
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
