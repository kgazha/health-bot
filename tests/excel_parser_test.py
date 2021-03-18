from src.excel_parser import ExcelParser
from unittest.mock import MagicMock
import unittest


class TestExcelParser(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestExcelParser, self).__init__(*args, **kwargs)
        self.excel_parser = ExcelParser()

    def test_load_data_source(self):
        self.excel_parser.load_data_source = MagicMock()
        assert self.assertEqual(self.excel_parser._data_source, None)

