from interfaces import ILCGenerator
from datetime import datetime, timedelta
from oop import LCGenerator
from oop.constants import *


class IDGenerator(ILCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        return [hex(round(int("aefbcd1234", 16) + self.sequence.__next__() * 10 + self.sequence.__next__()))]


class InstrumentGenerator(ILCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        return [LIST_OF_INSTRUMENTS[round(self.sequence.__next__() * 10) % INSTRUMENTS_COUNT]]


class PxGenerator(ILCGenerator):
    def __init__(self, px):
        self.px_list = px
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        for item in self.px_list:
            if round(self.sequence.__next__()) % 2 == 0:
                return [item[LEFT], round(item[RIGHT] + (self.sequence.__next__() / 1000), 8)]
            else:
                return [item[LEFT], round(item[RIGHT] - (self.sequence.__next__() / 1000), 8)]


class VolumeGenerator(ILCGenerator):
    def __init__(self):
        self.volume_list = [round(LCGenerator.LCGenerator.get_sequence().__next__() / 1000)]
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        for item in self.volume_list:
            if round(self.sequence.__next__()) % 2 == 0:
                return [round(item + (self.sequence.__next__() * 100), 2)]
            else:
                return [abs(round(item - (self.sequence.__next__() * 100), 2))]


class SideGenerator(ILCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        return [LIST_OF_SIDES[round(self.sequence.__next__()) % SIDES_COUNT]]


class StatusGenerator(ILCGenerator):
    def __init__(self, status_list):
        self.status_list = status_list
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        return [self.status_list[round(self.sequence.__next__()) % len(self.status_list)]]


class DateGenerator(ILCGenerator):
    def __init__(self, init_date, end_date):
        self.init_date = init_date
        self.end_date = end_date
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        initial_date = datetime.strptime(self.init_date, DATE_FORMAT)
        end_date = datetime.strptime(self.end_date, DATE_FORMAT)
        time_between = round((end_date - initial_date).total_seconds())
        time_step = round(time_between)
        return [
            (initial_date + timedelta(seconds=i) + timedelta(milliseconds=self.sequence.__next__() * 10))
            for i in range(0, time_between, time_step)
        ]


class NoteGenerator(ILCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        return [LIST_OF_NOTES[round(self.sequence.__next__() * 10) % NOTES_COUNT]]


class TagGenerator(ILCGenerator):
    def __init__(self):
        self.sequence = LCGenerator.LCGenerator.get_sequence()

    def generate_value(self):
        return [LIST_OF_TAGS[round(self.sequence.__next__() * 10) % TAGS_COUNT]]
