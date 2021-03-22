import pymorphy2
from nltk.corpus import stopwords
from string import punctuation


morph = pymorphy2.MorphAnalyzer()
russian_stopwords = stopwords.words("russian")


class TextHandler:
    def __init__(self, text: str):
        self.text = text
        self.cleaned_text = ""
        self.normalized_words = []

    def get_normalized_words(self, excluded_pos=None):
        if excluded_pos is None:
            excluded_pos = []
        self.normalized_words = []
        for word in self.text.split():
            normal_form = None
            for parsed_word in morph.parse(word):
                if parsed_word.tag.POS in excluded_pos:
                    continue
                normal_form = parsed_word.normal_form
                break
            if normal_form:
                self.normalized_words.append(normal_form)

    def get_cleaned_text(self, text: str):
        translator = str.maketrans({key: " " for key in punctuation})
        self.cleaned_text = " ".join(text.translate(translator).split())
