import logging
import yaml
from generator import *
from constants import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

items_range = [0, ORDERS_COUNT]  # распаковка аргументов
items_range_red_zone = [0, RED_ZONE_ORDERS_COUNT]
items_range_green_zone = [0, GREEN_ZONE_ORDERS_COUNT]
items_range_blue_zone = [0, BLUE_ZONE_ORDERS_COUNT]

with open(r'config.yaml') as configfile:
    config = yaml.load(configfile, Loader=yaml.FullLoader)


def generate_list_id():
    return [hex(round(2000000000000 + i * 10 + sequence.__next__())) for i in range(*items_range)]


def generate_list_instrument():
    return [LIST_OF_INSTRUMENTS[round(sequence.__next__() * 10) % INSTRUMENTS_COUNT] for i in range(*items_range)]


instruments = generate_list_instrument()


def generate_list_px(list):
    result = []
    for item in list:
        if round(sequence.__next__()) % 2 == 0:
            result.append((item[0], round(item[1] + (sequence.__next__() / 1000), 8)))
        else:
            result.append((item[0], round(item[1] - (sequence.__next__() / 1000), 8)))
    print(result)
    return result


# px_init = generate_list_px(instruments)
# px_fill = generate_list_px(px_init)


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
        (initial_date + timedelta(seconds=i) + timedelta(milliseconds=sequence.__next__() * 10)).__format__(DATE_FORMAT)
        for i in range(0, time_between, time_step)
    ]


print(generate_list_dates(600, RED_ZONE_INIT_DATE, RED_ZONE_END_DATE))


def generate_list_note():
    return [LIST_OF_NOTES[round(sequence.__next__() * 10) % NOTES_COUNT] for i in range(*items_range)]


def generate_list_tag():
    return [LIST_OF_TAGS[round(sequence.__next__() * 10) % TAGS_COUNT] for i in range(*items_range)]
