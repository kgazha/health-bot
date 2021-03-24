from src.analysis.df_manager import DataFrameManager
from src.analysis.base_text_handler import TextHandler

from pandas import DataFrame
import unittest


class DataFrameManagerTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(DataFrameManagerTest, self).__init__(*args, **kwargs)
        self.df = DataFrame([["0", "1|3", "2"], ["1", "2", "3"], ["6", "7|1", "8"]])
        self._df_manager = DataFrameManager(self.df, TextHandler())

    def test_split_data_in_column(self):
        self._df_manager.split_data_in_column(1, "|", "new_column")
        expected_df = DataFrame([["0", "1", "2"],
                                 ["0", "3", "2"],
                                 ["1", "2", "3"],
                                 ["6", "7", "8"],
                                 ["6", "1", "8"]])
        self.assertEqual(self._df_manager.df, expected_df)
