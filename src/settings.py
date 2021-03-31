import os


current_dir = os.path.dirname(os.path.abspath(__file__))

# Data parameters
SOURCE_DATA_DIR = os.path.join(current_dir, "source_data")
SOURCE_EXCEL_FILENAME = r""
DATAFRAME_FILENAME = "df.pkl"
DATA_MODEL_FILENAME = os.path.join(SOURCE_DATA_DIR, "data_model.h5")

# DataFrame parameters
ANSWERS_COLUMN = "answer_text"
QUESTIONS_COLUMN = "sample_phrases"
SEPARATOR = "|"
