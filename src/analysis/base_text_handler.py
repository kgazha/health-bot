import pymorphy2
from nltk.corpus import stopwords
from string import punctuation

from src.interfaces.text_handler_interface import TextHandlerInterface

morph = pymorphy2.MorphAnalyzer()
russian_stopwords = stopwords.words("russian")


class TextHandler(TextHandlerInterface):
    def __init__(self):
        pass
        # self.text = text

    def get_normalized_words(self, text: str, excluded_pos=None) -> list[str]:
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
    
    def split_text_by_separator(self, text: str, separator: str) -> list[str]:
        sentences = text.split(sep=separator)
        return sentences
