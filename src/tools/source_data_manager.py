import pickle
from typing import Union

from pandas import DataFrame, Series


def save_to_pickle(data: Union[Series, DataFrame, list], destination_filename: str) -> None:
    with open(destination_filename, "wb+") as file:
        pickle.dump(data, file)


def load_from_pickle(source_filename: str):
    with open(source_filename, "rb") as file:
        data = pickle.load(file)
    return data
