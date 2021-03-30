from argparse import ArgumentParser
import os

from handlers.excel_handler import ExcelHandler
from tools.source_data_converter import save_to_pickle
from interfaces.data_handler_interface import DataHandlerInterface


current_dir = os.path.dirname(os.path.abspath(__file__))


def save_dump(filename: str, data_handler: DataHandlerInterface):
    target_filename = os.path.join(current_dir, r"source_data\dump.pkl")
    data_handler.load_data_source(filename)
    df = data_handler.extract_data()
    df = df.iloc[:-1, 1:3]
    save_to_pickle(df, target_filename)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--source_excel', type=str)
    args = parser.parse_args()
    if args.source_excel:
        save_dump(args.source_excel, ExcelHandler())
