import pandas
from pandas import DataFrame

from src.interfaces.data_handler_interface import DataHandlerInterface


class ExcelHandler(DataHandlerInterface):

    def __init__(self):
        self._full_file_name = None
        self._data_source = None

    def load_data_source(self, full_file_name: str):
        self._data_source = pandas.read_excel(full_file_name)

    def extract_data(self) -> DataFrame:
        return self._data_source

    def save_data(self, full_file_name: str):
        pass
