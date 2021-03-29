from datetime import timedelta

from oop.LCGenerator import LCGenerator
from oop.constants import ITEMS_RANGE, RIGHT, DATE_FORMAT, LEFT
from oop.generatedata import GeneratorData
from oop.orderbuilder import OrderBuilder


class OrderList:
    def __init__(self):
        self.orders = []

    def populate_list(self) -> list:
        data = GeneratorData()
        for i in data.generate_data():
            order_builder = OrderBuilder()
            order = order_builder.build()
            time_delta = timedelta(milliseconds=0)

            for status in order.obj_status[i]:
                date = order.obj_date[i] + time_delta
                print(date)
                if status == 'cancel':
                    order.obj_px_init[i][RIGHT] = volume = 0
                if status == 'partially fill':
                    order.obj_px_init[i][RIGHT], volume = order.obj_px_fill[i][RIGHT], order.obj_volume_fill[i]
                else:
                    order.obj_px_init[i][RIGHT], volume = order.obj_px_init[i][RIGHT], order.obj_volume_init[i]
                self.orders.append(
                    [order.obj_id[i], order.obj_side[i], order.obj_px_init[i][LEFT], order.obj_px_init[i][RIGHT], volume,
                     date.__format__(DATE_FORMAT),
                     status,
                     order.obj_note[i], order.obj_tag[i]])
                time_delta += timedelta(milliseconds=iter(LCGenerator.get_lcg()).__next__() * 10)
        return self.orders
