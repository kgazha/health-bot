import os

from src.analysis.df_manager import DataFrameManager
from src.handlers.base_text_handler import TextHandler
from src.tools.source_data_manager import load_from_pickle
from src.settings import SOURCE_DATA_DIR, DATAFRAME_FILENAME, QUESTIONS_COLUMN, SEPARATOR


df = load_from_pickle(os.path.join(SOURCE_DATA_DIR, DATAFRAME_FILENAME))
df_manager = DataFrameManager(df, TextHandler())

df_manager.cut_column_by_splitting(QUESTIONS_COLUMN, SEPARATOR, max_values=1)
df_manager.generate_new_data_ngrams(QUESTIONS_COLUMN, ngram=3, max_ngrams=3)

