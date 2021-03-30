from oop.interfaces import IOrderBuilder


class OrderBuilder(IOrderBuilder):
    def build(self,
              obj_id,
              obj_instrument,
              obj_px_init,
              obj_px_fill,
              obj_volume_init,
              obj_volume_fill,
              obj_side,
              obj_status,
              obj_date,
              obj_note,
              obj_tag):
        return Order(
            obj_id, obj_instrument, obj_px_init, obj_px_fill, obj_volume_init, obj_volume_fill, obj_side, obj_status,
            obj_date, obj_note, obj_tag
        )


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
