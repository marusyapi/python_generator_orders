import yaml


with open(r'config.yaml') as configfile:
    config = yaml.load(configfile, Loader=yaml.FullLoader)

ID_INITIAL = int(config['id_initial'], 16)
ORDERS_COUNT = config['Orders']['count_orders']
RED_ZONE_ORDERS_COUNT = config['Orders']['ordersRed']
GREEN_ZONE_ORDERS_COUNT = config['Orders']['ordersGreen']
BLUE_ZONE_ORDERS_COUNT = config['Orders']['ordersBlue']
LIST_OF_INSTRUMENTS = list(config['Instrument']['List'].items())
INSTRUMENTS_COUNT = 11
NULL_RANGE = 0
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