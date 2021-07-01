from src.interfaces.df_manager_interface import DataFrameHandlerInterface
from src.interfaces.text_handler_interface import TextHandlerInterface

from pandas import DataFrame
from typing import Union
import pandas as pd


class DataFrameHandler(DataFrameHandlerInterface):

    def __init__(self, text_handler: TextHandlerInterface):
        self._text_handler = text_handler

    def transform_by_splitting_column(self, df, target_column: Union[int, str], separator: str) -> DataFrame:
        _df = pd.DataFrame()
        for (idx, row) in df.iterrows():
            sentences = self._text_handler.split_text_by_separator(row[target_column], separator)
            for sentence in sentences:
                row[target_column] = sentence
                _df = _df.append(pd.DataFrame([row], columns=df.columns), ignore_index=True)
        return _df

    def generate_new_df_by_ngrams(self, df, target_column: Union[int, str],
                                  ngram, max_ngrams) -> DataFrame:
        _df = pd.DataFrame()
        df_copy = df.copy()
        for (idx, row) in df_copy.iterrows():
            sentences = self._text_handler.get_ngrams(row[target_column].split(), ngram, max_ngrams)
            for sentence in sentences:
                row[target_column] = " ".join(sentence)
                _df = _df.append(pd.DataFrame([row], columns=df.columns), ignore_index=True)
        return _df

    def cut_column_by_splitting(self, df, target_column: Union[int, str],
                                separator: str, max_values: int):
        df[target_column] = df[target_column]\
            .apply(lambda x: separator.join(x.split(separator)[:max_values]))
