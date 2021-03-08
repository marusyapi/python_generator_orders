import logging
import yaml
from generator import *
from constants import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

list_id = []
list_instrument_values = []
list_instrument = []
list_px_init_values = []
list_px_init = []
list_px_fill_values = []
list_px_fill = []
list_side_values = []
list_side = []
list_status_red_values = []
list_status_red = []
list_status_green_values = []
list_status_green = []
list_status_blue_values = []
list_status_blue = []
list_note = []
list_tag = []

with open(r'config.yaml') as configfile:
    config = yaml.load(configfile, Loader=yaml.FullLoader)


def generate_list_id():
    list_id = [hex(round(2000000000000 + i * 10 + sequence.__next__())) for i in range(0, 2000)]
    print(list_id)


# def generate_list_instrument_by_lcg():
#     for item in range(NULL_RANGE, ORDERS_COUNT):
#         list_instrument_values.append(id_sequence.__next__())
#     logger.info(list_instrument_values)


def get_instrument_by_index():
    list_instrument = [LIST_OF_INSTRUMENTS[round(sequence.__next__() * 10) % INSTRUMENTS_COUNT] for i in range(0, 2000)]
    print(list_instrument)
    # list_instrument = list(map(lambda i: round(i % INSTRUMENTS_COUNT, DECIMAL_NUMBER_ROUND), list_instrument_values))
    # list_instrument_config = []

    # for i in range(NULL_RANGE, len(LIST_OF_INSTRUMENTS)):
    #     list_instrument_config.append(LIST_OF_INSTRUMENTS[i])
    # print(list_instrument_config)
    # #
    # for i in range(NULL_RANGE, len(list_instrument)):
    #     list_instrument[i] = list_instrument_config[list_instrument[i]]
    # print(list_instrument)


get_instrument_by_index()


def generate_list_px_init_by_lcg():
    for item in range(NULL_RANGE, ORDERS_COUNT):
        list_px_init_values.append(px_init_sequence.__next__())
    logger.info(list_px_init_values)


def generate_values_for_px_init():
    list_px_init = list(map(lambda i: i / DIVIDER_PX_INIT, list_px_init_values))
    print(list_px_init)
    list_px_init_config = []

    for i in range(NULL_RANGE, len(LIST_OF_INSTRUMENTS)):
        list_px_init_config.append(LIST_OF_INSTRUMENTS[i])
    print(list_px_init_config)

    # for i in range(0, len(list_px_init)):
    #     list_px_init[i] = list_px_init_config[list_px_init[i]]
    # print(list_px_init)


def generate_list_px_fill_by_lcg():
    for item in range(NULL_RANGE, ORDERS_COUNT):
        list_px_fill_values.append(px_fill_sequence.__next__())
    logger.info(list_px_fill_values)


def generate_values_for_px_fill():
    list_px_fill = list(map(lambda i: i / DIVIDER_PX_FILL, list_px_fill_values))
    print(list_px_fill)


def generate_list_side_by_lcg():
    for item in range(NULL_RANGE, ORDERS_COUNT):
        list_side_values.append(side_sequence.__next__())
    logger.info(list_side_values)


def get_side_by_index():
    list_side = list(map(lambda i: round(i / DIVIDER_SIDE), list_side_values))
    list_side_config = []

    for i in range(NULL_RANGE, len(LIST_OF_SIDES)):
        list_side_config.append(LIST_OF_SIDES[i])

    for i in range(NULL_RANGE, len(list_side)):
        list_side[i] = list_side_config[list_side[i]]
    print(list_side)


def generate_list_status_by_lcg():
    for item in range(NULL_RANGE, int(RED_ZONE_ORDERS_COUNT)):
        list_status_red_values.append(status_sequence.__next__())

    for item in range(NULL_RANGE, int(GREEN_ZONE_ORDERS_COUNT)):
        list_status_green_values.append(status_sequence.__next__())

    for item in range(NULL_RANGE, int(BLUE_ZONE_ORDERS_COUNT)):
        list_status_blue_values.append(status_sequence.__next__())

    logger.info(list_status_red_values)
    logger.info(list_status_green_values)
    logger.info(list_status_blue_values)
    # print(len(list_status_red_values), len(list_status_green_values), len(list_status_blue_values))


def convert_lcg_values_for_status():
    list_status_red = list(map(lambda i: round(i / DIVIDER_PX_FILL), list_status_red_values))
    list_status_green = list(map(lambda i: round(i / DIVIDER_PX_FILL), list_status_green_values))
    list_status_blue = list(map(lambda i: round(i / DIVIDER_PX_FILL), list_status_blue_values))
    list_status_red_config = []
    list_status_green_config = []
    list_status_blue_config = []

    for i in range(0, len(LIST_OF_RED_ZONE_STATUS)):
        list_status_red_config.append(LIST_OF_RED_ZONE_STATUS[i])

    print(list_status_red)
    print(list_status_red_config)
    print(list_status_green)
    print(list_status_blue)


# generate_list_status_by_lcg()
# convert_lcg_values_for_status()


def generate_list_note_by_lcg():
    for item in range(0, ORDERS_COUNT):
        list_note.append(note_sequence.__next__())
    logger.info(list_note)


def convert_lcg_values_for_note():
    for i in range(0, len(list_note)):
        list_note[i] = round(list_note[i] % len(config['Note']))
    print(list_note)


def generate_list_tag_by_lcg():
    for item in range(0, ORDERS_COUNT):
        list_tag.append(tag_sequence.__next__())
    logger.info(list_tag)


def convert_lcg_values_for_tag():
    for i in range(0, len(list_tag)):
        list_tag[i] = round(list_tag[i] % len(config['Tag']))
    print(list_tag)


def generate(list, sequence):
    for item in range(0, ORDERS_COUNT):
        list.append(sequence.__next__())
    print(list)


def convert(mylist, smth):
    for i in range(0, len(mylist)):
        mylist[i] = smth
    print(mylist)
