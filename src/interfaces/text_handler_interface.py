class TextHandlerInterface:
    def get_normalized_words(self, text: str, excluded_pos=None) -> list[str]:
        pass

    def get_cleaned_text(self, text: str) -> str:
        pass

    def split_text_by_separator(self, text: str, separator: str) -> list[str]:
        pass
