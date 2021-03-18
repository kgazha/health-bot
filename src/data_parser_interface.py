from pandas import DataFrame


class DataParserInterface:
    def load_data_source(self, full_file_name: str):
        pass

    def extract_data(self) -> DataFrame:
        pass
