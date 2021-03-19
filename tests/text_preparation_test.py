from src.text_preparation import (get_normalized_words, get_cleaned_text)
import unittest


class TestTextPreparation(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTextPreparation, self).__init__(*args, **kwargs)
        self.text = "Привет из Южного Урала!"

    def test_text_preparation(self):
        cleaned_text = "Привет из Южного Урала"
        normalized_words = get_normalized_words(cleaned_text)
        assert normalized_words == ["привет", "из", "южный", "урал"]

    def test_get_cleaned_text(self):
        cleaned_text = get_cleaned_text(self.text)
        assert cleaned_text == "Привет из Южного Урала"
