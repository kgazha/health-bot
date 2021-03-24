from src.analysis.base_text_handler import TextHandler
import unittest


class BaseTextHandlerTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(BaseTextHandlerTest, self).__init__(*args, **kwargs)
        self.text = "Привет из Южного Урала!"
        self.text_handler = TextHandler()

    def test_text_preparation(self):
        normalized_words = self.text_handler.get_normalized_words(self.text)
        expected_result = ["привет", "из", "южный", "урала!"]
        self.assertEqual(normalized_words, expected_result)

        normalized_words = self.text_handler.get_normalized_words(self.text, excluded_pos=["ADJF"])
        expected_result = ["привет", "из", "урала!"]
        self.assertEqual(normalized_words, expected_result)

    def test_get_cleaned_text(self):
        actual_text = self.text_handler.get_cleaned_text(self.text)
        cleaned_text = "Привет из Южного Урала"
        self.assertEqual(actual_text, cleaned_text)

    def test_split_text_by_separator(self):
        text = "Коронавирус, это что?|Что такое Коронавирус?|Что такое ковид?"
        expected = ["Коронавирус, это что?", "Что такое Коронавирус?", "Что такое ковид?"]
        sentences = self.text_handler.split_text_by_separator(text, "|")
        self.assertEqual(sentences, expected)
