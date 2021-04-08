from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Order:
    id: str
    instrument: str
    px_init: float
    px_fill: float
    volume_init: float
    volume_fill: float
    side: str
    status: str
    date: datetime
    note: str
    tag: str