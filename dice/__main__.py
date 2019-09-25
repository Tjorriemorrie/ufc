from collections import Counter, deque
from queue import Queue
from random import random, randint

from loguru import logger


MULTI = 2

def update_balance(outcome: bool, balance: float, bet: int) -> float:
    balance -= bet
    if outcome:
        balance += bet * MULTI
    logger.info(f'Balance is {balance:.0f}')
    return balance


def do_roll():
    roll = random()
    odds = 1 / MULTI
    edge = 0.01
    odds *= 1 - edge
    outcome = roll < odds
    logger.info(f'Outcome: {outcome}  from roll {roll:.3f}  with odds {odds:.3f}')
    return outcome


def run():
    outcomes = []
    balance = 50
    while balance < 100:
        bet = 1
        outcome = do_roll()
        outcomes.append(outcome)
        balance = update_balance(outcome, balance, bet)
        if balance < 1:
            raise ValueError(f'broke after {len(outcomes)} rolls')
    else:
        logger.info(f'{balance} after {len(outcomes)} rolls')


def show_bets(bets):
    cntr = Counter(bets)
    depth = 0
    for bet, ins in cntr.items():
        depth += 1
        logger.info(f'{depth}: Made {ins} bets of {bet}')


def run_martingale():
    bets = []
    outcomes = []
    balance = 0
    outcome = True
    while balance < 1000:
        bet = 1 if outcome else bet * 2
        bets.append(bet)
        outcome = do_roll()
        outcomes.append(outcome)
        balance = update_balance(outcome, balance, bet)
        # if balance < 1:
        #     show_bets(bets)
        #     raise ValueError(f'broke after {len(outcomes)} rolls')
    else:
        logger.info(f'{balance} after {len(outcomes)} rolls')
        show_bets(bets)


def run_reverse_martingale():
    bets = []
    outcomes = []
    balance = 0
    outcome = False
    target = 1000
    while balance < target:
        # double on win
        bet = 1 if not outcome else bet * 2
        # reset after n wins
        if bet >= 2**4:
            bet = 1
        bets.append(bet)
        outcome = do_roll()
        outcomes.append(outcome)
        balance = update_balance(outcome, balance, bet)
        if balance < -target:
            show_bets(bets)
            raise ValueError(f'broke after {len(outcomes)} rolls')
    else:
        logger.info(f'{balance} after {len(outcomes)} rolls')
        show_bets(bets)


def labouchere():
    min_balance = 0
    target = 1000
    seq = deque()
    while sum(seq) < target:
        seq.append(randint(0, 3))
    seq.append(1)
    bets = []
    outcomes = []
    balance = 0
    while len(seq):
        # take left and right
        bet = seq[0] + seq[-1] if len(seq) > 1 else seq[0]
        if not bet:
            continue
        bets.append(bet)
        outcome = do_roll()
        outcomes.append(outcome)
        # update seq
        if outcome:
            seq.popleft()
            seq.pop()
        else:
            seq.append(bet)
        logger.info(f'seq: {list(seq)[-10:]}')
        balance = update_balance(outcome, balance, bet)
        min_balance = min(balance, min_balance)
        # if balance < -target:
        #     show_bets(bets)
        #     raise ValueError(f'broke after {len(outcomes)} rolls')
    else:
        logger.info(f'{balance} after {len(outcomes)} rolls')
        show_bets(bets)
        logger.info(f'min balance: {min_balance:.0f}')


if __name__ == '__main__':
    # run()
    # run_martingale()
    # run_reverse_martingale()
    labouchere()
