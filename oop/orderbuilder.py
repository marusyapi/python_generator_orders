from dataclasses import dataclass

from oop.generators import *
from oop.interfaces import Builder
from datetime import datetime
import copy


class OrderBuilder(Builder):
    def build(self):
        orders = []

        for item in ITEMS_RANGE:
            if item < 600:
                status_zone = LIST_OF_RED_ZONE_STATUS
                date_init_zone = RED_ZONE_INIT_DATE
                date_fill_zone = RED_ZONE_END_DATE
            elif 600 <= item < 1800:
                status_zone = LIST_OF_GREEN_ZONE_STATUS
                date_init_zone = GREEN_ZONE_INIT_DATE
                date_fill_zone = GREEN_ZONE_END_DATE
            elif 1800 <= item < 2000:
                status_zone = LIST_OF_BLUE_ZONE_STATUS
                date_init_zone = BLUE_ZONE_INIT_DATE
                date_fill_zone = BLUE_ZONE_END_DATE

            instrument = copy.deepcopy(instrument_generator.generate_value())
            volume_init = copy.deepcopy(volume_init_generator.generate_value())
            volume_fill = copy.deepcopy(volume_fill_generator.generate_value())
            px_init = px_init_value.generate_value(px=instrument)
            px_fill = copy.deepcopy(px_fill_value.generate_value(px=px_init))

            order_main = Order(
                id_generator.generate_value(),
                instrument[0],
                px_init[1],
                px_fill[1],
                volume_init,
                volume_fill,
                side_generator.generate_value(),
                '',
                datetime.now(),
                note_generator.generate_value(),
                tag_generator.generate_value()
            )

            for status in status_generator.generate_value(status_list=status_zone):
                order = copy.copy(order_main)
                order.px_fill = None
                order.volume_init = None
                order.volume_fill = None
                order.status = status
                order.date = datetime.now()

                for date in date_generator.generate_value(date_init=date_init_zone, date_end=date_fill_zone):
                    if status == 'cancel':
                        px_init = volume_fill = 0
                    if status == 'partially fill':
                        volume_fill = px_fill
                    else:
                        volume_fill = px_init

                    order_copy = copy.copy(order)
                    order_copy.px_fill = px_fill
                    order_copy.volume_init = volume_init
                    order_copy.volume_fill = volume_fill
                    order_copy.status = status
                    order_copy.date = date.__format__(DATE_FORMAT)

                    orders.append(order_copy)

        return orders


class Order:
    def __init__(self,
                 obj_id: str,
                 obj_instrument: str,
                 obj_px_init: float,
                 obj_px_fill,
                 obj_volume_init,
                 obj_volume_fill,
                 obj_side,
                 obj_status: list,
                 obj_date,
                 obj_note,
                 obj_tag):
        self.obj_id = obj_id
        self.obj_instrument = obj_instrument
        self.obj_px_init = obj_px_init
        self.obj_px_fill = obj_px_fill
        self.obj_volume_init = obj_volume_init
        self.obj_volume_fill = obj_volume_fill
        self.obj_side = obj_side
        self.obj_status = obj_status
        self.obj_date = obj_date
        self.obj_note = obj_note
        self.obj_tag = obj_tag
