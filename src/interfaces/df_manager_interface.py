from typing import Union
from pandas import DataFrame


class DataFrameManagerInterface:

    def transform_by_splitting_column(self, df, target_column: Union[int, str], separator: str):
        pass

    def generate_new_df_by_ngrams(self, df, target_column: Union[int, str],
                                  ngram, max_ngrams: int) -> DataFrame:
        pass

    def cut_column_by_splitting(self, df, target_column: Union[int, str],
                                separator: str, max_values: int):
        pass
