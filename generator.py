import logging
import math

import yaml

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

with open(r'config.yaml') as configfile:
    config = yaml.load(configfile, Loader=yaml.FullLoader)


# def lcg(multipler=config['LCG']['multipler'], increment=config['LCG']['increment'],
#         modulus=config['LCG']['modulus'], seed=config['LCG']['seed']):
#     current = seed
#     # increment = seed // 2
#     while True:
#         next = int((multipler * current + increment) % modulus)
#         yield next
#         current = next


def lcg(multiplier, step, max, entry):
    current = entry
    while True:
        next_entry = (current * multiplier + step) % max
        yield next_entry
        current = next_entry


sequence = iter(lcg(math.pi, math.e, 10, 1))

instrument_sequence = iter(lcg(1664525, 1013904223, 1099511627776, 299004100060))
px_init_sequence = iter(lcg(106, 1283, 6075, 237))
px_fill_sequence = iter(lcg(211, 1663, 7875, 459))
side_sequence = iter(lcg(421, 1663, 7875, 370))
volume_init_sequence = iter(lcg(2175143, 10653, 1000000, 1771875))
volume_fill_sequence = iter(lcg(936, 1399, 6655, 2531))
date_red_zone_sequence = iter(lcg(1.000000003, 1.1652, 1000, 300))
date_green_zone_sequence = iter(lcg(1.000000003, 1.145, 1000, 300))
date_blue_zone_sequence = iter(lcg(1.000000003, 1.145, 1000, 300))
status_sequence = iter(lcg(106, 1283, 6173, 237))
status_red_zone_sequence = iter(lcg(106, 1283, 6173, 237))
status_green_zone_sequence = iter(lcg(106, 1283, 6173, 732))
status_blue_zone_sequence = iter(lcg(106, 1283, 6173, 372))
note_sequence = iter(lcg(106, 1283, 6173, 372))
tag_sequence = iter(lcg(106, 1283, 10173, 372))
