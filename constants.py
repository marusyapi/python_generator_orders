import logging
from pathlib import Path
import yaml


def open_config_file():
    try:
        with open(r'config.yaml') as configfile:
            config_file = yaml.load(configfile, Loader=yaml.FullLoader)
        return config_file
    except FileNotFoundError:
        logging.warning("The config file's missing")
        return Path.home() / 'config.yaml'


config = open_config_file()

CONFIG_PATH = 'config.yaml'
LOGGER_MESSAGE = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGER_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOGGER_PATH = 'logger.txt'
CSV_PATH = 'orders.csv'
SQL_CSV_PATH = 'sql.csv'
ID_INITIAL = int(config['id_initial'], 16)
ORDERS_COUNT = config['Orders']['count_orders']
ORDER_ATTRIBUTES = ["ID", "SIDE", "INSTRUMENT", "PX_INIT", "VOLUME_INIT", "DATE", "STATUS", "NOTE", "TAGS"]
SQL_ATTRIBUTES = ["QUERY"]
SQL_ORDER_ATTRIBUTES = 'ID', 'SIDE', 'INSTRUMENT', 'PX_INIT', 'VOLUME_INIT', 'DATE', 'STATUS', 'NOTE', 'TAGS'
FORMAT_DISPLAYING_ORDERS = '{:<13}{:<7}{:<13}{:<14}{:<15}{:<30}{:<17}{:<14}{:<13}'
RED_ZONE_ORDERS_COUNT = config['Orders']['ordersRed']
GREEN_ZONE_ORDERS_COUNT = config['Orders']['ordersGreen']
BLUE_ZONE_ORDERS_COUNT = config['Orders']['ordersBlue']
LIST_OF_INSTRUMENTS = list(config['Instrument']['List'].items())
INSTRUMENTS_COUNT = 11
DECIMAL_NUMBER_ROUND = 1
DIVIDER_PX_INIT = 6075
DIVIDER_PX_FILL = 7875
DIVIDER_SIDE = 7875
LIST_OF_SIDES = config['Side']
SIDES_COUNT = len(config['Side'])
DIVIDER_STATUS = 6173
LIST_OF_RED_ZONE_STATUS = list(config['Zone']['Red']['status'].values())
LIST_OF_GREEN_ZONE_STATUS = list(config['Zone']['Green']['status'].values())
LIST_OF_BLUE_ZONE_STATUS = list(config['Zone']['Blue']['status'].values())
RED_ZONE_INIT_DATE = config['Zone']['Red']['start_date']
RED_ZONE_END_DATE = config['Zone']['Red']['end_date']
GREEN_ZONE_INIT_DATE = config['Zone']['Green']['start_date']
GREEN_ZONE_END_DATE = config['Zone']['Green']['end_date']
BLUE_ZONE_INIT_DATE = config['Zone']['Blue']['start_date']
BLUE_ZONE_END_DATE = config['Zone']['Blue']['end_date']
DATE_FORMAT = config['date_format']
LIST_OF_NOTES = config['Note']
NOTES_COUNT = len(config['Note'])
LIST_OF_TAGS = config['Tag']
TAGS_COUNT = len(config['Tag'])
LEFT = 0
RIGHT = 1
