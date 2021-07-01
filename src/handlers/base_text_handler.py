import pymorphy2
from typing import Union
from nltk import ngrams
from string import punctuation
from typing import List
from nltk.stem import SnowballStemmer
from typing import get_origin
from navec import Navec

from src.settings import NAVEC_DATA_FILENAME, COVID_WORDS, COVID_TOKEN
from src.interfaces.text_handler_interface import TextHandlerInterface


class TextHandler(TextHandlerInterface):

    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()
        self.snowball = SnowballStemmer(language="russian")
        self.navec = Navec.load(NAVEC_DATA_FILENAME)

    def get_normalized_words(self, text: str, excluded_pos=None) -> List[str]:
        if excluded_pos is None:
            excluded_pos = []
        normalized_words = []
        for word in text.split():
            normal_form = None
            for parsed_word in self.morph.parse(word):
                if parsed_word.tag.POS in excluded_pos:
                    continue
                normal_form = parsed_word.normal_form
                break
            if normal_form:
                normalized_words.append(normal_form)
        return normalized_words

    def get_stemmed_words(self, words: List[str]) -> List[str]:
        return [self.snowball.stem(word) for word in words]

    def get_cleaned_text(self, text: str) -> str:
        translator = str.maketrans({key: " " for key in punctuation})
        cleaned_text = " ".join(text.translate(translator).split())
        return cleaned_text

    def split_text_by_separator(self, text: str, separator: str) -> List[str]:
        result = text.split(sep=separator)
        return result

    def get_ngrams(self, words: List[str], n: int, max_ngrams: int = None) -> List[List[str]]:
        sentences = list(ngrams(words, n))
        if max_ngrams is not None:
            return sentences[:max_ngrams]
        return sentences

    def get_navec_tokens(self, words: List[str]) -> List[int]:
        tokens = []
        [tokens.append(self.navec.vocab[word]) for word in words if word in self.navec.vocab]
        if COVID_WORDS[0] in words:
            tokens.append(COVID_TOKEN)
        return tokens

    def synonyms_transform(self, input_data: Union[str, List[str]],
                           synonyms: List[str], target_word: str) -> List[str]:
        result = []
        if type(input_data) is get_origin(str):
            result = [target_word if x.lower() in synonyms else x for x in input_data.split()]
        elif type(input_data) is get_origin(List[str]):
            result = [target_word if x.lower() in synonyms else x for x in input_data]
        return result
