from src.analysis.df_manager import DataFrameManager
from src.analysis.base_text_handler import TextHandler

from pandas import DataFrame
from pandas.testing import assert_frame_equal
import unittest


class DataFrameManagerTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(DataFrameManagerTest, self).__init__(*args, **kwargs)
        self.df = DataFrame([["0", "1|3", "2"], ["1", "2", "3"], ["6", "7|1", "8"]])
        self._df_manager = DataFrameManager(self.df, TextHandler())

    def test_transform_by_splitting_column(self):
        self._df_manager.transform_by_splitting_column(1, "|")
        expected_df = DataFrame([["0", "1", "2"],
                                 ["0", "3", "2"],
                                 ["1", "2", "3"],
                                 ["6", "7", "8"],
                                 ["6", "1", "8"]])
        assert_frame_equal(self._df_manager.df, expected_df)
