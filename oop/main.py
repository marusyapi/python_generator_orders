from oop.CSVStorage import CSVStorage
from oop.generators import *
from oop.orderbuilder import OrderBuilder


class Main:
    @staticmethod
    def main():
        order_builder = OrderBuilder()
        order = []
        id_order = IDGenerator()
        instrument_order = InstrumentGenerator().generate_value()
        px_init = PxGenerator(instrument_order)
        px_init_order = px_init.generate_value()
        px_fill_order = PxGenerator.generate_value(px_init)
        volume_init_order = VolumeGenerator()
        volume_fill_order = VolumeGenerator.generate_value(volume_init_order)
        side_order = SideGenerator()
        note_order = NoteGenerator()
        tag_order = TagGenerator()
        for i in ITEMS_RANGE:
            time_delta = timedelta(milliseconds=0)
            if i < RED_ZONE_ORDERS_COUNT:
                status_order = StatusGenerator(LIST_OF_RED_ZONE_STATUS)
                date_order = DateGenerator(RED_ZONE_INIT_DATE, RED_ZONE_END_DATE)
                for status in status_order.generate_value():
                    for date in date_order.generate_value():
                        if status == 'cancel':
                            px_init = volume_fill_order = 0
                        if status == 'partially fill':
                            volume_fill_order = px_fill_order
                        else:
                            volume_fill_order = px_init
                        order = order_builder.build(id_order.generate_value(),
                                                    instrument_order,
                                                    px_init,
                                                    px_fill_order,
                                                    volume_init_order.generate_value(),
                                                    volume_fill_order,
                                                    side_order.generate_value(),
                                                    status[i],
                                                    date.__format__(DATE_FORMAT),
                                                    note_order.generate_value(),
                                                    tag_order.generate_value())

            if RED_ZONE_ORDERS_COUNT <= i < 1800:
                status_order = StatusGenerator(LIST_OF_GREEN_ZONE_STATUS)
                date_order = DateGenerator(GREEN_ZONE_INIT_DATE, GREEN_ZONE_END_DATE)
                for status in status_order.generate_value():
                    for date in date_order.generate_value():
                        if status == 'cancel':
                            px_init = volume_fill_order = 0
                        if status == 'partially fill':
                            volume_fill_order = px_fill_order
                        else:
                            volume_fill_order = px_init
                        order = order_builder.build(id_order.generate_value(),
                                                    instrument_order,
                                                    px_init,
                                                    px_fill_order,
                                                    volume_init_order.generate_value(),
                                                    volume_fill_order,
                                                    side_order.generate_value(),
                                                    status[i],
                                                    date.__format__(DATE_FORMAT),
                                                    note_order.generate_value(),
                                                    tag_order.generate_value())

            if 1800 <= i < ORDERS_COUNT:
                status_order = StatusGenerator(LIST_OF_BLUE_ZONE_STATUS)
                date_order = DateGenerator(BLUE_ZONE_INIT_DATE, BLUE_ZONE_END_DATE)
                for status in status_order.generate_value():
                    for date in date_order.generate_value():
                        if status == 'cancel':
                            px_init = volume_fill_order = 0
                        if status == 'partially fill':
                            volume_fill_order = px_fill_order
                        else:
                            volume_fill_order = px_init
                        order = order_builder.build(id_order.generate_value(),
                                                    instrument_order,
                                                    px_init,
                                                    px_fill_order,
                                                    volume_init_order.generate_value(),
                                                    volume_fill_order,
                                                    side_order.generate_value(),
                                                    status[i],
                                                    date.__format__(DATE_FORMAT),
                                                    note_order.generate_value(),
                                                    tag_order.generate_value())

        csv = CSVStorage()
        csv.create_path(CSV_PATH)
        file = csv.write_to(CSV_PATH, order, ORDER_ATTRIBUTES)


if __name__ == "__main__":
    Main.main()
