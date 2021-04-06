import csv

from oop.CSVStorage import CSVStorage
from oop.DBStorage import DBStorage
from oop.generators import *
from oop.interfaces import Director
from oop.orderbuilder import OrderBuilder


class Main:

    @staticmethod
    def main():
        director = Director()
        director.builder = OrderBuilder()

        orders = [director.builder.build()]

        csv = CSVStorage()
        csv.create_path(path=CSV_PATH)
        for order in orders:
            csv.write_to(path=CSV_PATH, file=order)

        db = DBStorage()
        db.create_path(path=SQL_CSV_PATH)
        db.write_to(path=SQL_CSV_PATH, data=orders)


if __name__ == "__main__":
    Main.main()
