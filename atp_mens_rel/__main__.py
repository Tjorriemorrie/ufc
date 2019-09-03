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

from .data_2019_07 import DATA_2019_07


class ATPEnv(Env):
    ACTIONS = [
        'No bet',
        'Bet x1',
        'Bet x2',
        'Bet x4',
    ]

    def __init__(self):
        self._load_data()

    def _load_data(self):
        self.x_train = []
        self.y_train = []
        self.x_test = []
        self.y_test = []

        all_data = DATA_2019_07
        cutoff = len(all_data) * 0.90

        # ratings = defaultdict(lambda: Rating())

        for i, competition in enumerate(all_data):
            for match in competition['matches']:
                # skip if missing data:
                if 'odds' not in match or 'score' not in match:
                    continue

                p1, p2 = match['players']

                # odds
                p1_odds = match['odds'][p1]
                p2_odds = match['odds'][p2]

                x = [
                    1 / p1_odds,
                    1 / p2_odds,
                ]

                # y is the data to calculate the reward
                y = [p1_odds, p2_odds]

                # flip item if upset: p1 (the winner), was not the favourite
                is_win_1 = 1
                if p1_odds > p2_odds:
                    is_win_1 = 0
                    x = x[::-1]
                    y = y[::-1]

                # add non-pair data
                y.append(is_win_1)

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
        if self.x_test:
            self.x_test = scaler.transform(self.x_test)

    def _reset(self) -> None:
        self.i = 0
        self.rewards = []

    def _get_obs(self) -> List[float]:
        obs = self.x_train[self.i]
        return np.array(obs)

    def reset(self) -> List[float]:
        self._reset()
        return self._get_obs()

    def step(self, action) -> Tuple[Optional[List[float]], float, bool, dict]:
        multi_map = {
            0: 0,
            1: 1,
            2: 2,
            3: 4,
        }
        p1_odds, p2_odds, is_win_1 = self.y_train[self.i]
        bet = multi_map[action]

        # deduct bet
        reward = -bet

        # won with first fighter
        if is_win_1:
            reward += p1_odds * bet

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
    num_actions = len(ATPEnv.ACTIONS)
    model = Sequential()
    model.add(Flatten(input_shape=(1, 2)))
    model.add(Dense(units=2, activation='relu'))
    # model.add(Dense(units=20, activation='relu'))
    model.add(Dense(units=num_actions, activation='linear'))
    logger.info(model.summary())

    steps = 1E9
    interval = steps // 100

    # policy = MyPolicy()
    policy = BoltzmannQPolicy()
    agent = SARSAAgent(model=model, nb_actions=num_actions, policy=policy,
                       train_interval=10, nb_steps_warmup=10)

    adam = Adam()
    sgd = SGD(lr=1e-3, momentum=0, decay=0, nesterov=False)
    agent.compile(optimizer=adam, metrics=['mse'])

    env = ATPEnv()
    agent.fit(env, steps, verbose=2, visualize=True)

    fp = Path(__file__).resolve().parent / 'sarsa_weights.h5f'
    agent.save_weights(fp, overwrite=True)

    logger.info('Done')


if __name__ == '__main__':
    main()
