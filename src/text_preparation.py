import pymorphy2
from nltk.corpus import stopwords
from string import punctuation


morph = pymorphy2.MorphAnalyzer()
russian_stopwords = stopwords.words("russian")


def get_normalized_words(text: str, excluded_pos=None) -> []:
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


def get_cleaned_text(text: str) -> str:
    translator = str.maketrans({key: " " for key in punctuation})
    cleaned_text = " ".join(text.translate(translator).split())
    return cleaned_text
