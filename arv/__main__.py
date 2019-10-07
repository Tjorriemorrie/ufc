from loguru import logger


ORIGIN = {
    'natural',
    'manmade'
}

AESTHETIC_IMPACT = {
    'happy',
    'sad',
    'surprise',
    'anger',
    # fear, disgust, nervous, tired, bored, dizzy, peaceful, shocked
}

COLOURS = {
    'red',
    'yellow',
    'blue',
    'brown',
    'orange',
    'green',
    'purple',
    'transparent',
}

TEMPERATURES = {
    'cold/cool',
    'hot/warm',
    'humid',
    'arid',
    'room',
}

TEXTURES = {
    'glass',
    'feathery',
    'hairy',
    'leathery',
    'metallic',
    'prickly',
    'rubbery',
    'sandy',
    'silky',
    'wooden',
    'wet',
    'smooth',
    'rough',
}

SOUNDS = {
    'humming',
    'jingling',
    'rumbling',
    'squeking',
    'metallic',
    'buzzing',
    'quiet',
    'voices',
}

DIMENSIONS = {
    'angular',
    'big',
    'cylindrical/circle',
    'flat',
    'pointed',
    'rectangular',
    'wavy',
}
SMELL = {
    'bitter',
    'chemical',
    'fresh',
    'metallic',
    'salty',
    'sour',
    'stony',
    'sweet',
    'wooden',
}

def generator():
    logger.info('generating')

    logger.info('done')


if __name__ == '__main__':
    generator()
