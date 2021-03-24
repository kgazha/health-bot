import pymorphy2
from nltk.corpus import stopwords
from string import punctuation

from src.interfaces.text_handler_interface import TextHandlerInterface

morph = pymorphy2.MorphAnalyzer()
russian_stopwords = stopwords.words("russian")


class TextHandler(TextHandlerInterface):
    def __init__(self, text: str):
        self.text = text

    def get_normalized_words(self, excluded_pos=None) -> []:
        if excluded_pos is None:
            excluded_pos = []
        normalized_words = []
        for word in self.text.split():
            normal_form = None
            for parsed_word in morph.parse(word):
                if parsed_word.tag.POS in excluded_pos:
                    continue
                normal_form = parsed_word.normal_form
                break
            if normal_form:
                normalized_words.append(normal_form)
        return normalized_words

    def get_cleaned_text(self) -> str:
        translator = str.maketrans({key: " " for key in punctuation})
        cleaned_text = " ".join(self.text.translate(translator).split())
        return cleaned_text
    
    def split_text_by_separator(self, separator: str) -> list[str]:
        sentences = self.text.split(sep=separator)
        return sentences
