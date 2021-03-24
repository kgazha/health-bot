class TextHandlerInterface:
    def get_normalized_words(self, excluded_pos=None) -> []:
        pass

    def get_cleaned_text(self) -> str:
        pass

    def split_text_by_separator(self, separator: str) -> list[str]:
        pass
