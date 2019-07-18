from keras.layers import Flatten, Dense, Activation
from loguru import logger
from rl.agents import SARSAAgent
from keras.models import Sequential


class UfcEnv:
    observation_space = 20


def main():

    model = Sequential()
    model.add(Flatten(input_shape=(1, UfcEnv.observation_space)))
    model.add(Dense(UfcEnv.observation_space))
    model.add(Activation('relu'))
    model.add(Dense(UfcEnv.observation_space))
    model.add(Activation('relu'))
    model.add(Dense(UfcEnv.observation_space))
    model.add(Activation('softmax'))
    print(model.summary())

    # agent = SARSAAgent()
    logger.info('Done')


if __name__ == '__main__':
    main()
