from generator import *


def init():
    pass


def setup():
    pass


def workflow():
    pass


def out():
    pass


if __name__ == '__main__':
    try:
        init()
        setup()
        workflow()
        out()
    except Exception as e:
        logger.error(e)
