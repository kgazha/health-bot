from src.text_preparation import (get_normalized_words, get_cleaned_text)
import unittest


class TestTextPreparation(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTextPreparation, self).__init__(*args, **kwargs)
        self.text = "Привет из Южного Урала!"
        self.cleaned_text = "Привет из Южного Урала"

    def test_text_preparation(self):
        normalized_words = get_normalized_words(self.cleaned_text)
        expected_result = ["привет", "из", "южный", "урал"]
        self.assertEqual(normalized_words, expected_result)

        normalized_words = get_normalized_words(self.cleaned_text, excluded_pos=["ADJF"])
        expected_result = ["привет", "из", "урал"]
        self.assertEqual(normalized_words, expected_result)

    def test_get_cleaned_text(self):
        actual_text = get_cleaned_text(self.text)
        self.assertEqual(actual_text, self.cleaned_text)

