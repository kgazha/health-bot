import pymorphy2
from nltk.corpus import stopwords
from nltk import ngrams
from string import punctuation
from typing import List

from src.interfaces.text_handler_interface import TextHandlerInterface

morph = pymorphy2.MorphAnalyzer()
russian_stopwords = stopwords.words("russian")


class TextHandler(TextHandlerInterface):
    def __init__(self):
        pass

    def get_normalized_words(self, text: str, excluded_pos=None) -> List[str]:
        if excluded_pos is None:
            excluded_pos = []
        normalized_words = []
        for word in text.split():
            normal_form = None
            for parsed_word in morph.parse(word):
                if parsed_word.tag.POS in excluded_pos:
                    continue
                normal_form = parsed_word.normal_form
                break
            if normal_form:
                normalized_words.append(normal_form)
        return normalized_words

    def get_cleaned_text(self, text: str) -> str:
        translator = str.maketrans({key: " " for key in punctuation})
        cleaned_text = " ".join(text.translate(translator).split())
        return cleaned_text

    def split_text_by_separator(self, text: str, separator: str) -> List[str]:
        sentences = text.split(sep=separator)
        return sentences

    def get_ngrams(self, words: List[str], n: int, max_ngrams: int = None) -> List[List[str]]:
        sentences = list(ngrams(words, n))
        if max_ngrams is not None:
            return sentences[:max_ngrams]
        return sentences
