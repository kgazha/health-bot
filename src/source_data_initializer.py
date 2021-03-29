import pickle
from pandas import DataFrame

from src.handlers.excel_handler import ExcelHandler


def save_to_pickle(source_filename: str, destination_filename: str):
    excel_handler = ExcelHandler()
    excel_handler.load_data_source(source_filename)
    df = excel_handler.extract_data()
    with open(destination_filename, "wb") as file:
        pickle.dump(df, file)


def load_from_pickle(source_filename: str) -> DataFrame:
    with open(source_filename, "rb") as file:
        df = pickle.load(file)
    return df
