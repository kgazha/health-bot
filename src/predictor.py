from tensorflow.keras.models import load_model
import numpy as np
from src.handlers.base_text_handler import TextHandler
import os

from src.settings import SOURCE_DATA_DIR, DATA_MODEL_FILENAME, COVID_WORDS
from src.tools.source_data_manager import load_from_pickle

os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
model = load_model(DATA_MODEL_FILENAME)
answers = load_from_pickle(os.path.join(SOURCE_DATA_DIR, "answers.pkl"))
words = load_from_pickle(os.path.join(SOURCE_DATA_DIR, "words.pkl"))
classes = load_from_pickle(os.path.join(SOURCE_DATA_DIR, "classes.pkl"))
text_handler = TextHandler()


def bow(sentence, words, show_details=True):
    cleaned_text = text_handler.get_cleaned_text(sentence)
    normalized_words = text_handler.get_normalized_words(cleaned_text)
    normalized_words = text_handler.synonyms_transform(normalized_words, COVID_WORDS, COVID_WORDS[0])
    sentence_words = text_handler.get_stemmed_words(normalized_words)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)


def predict_class(sentence, model, show_details=False):
    p = bow(sentence, words, show_details)
    res = model.predict(np.array([p]))[0]
    error_threshold = 0.1
    results = [[i, r] for i, r in enumerate(res) if r > error_threshold]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"answer": classes[r[0]], "probability": str(r[1])})
    return return_list
