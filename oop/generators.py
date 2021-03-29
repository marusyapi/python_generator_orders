from interfaces import ILCGenerator
from datetime import datetime, timedelta
from oop import LCGenerator
from oop.constants import *


class IDGenerator(ILCGenerator):
    def __init__(self):
        pass

    @staticmethod
    def generate_value():
        sequence = iter(LCGenerator.LCGenerator.get_lcg())
        return [hex(round(int("aefbcd1234", 16) + i * 10 + sequence.__next__())) for i in range(*ITEMS_RANGE)]


class InstrumentGenerator(ILCGenerator):
    def __init__(self):
        pass

    @staticmethod
    def generate_value():
        sequence = iter(LCGenerator.LCGenerator.get_lcg())
        return [LIST_OF_INSTRUMENTS[round(sequence.__next__() * 10) % INSTRUMENTS_COUNT] for i in range(*ITEMS_RANGE)]


class PxGenerator(ILCGenerator):
    def __init__(self, px):
        self.pxlist = px

    @staticmethod
    def generate_value(pxlist):
        sequence = iter(LCGenerator.LCGenerator.get_lcg())
        result = []
        for item in pxlist:
            if round(sequence.__next__()) % 2 == 0:
                result.append([item[LEFT], round(item[RIGHT] + (sequence.__next__() / 1000), 8)])
            else:
                result.append([item[LEFT], round(item[RIGHT] - (sequence.__next__() / 1000), 8)])
        return result


class VolumeGenerator(ILCGenerator):
    def __init__(self, volume):
        self.volumelist = volume

    @staticmethod
    def generate_value(volumelist):
        sequence = iter(LCGenerator.LCGenerator.get_lcg())
        result = []
        for item in volumelist:
            if round(sequence.__next__()) % 2 == 0:
                result.append(round(item + (sequence.__next__() * 100), 2))
            else:
                result.append(abs(round(item - (sequence.__next__() * 100), 2)))
        return result


class SideGenerator(ILCGenerator):
    def __init__(self):
        pass

    @staticmethod
    def generate_value():
        sequence = iter(LCGenerator.LCGenerator.get_lcg())
        return [LIST_OF_SIDES[round(sequence.__next__()) % SIDES_COUNT] for i in range(*ITEMS_RANGE)]


class StatusGenerator(ILCGenerator):
    def __init__(self, status_list, total_range):
        self.status_list = status_list
        self.total_range = total_range

    @staticmethod
    def generate_value(status_list, total_range):
        sequence = iter(LCGenerator.LCGenerator.get_lcg())
        return [status_list[round(sequence.__next__()) % len(status_list)] for i in range(*total_range)]


class DateGenerator(ILCGenerator):
    def __init__(self, total_range, init_date, end_date):
        self.total_range = total_range
        self.init_date = init_date
        self.end_date = end_date

    @staticmethod
    def generate_value(total_range, init_date, end_date):
        sequence = iter(LCGenerator.LCGenerator.get_lcg())
        initial_date = datetime.strptime(init_date, DATE_FORMAT)
        end_date = datetime.strptime(end_date, DATE_FORMAT)
        time_between = round((end_date - initial_date).total_seconds())
        time_step = round(time_between / total_range)
        return [
            (initial_date + timedelta(seconds=i) + timedelta(milliseconds=sequence.__next__() * 10))
            for i in range(0, time_between, time_step)
        ]


class NoteGenerator(ILCGenerator):
    def __init__(self):
        pass

    @staticmethod
    def generate_value():
        sequence = iter(LCGenerator.LCGenerator.get_lcg())
        return [LIST_OF_NOTES[round(sequence.__next__() * 10) % NOTES_COUNT] for i in range(*ITEMS_RANGE)]


class TagGenerator(ILCGenerator):
    def __init__(self):
        pass

    @staticmethod
    def generate_value():
        sequence = iter(LCGenerator.LCGenerator.get_lcg())
        return [LIST_OF_TAGS[round(sequence.__next__() * 10) % TAGS_COUNT] for i in range(*ITEMS_RANGE)]
