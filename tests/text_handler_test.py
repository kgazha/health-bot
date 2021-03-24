from src.analysis.text_handler import TextHandler
import unittest


class TestTextHandler(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTextHandler, self).__init__(*args, **kwargs)
        self.text = "Привет из Южного Урала!"
        self.textHandler = TextHandler(self.text)

    def test_text_preparation(self):
        normalized_words = self.textHandler.get_normalized_words()
        expected_result = ["привет", "из", "южный", "урала!"]
        self.assertEqual(normalized_words, expected_result)

        normalized_words = self.textHandler.get_normalized_words(excluded_pos=["ADJF"])
        expected_result = ["привет", "из", "урала!"]
        self.assertEqual(normalized_words, expected_result)

    def test_get_cleaned_text(self):
        actual_text = self.textHandler.get_cleaned_text()
        cleaned_text = "Привет из Южного Урала"
        self.assertEqual(actual_text, cleaned_text)

    def test_split_text_by_separator(self):
        self.textHandler.text = "Коронавирус, это что?|Что такое Коронавирус?|Что такое ковид?"
        expected = ["Коронавирус, это что?", "Что такое Коронавирус?", "Что такое ковид?"]
        sentences = self.textHandler.split_text_by_separator("|")
        self.assertEqual(sentences, expected)
