from typing import List


class TextHandlerInterface:

    def get_normalized_words(self, text: str, excluded_pos=None) -> List[str]:
        pass

    def get_cleaned_text(self, text: str) -> str:
        pass

    def split_text_by_separator(self, text: str, separator: str) -> List[str]:
        pass

    def get_ngrams(self, words: List[str], n: int, max_ngrams: int = None) -> List[List[str]]:
        pass
