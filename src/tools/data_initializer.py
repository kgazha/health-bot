import os

from src.settings import SOURCE_DATA_DIR, DATAFRAME_FILENAME, SOURCE_EXCEL_FILENAME
from src.handlers.excel_handler import ExcelHandler
from src.tools.source_data_manager import save_to_pickle
from src.interfaces.data_handler_interface import DataHandlerInterface


def save_dump(filename: str, data_handler: DataHandlerInterface):
    target_filename = os.path.join(SOURCE_DATA_DIR, DATAFRAME_FILENAME)
    data_handler.load_data_source(filename)
    df = data_handler.extract_data()
    df = df.iloc[:-1, 1:3]
    save_to_pickle(df, target_filename)


save_dump(SOURCE_EXCEL_FILENAME, ExcelHandler())
