from typing import Union


class DataFrameManagerInterface:
    def transform_by_splitting_column(self, target_column: Union[int, str], separator: str):
        pass
