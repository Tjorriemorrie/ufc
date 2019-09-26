from collections import Counter, deque
from queue import Queue
from random import random, randint

from loguru import logger


MULTI = 2

def update_balance(outcome: bool, balance: float, bet: int, multi: float = None) -> float:
    multi = multi or MULTI
    balance -= bet
    payout = 0
    if outcome:
        payout = bet * multi
        balance += payout
    logger.info(f'Balance is {balance:.0f}  bet was {bet:.1f}  multi: {multi:.1f}  payout: {payout:.1f}  profit: {payout - bet:.1f}')
    return balance


def do_roll(multi=None):
    multi = multi or MULTI
    roll = random()
    odds = 1 / multi
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


def run_dice():
    bets = []
    outcomes = []
    balance = 10000
    min_balance = balance
    target = balance * 2
    losing_streak = 0
    running_loss = 0
    odds = 1 / 3
    bet = 1
    while balance < target:
        bets.append(bet)
        outcome = do_roll(multi=1 / odds)
        outcomes.append(outcome)
        balance = update_balance(outcome, balance, bet, multi=1 / odds)
        min_balance = min(min_balance, balance)
        # update bet
        if outcome:
            # reset
            losing_streak = 0
            bet = 1
            odds = 1 / 3
            running_loss = 0
        else:
            losing_streak += 1
            running_loss += bet
            odds = 1 - (1 / (losing_streak + 1))
            bet = (running_loss / (1 - odds)) - running_loss
            logger.info(f'Streak: {losing_streak}  Losses: {running_loss:.1f}  odds: {odds:.2f}  bet: {bet:.1f}')
        # fail
        if balance < 1:
            show_bets(bets)
            raise ValueError(f'broke after {len(outcomes)} rolls')
        if bet > balance:
            show_bets(bets)
            raise ValueError(f'broke after {len(outcomes)} rolls, no money to bet {bet:.1f}')

    else:
        show_bets(bets)
        logger.info(f'{balance} after {len(outcomes)} rolls')
        logger.info(f'Minimum balance {min_balance:.0f}')


def run_reverse_dice():
    bets = []
    outcomes = []
    balance = 10000
    min_balance = balance
    target = balance * 2
    losing_streak = 0
    running_loss = 0
    last_loss = 0
    multi = 1.5
    bet = 1
    while balance < target:
        bets.append(bet)
        outcome = do_roll(multi=multi)
        outcomes.append(outcome)
        balance = update_balance(outcome, balance, bet, multi=multi)
        min_balance = min(min_balance, balance)
        # update bet
        if outcome:
            # reset
            losing_streak = 0
            last_loss = 0
            bet = 1
            multi = 1.5
            running_loss = 0
        else:
            losing_streak += 1
            running_loss += bet
            last_loss, bet = bet, bet + last_loss
            # if losing_streak < 3:
            #     bet = 1
            multi = (running_loss / bet) + 1
            logger.info(f'Streak: {losing_streak}  Losses: {running_loss:.1f}  odds: {1/multi:.2f}  bet: {bet:.1f}')
        # fail
        if balance < 1:
            show_bets(bets)
            raise ValueError(f'broke after {len(outcomes)} rolls')
        if bet > balance:
            show_bets(bets)
            raise ValueError(f'broke after {len(outcomes)} rolls, no money to bet {bet:.1f}')

    else:
        show_bets(bets)
        logger.info(f'{balance} after {len(outcomes)} rolls')
        logger.info(f'Minimum balance {min_balance:.0f}')


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
    balance = 100000
    target = balance * 2
    checkpoint = balance
    bet = 1
    while balance < target:
        bets.append(bet)
        outcome = do_roll()
        outcomes.append(outcome)
        balance = update_balance(outcome, balance, bet)
        # double on win
        bet = 1 if not outcome else bet * 2
        # reset after checkpoint breached
        if balance > checkpoint:
            checkpoint = balance
            bet = 1
        if balance < 0:
            show_bets(bets)
            logger.info(f'Checkpoint is at {checkpoint:.0f}')
            raise ValueError(f'broke after {len(outcomes)} rolls')
        if bet > balance:
            show_bets(bets)
            logger.info(f'Checkpoint is at {checkpoint:.0f}')
            raise ValueError(f'broke after {len(outcomes)} rolls, no money to bet {bet:.1f}')
    else:
        logger.info(f'{balance} after {len(outcomes)} rolls')
        show_bets(bets)


def labouchere():
    balance = 1000
    target = balance * 2
    min_balance = balance
    seq = deque([1, 2, 3])
    logger.warning(f'seq = {seq}')
    bets = []
    outcomes = []
    while balance < target:
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
            if len(seq):
                seq.pop()
        else:
            for b in range(bet):
                seq.append(1)
        logger.info(f'seq: {list(seq)[-10:]}')
        balance = update_balance(outcome, balance, bet)
        min_balance = min(balance, min_balance)
        if balance < 0:
            show_bets(bets)
            raise ValueError(f'broke after {len(outcomes)} rolls')
        if not len(seq):
            seq = deque([1, 2, 3])
    else:
        logger.info(f'{balance} after {len(outcomes)} rolls')
        show_bets(bets)
        logger.info(f'min balance: {min_balance:.0f}')


def lambert():
    balance = 1000
    min_balance = balance
    target = balance * 2
    bets = []
    outcomes = []
    bet = 1
    while balance < target:
        bets.append(bet)
        outcome = do_roll()
        outcomes.append(outcome)
        balance = update_balance(outcome, balance, bet)
        min_balance = min(balance, min_balance)
        # update bet
        if outcome:
            bet = max(bet - 1, 1)
        else:
            bet += 1
        if balance < 0:
            show_bets(bets)
            raise ValueError(f'broke after {len(outcomes)} rolls')
    else:
        logger.info(f'{balance} after {len(outcomes)} rolls')
        show_bets(bets)
        logger.info(f'min balance: {min_balance:.0f}')


if __name__ == '__main__':
    # run()
    # run_dice()
    run_reverse_dice()
    # run_martingale()
    # run_reverse_martingale()
    # labouchere()
    # lambert()
