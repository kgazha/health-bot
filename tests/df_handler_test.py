from src.handlers.df_handler import DataFrameHandler
from src.handlers.base_text_handler import TextHandler

from pandas import DataFrame
from pandas.testing import assert_frame_equal
import unittest


class DataFrameHandlerTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(DataFrameHandlerTest, self).__init__(*args, **kwargs)
        self.df = DataFrame([["0", "1|3", "2"], ["1", "2", "3"], ["6", "7|1", "8"]])
        self._df_handler = DataFrameHandler(TextHandler())

    def test_transform_by_splitting_column(self):
        result = self._df_handler.transform_by_splitting_column(self.df, 1, "|")
        expected_df = DataFrame([["0", "1", "2"],
                                 ["0", "3", "2"],
                                 ["1", "2", "3"],
                                 ["6", "7", "8"],
                                 ["6", "1", "8"]])
        assert_frame_equal(result, expected_df)

    def test_cut_column_by_splitting(self):
        self._df_handler.cut_column_by_splitting(self.df, 1, "|", 1)
        expected_df = DataFrame([["0", "1", "2"],
                                 ["1", "2", "3"],
                                 ["6", "7", "8"]])
        assert_frame_equal(self.df, expected_df)
