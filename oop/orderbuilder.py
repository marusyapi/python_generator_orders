from oop.generators import *
from oop.interfaces import Builder

from oop.order import Order


class OrderBuilder(Builder):
    def build(self):
        instrument = instrument_generator.generate_value()
        px_init = px_generator.generate_value(instrument=instrument)
        px_fill = px_generator.generate_value(instrument=instrument)
        volume_init = volume_generator.generate_value()

        order = Order(
            id_generator.generate_value(),
            instrument,
            px_init,
            px_fill,
            volume_init,
            0,
            side_generator.generate_value(),
            '',
            datetime.now(),
            note_generator.generate_value(),
            tag_generator.generate_value()
        )

        return order
