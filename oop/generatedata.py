from oop.LCGenerator import LCGenerator
from oop.generators import *


class GeneratorData:
    def generate_data(self):
        return [IDGenerator.generate_value(),
                 InstrumentGenerator.generate_value(),
                 PxGenerator.generate_value(InstrumentGenerator.generate_value()),
                 PxGenerator.generate_value(PxGenerator.generate_value(InstrumentGenerator.generate_value())),
                 VolumeGenerator.generate_value(
                     [round(iter(LCGenerator.LCGenerator.get_lcg()).__next__() / 1000) for i in
                      range(*ITEMS_RANGE)]),
                 VolumeGenerator.generate_value(VolumeGenerator.generate_value(
                     [round(iter(LCGenerator.LCGenerator.get_lcg()).__next__() / 1000) for i in
                      range(*ITEMS_RANGE)])),
                 SideGenerator.generate_value(),
                 StatusGenerator.generate_value(LIST_OF_RED_ZONE_STATUS, ITEMS_RANGE_RED_ZONE) + \
                 StatusGenerator.generate_value(LIST_OF_GREEN_ZONE_STATUS, ITEMS_RANGE_GREEN_ZONE) + \
                 StatusGenerator.generate_value(LIST_OF_BLUE_ZONE_STATUS, ITEMS_RANGE_BLUE_ZONE),
                 DateGenerator.generate_value(600, RED_ZONE_INIT_DATE, RED_ZONE_END_DATE) + \
                 DateGenerator.generate_value(1200, GREEN_ZONE_INIT_DATE, GREEN_ZONE_END_DATE) + \
                 DateGenerator.generate_value(200, BLUE_ZONE_INIT_DATE, BLUE_ZONE_END_DATE),
                 NoteGenerator.generate_value(),
                 TagGenerator.generate_value()
                 ]