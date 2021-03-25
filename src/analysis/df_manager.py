from src.interfaces.df_manager_interface import DataFrameManagerInterface
from src.interfaces.text_handler_interface import TextHandlerInterface

from pandas import DataFrame
from typing import Union
import pandas as pd


class DataFrameManager(DataFrameManagerInterface):

    def __init__(self, df: DataFrame, text_handler: TextHandlerInterface):
        self.df = df
        self._text_handler = text_handler

    def transform_by_splitting_column(self, target_column: Union[int, str], separator: str):
        _df = pd.DataFrame()
        for (idx, row) in self.df.iterrows():
            sentences = self._text_handler.split_text_by_separator(row[target_column], separator)
            for sentence in sentences:
                row[target_column] = sentence
                _df = _df.append(pd.DataFrame([row], columns=self.df.columns), ignore_index=True)
        self.df = _df

    def generate_new_data(self, target_column: Union[int, str], ngram, max_ngrams):
        _df = pd.DataFrame()
        for (idx, row) in self.df.iterrows():
            sentences = self._text_handler.get_ngrams(row[target_column], ngram, max_ngrams)
            for sentence in sentences:
                row[target_column] = sentence
                _df = _df.append(pd.DataFrame([row], columns=self.df.columns), ignore_index=True)
        self.df = _df
