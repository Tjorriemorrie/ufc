from collections import defaultdict
from itertools import chain
from pathlib import Path
from typing import List, Optional, Tuple
import numpy as np
from keras.layers import Flatten, Dense, Activation
from keras.optimizers import Adam, SGD
from loguru import logger
from keras.models import Sequential
from math import sqrt
from rl.agents import SARSAAgent
from rl.core import Env
from rl.policy import BoltzmannQPolicy, Policy
from sklearn.preprocessing import MinMaxScaler
from trueskill import BETA, global_env, Rating, rate_1vs1

from .data_2016 import DATA_2016
from .data_2017 import DATA_2017
from .data_2018 import DATA_2018
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
        return np.array(norm_q_values)


class MyEnv(Env):
    ACTIONS = [
        'Bet f1 *1',
        'Bet f2 *1',
        'Bet f1 *2',
        'Bet f2 *2',
        'Bet f1 *4',
        'Bet f2 *4',
    ]

    def __init__(self):
        self._load_data()

    def _load_data(self):
        self.x_train = []
        self.y_train = []
        self.x_test = []
        self.y_test = []
        ratings = defaultdict(lambda: Rating())
        all_data = DATA_2016 + DATA_2017 + DATA_2018 + DATA
        cutoff = int(len(all_data) * 0.90)
        for i, scene in enumerate(all_data):
            for fight in scene['fights']:
                # skip if no odds:
                if 'odds' not in fight or 'winner' not in fight:
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

                x = [
                    win1_prob,
                    f1_odds,
                    f2_odds,
                    ratings[f1].mu,
                    ratings[f2].mu,
                    ratings[f1].sigma,
                    ratings[f2].sigma,
                ]

                # y is the data to calculate the reward
                y = [is_win_1, fight['odds'][f1], fight['odds'][f2]]

                # update ratings
                ratings[fw], ratings[fl] = rate_1vs1(ratings[fw], ratings[fl], drawn=drawn)

                # add data and results for rewards
                if i < cutoff:
                    self.x_train.append(x)
                    self.y_train.append(y)
                else:
                    self.x_test.append(x)
                    self.y_test.append(y)

        # scale data
        scaler = MinMaxScaler()
        scaler.partial_fit(self.x_train)
        self.x_train = scaler.transform(self.x_train)
        self.x_test = scaler.transform(self.x_test)

    def _reset(self) -> None:
        self.i = 0
        self.rewards = []

    def _get_obs(self) -> List[float]:
        obs = self.x_train[self.i]
        assert len(obs) == 7
        return np.array(obs)

    def reset(self) -> List[float]:
        self._reset()
        return self._get_obs()

    def step(self, action) -> Tuple[Optional[List[float]], float, bool, dict]:
        # bet_size = max(sum(self.rewards), 200) // 20
        is_win_1, f1_odds, f2_odds = self.y_train[self.i]
        multi = 1 if action < 2 else 2 if action < 4 else 4
        bet_size = 5 * multi

        # deduct bet
        reward = -bet_size

        # won with first fighter
        if is_win_1 and action % 2 == 0:
            reward += f1_odds * bet_size

        # won with second fighter
        elif not is_win_1 and action % 2 != 0:
            reward += f2_odds * bet_size

        # reward = -reward
        self.rewards.append(reward)

        self.i += 1

        game_over = self.i == len(self.x_train) - 1

        obs = self._get_obs()

        info = {}

        return obs, reward, game_over, info

    def close(self):
        pass

    def render(self, mode='human', close=False):
        # logger.info(f'Trained on scene {self.i-1} [{self.i/len(self.x_train)*100:.0f}% done], balance: ${sum(self.rewards):.0f}')
        pass

    # def seed(self, seed=None):
    #     pass

    # def configure(self, *args, **kwargs):
    #     pass


def main():

    model = Sequential()
    model.add(Flatten(input_shape=(1, 7)))
    model.add(Dense(units=20, activation='relu'))
    model.add(Dense(units=20, activation='relu'))
    model.add(Dense(units=6, activation='linear'))
    logger.info(model.summary())

    steps = 1E9
    interval = steps // 100

    # policy = MyPolicy()
    policy = BoltzmannQPolicy()
    agent = SARSAAgent(model=model, nb_actions=6, policy=policy, train_interval=10, nb_steps_warmup=10)

    adam = Adam()
    sgd = SGD(lr=1e-3, momentum=0, decay=0, nesterov=False)
    agent.compile(optimizer=adam, metrics=['mse'])

    env = MyEnv()
    agent.fit(env, steps, verbose=2, visualize=True)

    fp = Path(__file__).resolve().parent / 'sarsa_weights.h5f'
    agent.save_weights(fp, overwrite=True)

    logger.info('Done')


if __name__ == '__main__':
    main()
