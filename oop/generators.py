from random import random

from interfaces import LCGenerator
from datetime import datetime, timedelta
import LCGenerator
from oop.constants import *


class IDGenerator(LCGenerator.LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        return hex(round(int("aefbcd1234", 16) + self.sequence.__next__() * 10 + self.sequence.__next__()))


class InstrumentGenerator(LCGenerator.LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        seq = self.sequence.__next__()
        return LIST_OF_INSTRUMENTS[round(seq * 10) % INSTRUMENTS_COUNT]


class PxGenerator(LCGenerator.LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self, **kwargs):
        px_list = kwargs.get("px")

        if type(px_list[0]) == tuple:
            px_list = list(px_list[0])

        if round(self.sequence.__next__()) % 2 == 0:
            return px_list[LEFT], round(px_list[RIGHT] + (self.sequence.__next__() / 1000), 8)
        else:
            return px_list[LEFT], round(px_list[RIGHT] - (self.sequence.__next__() / 1000), 8)


class VolumeGenerator(LCGenerator.LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):

        for item in [round(self.sequence.__next__() / 1000)]:
            if round(self.sequence.__next__()) % 2 == 0:
                return round(item + (self.sequence.__next__() * 100), 2)
            else:
                return abs(round(item - (self.sequence.__next__() * 100), 2))


class SideGenerator(LCGenerator.LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        return LIST_OF_SIDES[round(self.sequence.__next__()) % SIDES_COUNT]


class StatusGenerator(LCGenerator.LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self, **kwargs):
        status_list = kwargs.get("status_list")

        return status_list[round(self.sequence.__next__()) % len(status_list)]


class DateGenerator(LCGenerator.LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self, **kwargs):
        date_init = kwargs.get("date_init")
        date_end = kwargs.get("date_end")

        initial_date = datetime.strptime(date_init, DATE_FORMAT)
        end_date = datetime.strptime(date_end, DATE_FORMAT)
        time_between = round((end_date - initial_date).total_seconds())
        time_step = round(time_between)
        return [
            (initial_date + timedelta(seconds=i) + timedelta(milliseconds=self.sequence.__next__() * 10))
            for i in range(0, time_between, time_step)
        ]


class NoteGenerator(LCGenerator.LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        return LIST_OF_NOTES[round(self.sequence.__next__() * 10) % NOTES_COUNT]


class TagGenerator(LCGenerator.LCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        return LIST_OF_TAGS[round(self.sequence.__next__() * 10) % TAGS_COUNT]
