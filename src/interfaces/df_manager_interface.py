from typing import Union


class DataFrameManagerInterface:
    def transform_by_splitting_column(self, target_column: Union[int, str], separator: str):
        pass

    def generate_new_data_ngrams(self, target_column: Union[int, str], ngram, max_ngrams: int):
        pass

    def cut_column_by_splitting(self, target_column: Union[int, str], separator: str, max_values: int):
        pass
