import sqlite3
from pathlib import Path

import pandas

from oop.constants import SQL_ORDER_ATTRIBUTES
from oop.interfaces import OrderListStorageTemplate
from pypika import Query, Table


class DBStorage(OrderListStorageTemplate):
    def connection(self):
        conn = sqlite3.connect('TestDB1.db')
        return conn

    def read_from(self, **kwargs):
        pass

    def create_path(self, **kwargs):
        path = kwargs.get("path")
        file_path = Path(path)
        return file_path

    def write_to(self, **kwargs):
        data = kwargs.get("data")
        # conn = self.connection()
        # curs = conn.cursor()
        # curs.execute('CREATE TABLE ORDERS (id, instrument, px_init, px_fill, volume_init, volume_fill, '
        #                           'side, status, date, note, tag)')
        # conn.commit()
        #
        # df = pandas.DataFrame(data=data, columns=['id', 'instrument', 'px_init', 'px_fill', 'volume_init', 'volume_fill',
        #                                           'side', 'status', 'date', 'note', 'tag'])
        # df.to_sql('Orders', conn, if_exists='replace', index=False)

        orders = Table('Orders')
        orders_sql_list = []
        for i in data:
            orders_sql_list.append((Query.from_(orders).into(SQL_ORDER_ATTRIBUTES).insert(i)).get_sql())
        return orders_sql_list



