import yaml


with open(r'config.yaml') as configfile:
    config = yaml.load(configfile, Loader=yaml.FullLoader)

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
DIVIDER_STATUS = 6173
LIST_OF_RED_ZONE_STATUS = config['Zone']['Red']['status']
LIST_OF_GREEN_ZONE_STATUS = config['Zone']['Green']['status']
LIST_OF_BLUE_ZONE_STATUS = config['Zone']['Blue']['status']