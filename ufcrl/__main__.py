from typing import List

from keras.layers import Flatten, Dense, Activation
from keras.optimizers import Adam
from loguru import logger
from keras.models import Sequential
from rl.agents import SARSAAgent
from rl.core import Env
from rl.policy import BoltzmannQPolicy


class MyEnv(Env):

    def __init__(self):
        self._reset()

    def _reset(self) -> None:
        self.i = 0
        self.balance = 100

    def _get_obs(self) -> List[float]:
        return [1] * 20

    def reset(self) -> List[float]:
        self._reset()
        return self._get_obs()

    # def render(self, mode='human', close=False):
    #     pass

    def close(self):
        pass

    # def seed(self, seed=None):
    #     pass

    # def configure(self, *args, **kwargs):
    #     pass

    # def step(self, action):
    #     pass


def main():

    model = Sequential()
    model.add(Dense(units=20, activation='relu', input_shape=(1, 20)))
    model.add(Dense(units=10, activation='softmax'))
    logger.info(model.summary())

    policy = BoltzmannQPolicy()
    agent = SARSAAgent(model=model, nb_actions=10, policy=policy)

    optimizer = Adam(lr=1e-3)
    agent.compile(optimizer, metrics=['mae'])

    env = MyEnv()
    agent.fit(env, 1, verbose=2, visualize=True)

    agent.save_weights('sarsa_wegihts.h5f', overwrite=True)

    logger.info('Done')


if __name__ == '__main__':
    main()
