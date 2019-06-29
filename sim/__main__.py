from collections import defaultdict
from itertools import chain
from math import sqrt

from loguru import logger
from trueskill import quality_1vs1, Rating, BETA, global_env, rate_1vs1

from data import DATA

BET_AMT = 10


def win_probability(team1, team2):
    delta_mu = sum(r.mu for r in team1) - sum(r.mu for r in team2)
    sum_sigma = sum(r.sigma ** 2 for r in chain(team1, team2))
    size = len(team1) + len(team2)
    denom = sqrt(size * (BETA * BETA) + sum_sigma)
    ts = global_env()
    return ts.cdf(delta_mu / denom)


def get_implied_odds(american):
    if american > 0:
        return 100 / (american + 100)
    return abs(american) / (abs(american) + 100)


def main():
    ratings = defaultdict(lambda: Rating())
    balance = 0
    accuracy = (0, 0)
    ac_msgs = []
    logger.info(f'Balance is {balance}. good luck!')

    for scene in DATA:
        logger.info(f'{scene["date"]} {scene["name"]}')
        for fight in scene['fights']:
            f1 = fight['fighters'][0]['name']
            f2 = fight['fighters'][1]['name']

            draw_prob = round(quality_1vs1(ratings[f1], ratings[f2]), 2)
            win1_prob = round(win_probability([ratings[f1]], [ratings[f2]]), 2)

            # get winner
            fw = fight['winner']['fighter']
            is_win_1 = fw == f1
            fl = f2 if is_win_1 else f1
            if not is_win_1 and fw != f2:
                raise ValueError(f'unknown winner {fw}')

            # skip if no odds:
            if not 'odds' in fight:
                continue

            # absolute betting
            correct = 0
            payout = -BET_AMT
            f1_odds = fight['odds'][f1]
            f2_odds = fight['odds'][f2]
            if is_win_1 and (win1_prob > 0.5 or win1_prob == 0.5 and f1_odds < f2_odds):
                correct = 1
                if f1_odds > 0:
                    payout += f1_odds / BET_AMT + BET_AMT
                else:
                    payout += 100 * BET_AMT / abs(f1_odds) + BET_AMT
            elif not is_win_1 and (win1_prob < 0.5 or win1_prob == 0.5 and f2_odds < f1_odds):
                correct = 1
                if f2_odds > 0:
                    payout += f2_odds / BET_AMT + BET_AMT
                else:
                    payout += 100 * BET_AMT / abs(f2_odds) + BET_AMT
            balance += payout

            logger.info(f'[{ratings[fw].mu:.2f} : {ratings[fl].mu:.2f}] {fw} {fight["winner"]["by"]} {fl} ==> {payout:.0f} bal:{balance:.0f}')

            # accuracy
            if round(ratings[fw].mu, 2) != 25 and round(ratings[fl].mu, 2) != 25:
                accuracy = (accuracy[0] + correct, accuracy[1] + 1)
                ac_msgs.append(f'{fw} [{ratings[fw].mu:.2f}] bt {fl} [{ratings[fl].mu:.2f}]')

            # update ratings
            ratings[fw], ratings[fl] = rate_1vs1(ratings[fw], ratings[fl])

    if accuracy[1]:
        for msg in ac_msgs:
            logger.info(msg)
        logger.info(f'Accuracy {accuracy[0]}/{accuracy[1]} = {accuracy[0]/accuracy[1]*100:.0f}%')


def to_decimal_odds(us_odds):
    if us_odds > 0:
        return us_odds / 100 + 1
    else:
        return 100 / us_odds + 1


if __name__ == '__main__':
    main()


# from trueskill import Rating, quality_1vs1, rate_1vs1
# alice, bob = Rating(25), Rating(30)  # assign Alice and Bob's ratings
# if quality_1vs1(alice, bob) < 0.50:
#     print('This match seems to be not so fair')
# alice, bob = rate_1vs1(alice, bob)  # update the ratings after the match
