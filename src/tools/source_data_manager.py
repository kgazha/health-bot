import pickle
from pandas import DataFrame
from functools import singledispatch

from src.interfaces.data_handler_interface import DataHandlerInterface


@singledispatch
def save_to_pickle(data_handler: DataHandlerInterface, source_filename: str, destination_filename: str):
    data_handler.load_data_source(source_filename)
    df = data_handler.extract_data()
    with open(destination_filename, "wb+") as file:
        pickle.dump(df, file)


@save_to_pickle.register(DataFrame)
def _save_to_pickle(df: DataFrame, destination_filename: str) -> None:
    with open(destination_filename, "wb+") as file:
        pickle.dump(df, file)


@save_to_pickle.register(list)
def _save_to_pickle(data: list, destination_filename: str) -> None:
    with open(destination_filename, "wb+") as file:
        pickle.dump(data, file)


def load_from_pickle(source_filename: str):
    with open(source_filename, "rb") as file:
        data = pickle.load(file)
    return data