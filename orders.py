from datetime import datetime, timedelta

from generator import *
from constants import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

items_range = [0, ORDERS_COUNT]
items_range_red_zone = [0, RED_ZONE_ORDERS_COUNT]
items_range_green_zone = [0, GREEN_ZONE_ORDERS_COUNT]
items_range_blue_zone = [0, BLUE_ZONE_ORDERS_COUNT]

with open(r'config.yaml') as configfile:
    config = yaml.load(configfile, Loader=yaml.FullLoader)


def generate_list_id():
    return [hex(round(ID_INITIAL + i * 10 + sequence.__next__())) for i in range(*items_range)]


def generate_list_instrument():
    return [LIST_OF_INSTRUMENTS[round(sequence.__next__() * 10) % INSTRUMENTS_COUNT] for i in range(*items_range)]


def generate_list_px(list):
    result = []
    for item in list:
        if round(sequence.__next__()) % 2 == 0:
            result.append([item[0], round(item[1] + (sequence.__next__() / 1000), 8)])
        else:
            result.append([item[0], round(item[1] - (sequence.__next__() / 1000), 8)])
    return result


def generate_list_volume(list):
    result = []
    for item in list:
        if round(sequence.__next__()) % 2 == 0:
            result.append(round(item + (sequence.__next__() * 100), 2))
        else:
            result.append(abs(round(item - (sequence.__next__() * 100), 2)))
    return result


def generate_list_side():
    return [LIST_OF_SIDES[round(sequence.__next__()) % SIDES_COUNT] for i in range(*items_range)]


def generate_list_status(status_list, total_range):
    return [status_list[round(sequence.__next__()) % len(status_list)] for i in range(*total_range)]


def generate_list_dates(total_range, init_date, end_date):
    initial_date = datetime.strptime(init_date, DATE_FORMAT)
    end_date = datetime.strptime(end_date, DATE_FORMAT)
    time_between = round((end_date - initial_date).total_seconds())
    time_step = round(time_between / total_range)
    return [
        (initial_date + timedelta(seconds=i) + timedelta(milliseconds=sequence.__next__() * 10))
        for i in range(0, time_between, time_step)
    ]


def generate_list_note():
    return [LIST_OF_NOTES[round(sequence.__next__() * 10) % NOTES_COUNT] for i in range(*items_range)]


def generate_list_tag():
    return [LIST_OF_TAGS[round(sequence.__next__() * 10) % TAGS_COUNT] for i in range(*items_range)]


def build_orders():
    ids = generate_list_id()
    px_inits = generate_list_px(generate_list_instrument())
    px_fills = generate_list_px(px_inits)
    volume_inits = generate_list_volume([round(sequence.__next__() / 1000) for i in range(*items_range)])
    volume_fills = generate_list_volume(volume_inits)
    sides = generate_list_side()
    statuses = generate_list_status(LIST_OF_RED_ZONE_STATUS, items_range_red_zone) + \
               generate_list_status(LIST_OF_GREEN_ZONE_STATUS, items_range_green_zone) + \
               generate_list_status(LIST_OF_BLUE_ZONE_STATUS, items_range_blue_zone)
    dates = generate_list_dates(600, RED_ZONE_INIT_DATE, RED_ZONE_END_DATE) + \
            generate_list_dates(1200, GREEN_ZONE_INIT_DATE, GREEN_ZONE_END_DATE) + \
            generate_list_dates(200, BLUE_ZONE_INIT_DATE, BLUE_ZONE_END_DATE)
    notes = generate_list_note()
    tags = generate_list_tag()
    orders = []

    for i in range(*items_range):
        time_delta = timedelta(milliseconds=0)
        for status in statuses[i]:
            date = dates[i] + time_delta
            if status == 'cancel':
                px_inits[i][1] = volume = 0
            if status == 'partially fill':
                px_inits[i][1], volume = px_fills[i][1], volume_fills[i]
            else:
                px_inits[i][1], volume = px_inits[i][1], volume_inits[i]
            orders.append(
                [ids[i], sides[i], px_inits[i][0], px_inits[i][1], volume, date.__format__(DATE_FORMAT), status,
                 notes[i], tags[i]])
            time_delta += timedelta(milliseconds=sequence.__next__() * 10)
    print(orders)


build_orders()