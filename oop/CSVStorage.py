from pathlib import Path
import pandas
from oop.interfaces import OrderListStorageTemplate


class CSVStorage(OrderListStorageTemplate):
    def create_path(self, **kwargs):
        path = kwargs.get("path")
        file_path = Path(path)
        return file_path

    def write_to(self, **kwargs):
        path = kwargs.get("path")
        file = kwargs.get("file")
        csv_file = pandas.DataFrame(data=file)
        csv_file.to_csv(path, index_label=False, sep='\t')
        return csv_file

    def read_from(self, **kwargs):
        file = kwargs.get("file")
        csv_file = pandas.read_csv(file)
        return csv_file

    def connection(self):
        pass
