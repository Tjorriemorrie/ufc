from collections import defaultdict
from itertools import chain
from pathlib import Path
from typing import List, Optional, Tuple

from keras.layers import Flatten, Dense, Activation, np
from keras.losses import mean_squared_error
from keras.optimizers import Adam
from loguru import logger
from keras.models import Sequential
from math import sqrt
from rl.agents import SARSAAgent
from rl.core import Env
from rl.policy import BoltzmannQPolicy, Policy
from trueskill import BETA, global_env, Rating, rate_1vs1

from .data import DATA


def win_probability(team1, team2):
    delta_mu = sum(r.mu for r in team1) - sum(r.mu for r in team2)
    sum_sigma = sum(r.sigma ** 2 for r in chain(team1, team2))
    size = len(team1) + len(team2)
    denom = sqrt(size * (BETA * BETA) + sum_sigma)
    ts = global_env()
    return ts.cdf(delta_mu / denom)


class MyPolicy(Policy):

    def select_action(self, **kwargs):
        q_values = kwargs['q_values']
        # select per fight
        pair_q_values = []
        for q1, q2 in zip(*[iter(q_values)]*2):
            pair_q_values.append(q1 if q1 >= q2 else 0)
            pair_q_values.append(q2 if q2 > q1 else 0)
        # scale to pool
        norm_q_values = []
        for q in pair_q_values:
            norm_q_values.append(q / sum(pair_q_values))
        return norm_q_values


class MyEnv(Env):

    def __init__(self):
        self._load_data()
        self._reset()

    def _load_data(self):
        self.x_train = []
        self.y_train = []
        self.x_test = []
        self.y_test = []
        ratings = defaultdict(lambda: Rating())
        cutoff = int(len(DATA) * 0.7)
        for i, scene in enumerate(DATA):
            if len(scene['fights']) < 10:
                continue
            x = []
            y = []
            for fight in reversed(scene['fights']):
                # skip if no odds:
                if 'odds' not in fight:
                    continue

                f1 = fight['fighters'][0]['name']
                f2 = fight['fighters'][1]['name']

                f1_odds = fight['odds'][f1]
                f2_odds = fight['odds'][f2]
                if not -50 < f1_odds < 50 or not -50 < f2_odds < 50:
                    raise ValueError(f'surely these odds are wrong? {f1_odds} {f2_odds}')

                win1_prob = win_probability([ratings[f1]], [ratings[f2]])
                win2_prob = win_probability([ratings[f2]], [ratings[f1]])

                # get winner
                fw = fight['winner']['fighter']
                is_win_1 = fw == f1
                fl = f2 if is_win_1 else f1
                if not is_win_1 and fw != f2 and fw is not None:
                    raise ValueError(f'unknown winner {fw}')
                drawn = fw is None

                x.extend([
                    1 / f1_odds,
                    1 / f2_odds,
                    win1_prob,
                    win2_prob,
                ])

                y.extend([
                    fight['odds'][f1] if is_win_1 else 0,
                    fight['odds'][f2] if not is_win_1 else 0,
                ])

                # update ratings
                ratings[fw], ratings[fl] = rate_1vs1(ratings[fw], ratings[fl], drawn=drawn)

                if len(x) == 40:
                    break

            # add data and results for rewards
            if i < cutoff:
                self.x_train.append(x)
                self.y_train.append(y)
            else:
                self.x_test.append(x)
                self.y_test.append(y)

    def _reset(self) -> None:
        self.i = 0
        self.balance = 1000

    def _get_obs(self) -> List[float]:
        obs = self.x_train[self.i]
        assert len(obs) == 40
        return obs

    def reset(self) -> List[float]:
        self._reset()
        return self._get_obs()

    def step(self, action) -> Tuple[Optional[List[float]], float, bool, dict]:
        odds = self.y_train[self.i]
        bet_amt = max(self.balance, 200) / 100
        reward = -bet_amt * 10
        reward += sum([b * o * bet_amt for b, o in zip(action, odds)])
        self.balance += reward

        game_over = self.balance <= 0

        self.i += 1
        obs = self._get_obs()

        info = {}

        return obs, reward, game_over, info

    def close(self):
        pass

    def render(self, mode='human', close=False):
        logger.info(f'Trained on scene {self.i-1}, balance: ${self.balance-1000:.0f}')

    # def seed(self, seed=None):
    #     pass

    # def configure(self, *args, **kwargs):
    #     pass


def load_data():
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    ratings = defaultdict(lambda: Rating())
    cutoff = int(len(DATA) * 0.7)
    for i, scene in enumerate(DATA):
        if len(scene['fights']) < 10:
            continue
        x = []
        y = []
        for fight in reversed(scene['fights']):
            # skip if no odds:
            if 'odds' not in fight:
                continue

            f1 = fight['fighters'][0]['name']
            f2 = fight['fighters'][1]['name']

            f1_odds = fight['odds'][f1]
            f2_odds = fight['odds'][f2]
            if not -50 < f1_odds < 50 or not -50 < f2_odds < 50:
                raise ValueError(f'surely these odds are wrong? {f1_odds} {f2_odds}')

            win1_prob = win_probability([ratings[f1]], [ratings[f2]])
            win2_prob = win_probability([ratings[f2]], [ratings[f1]])

            # get winner
            fw = fight['winner']['fighter']
            is_win_1 = fw == f1
            fl = f2 if is_win_1 else f1
            if not is_win_1 and fw != f2 and fw is not None:
                raise ValueError(f'unknown winner {fw}')
            drawn = fw is None

            x.extend([
                1 / f1_odds,
                1 / f2_odds,
                win1_prob,
                win2_prob,
            ])

            y.extend([
                fight['odds'][f1] if is_win_1 else 0,
                fight['odds'][f2] if not is_win_1 else 0,
            ])

            # update ratings
            ratings[fw], ratings[fl] = rate_1vs1(ratings[fw], ratings[fl], drawn=drawn)

            if len(x) == 40:
                break

        # add data and results for rewards
        if i < cutoff:
            x_train.append(x)
            y_train.append(y)
        else:
            x_test.append(x)
            y_test.append(y)

    return np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)


def main():

    x_train, y_train, x_test, y_test = load_data()

    model = Sequential()
    model.add(Dense(units=40, activation='relu', input_dim=40))
    model.add(Dense(units=40, activation='relu'))
    model.add(Dense(units=10, activation='softmax'))
    logger.info(print(model.summary()))

    optimizer = Adam(lr=1e-3)
    model.compile(optimizer, loss=mean_squared_error)

    model.fit(x_train, y_train)

    score = model.evaluate(x_test, y_test)
    logger.info(f'Model score {score:.2f}')

    logger.info('Done')


if __name__ == '__main__':
    main()
