class DataHandlerInterface:
    def load_data_source(self, full_file_name: str):
        pass

    def extract_data(self):
        pass

    def save_data(self, full_file_name: str):
        pass
