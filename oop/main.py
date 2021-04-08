import copy

from oop.CSVStorage import CSVStorage
from oop.DBStorage import DBStorage
from oop.generators import *
from oop.interfaces import Director
from oop.orderbuilder import OrderBuilder

orders = []


class Main:
    @staticmethod
    def workflow():
        director = Director()
        director.builder = OrderBuilder()

        for item in ITEMS_RANGE:
            if item < 600:
                status_zone = LIST_OF_RED_ZONE_STATUS
                date_init_zone = RED_ZONE_INIT_DATE
                date_end_zone = RED_ZONE_END_DATE
            elif 600 <= item < 1800:
                status_zone = LIST_OF_GREEN_ZONE_STATUS
                date_init_zone = GREEN_ZONE_INIT_DATE
                date_end_zone = GREEN_ZONE_END_DATE
            elif 1800 <= item < 2000:
                status_zone = LIST_OF_BLUE_ZONE_STATUS
                date_init_zone = BLUE_ZONE_INIT_DATE
                date_end_zone = BLUE_ZONE_END_DATE

            order_main = director.builder.build()

            order_main.date = date_generator.generate_value(date_init=date_init_zone, date_end=date_end_zone)

            for status in status_generator.generate_value(status_list=status_zone):

                order = copy.copy(order_main)

                if status == 'partially fill':
                    order.px_fill = order.px_init
                    order.volume_fill = order.volume_init - (next(LCGenerator.get_sequence()) % order.volume_init)
                if status == 'fill':
                    order.px_fill = order.px_fill
                    order.volume_fill = order.px_fill
                if status == 'in process' or status == 'new':
                    order.px_fill = 0

                order.date = order.date + timedelta(seconds=next(LCGenerator.get_sequence()) % 20) \
                             + timedelta(milliseconds=next(LCGenerator.get_sequence()) * 10)
                order.status = status

                orders.append(order)

        return orders

    @staticmethod
    def main():
        history_orders = Main.workflow()

        for order in history_orders:
            print(order)

        csv = CSVStorage()
        csv.create_path(path=CSV_PATH)
        csv.write_to(path=CSV_PATH, file=history_orders)

        db = DBStorage()
        db.create_path(path=SQL_CSV_PATH)
        db.write_to(data=history_orders)


if __name__ == "__main__":
    Main.main()
