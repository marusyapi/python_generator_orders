from random import random

from interfaces import LCGenerator
from datetime import datetime, timedelta
from LCGenerator import LCGenerator
from oop.constants import *


class IDGenerator(LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.get_sequence()
        self.current = 0

    def generate_value(self):
        self.current += round(int("aefbcd1234", 16) + self.sequence.__next__() * 10 + self.sequence.__next__())
        return hex(self.current)


class InstrumentGenerator(LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.get_sequence()

    def generate_value(self):
        seq = self.sequence.__next__()
        instrument_px_list = list(INSTRUMENT_PX_DICT.items())
        return instrument_px_list[round(seq * 10) % INSTRUMENTS_COUNT][0]


class PxGenerator(LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.get_sequence()

    def generate_value(self, **kwargs):
        instrument = kwargs.get("instrument")
        instrument = INSTRUMENT_PX_DICT.get(instrument)
        if round(self.sequence.__next__()) % 2 == 0:
            return round(instrument + (self.sequence.__next__() / 1000), 8)
        else:
            return round(instrument - (self.sequence.__next__() / 1000), 8)


class VolumeGenerator(LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.get_sequence()

    def generate_value(self):

        for item in [round(self.sequence.__next__() / 1000)]:
            if round(self.sequence.__next__()) % 2 == 0:
                return round(item + (self.sequence.__next__() * 100), 2)
            else:
                return abs(round(item - (self.sequence.__next__() * 100), 2))


class SideGenerator(LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.get_sequence()

    def generate_value(self):
        return LIST_OF_SIDES[round(self.sequence.__next__()) % SIDES_COUNT]


class StatusGenerator(LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.get_sequence()

    def generate_value(self, **kwargs):
        status_list = kwargs.get("status_list")

        return status_list[round(self.sequence.__next__()) % len(status_list)]


class DateGenerator(LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.get_sequence()
        self.current = 0

    def generate_value(self, **kwargs):
        date_init = kwargs.get("date_init")
        date_end = kwargs.get("date_end")

        initial_date = datetime.strptime(date_init, DATE_FORMAT)
        end_date = datetime.strptime(date_end, DATE_FORMAT)
        time_between = (end_date - initial_date).total_seconds()
        time_step = time_between + self.sequence.__next__() * 10

        milliseconds = timedelta(milliseconds=time_step)
        self.current = initial_date + milliseconds

        return self.current


class NoteGenerator(LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.get_sequence()

    def generate_value(self):
        return LIST_OF_NOTES[round(self.sequence.__next__() * 10) % NOTES_COUNT]


class TagGenerator(LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.get_sequence()

    def generate_value(self):
        return LIST_OF_TAGS[round(self.sequence.__next__() * 10) % TAGS_COUNT]


id_generator = IDGenerator()
instrument_generator = InstrumentGenerator()
px_generator = PxGenerator()
volume_generator = VolumeGenerator()
side_generator = SideGenerator()
status_generator = StatusGenerator()
date_generator = DateGenerator()
note_generator = NoteGenerator()
tag_generator = TagGenerator()
