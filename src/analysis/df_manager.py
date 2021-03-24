from src.interfaces.df_manager_interface import DataFrameManagerInterface
from src.interfaces.text_handler_interface import TextHandlerInterface

from pandas import DataFrame


class DataFrameManager(DataFrameManagerInterface):

    def __init__(self, df: DataFrame, text_handler: TextHandlerInterface):
        self.df = df
        self._text_handler = text_handler

    def split_data_in_column(self, target_column: int, new_column_name: str):
        pass
