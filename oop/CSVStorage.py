from pathlib import Path
import pandas
from oop.interfaces import IOrderListStorageTemplate


class CSVStorage(IOrderListStorageTemplate):
    def create_path(self, path):
        file_path = Path(path)
        return file_path

    def write_to(self, path, mylist, columns):
        csv_file = pandas.DataFrame()
        csv_file.to_csv(path, index_label=False, sep='\t')
        return csv_file

    def read_from(self, file):
        csv_file = pandas.read_csv(file)
        return csv_file
