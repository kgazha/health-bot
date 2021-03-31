import os
from random import shuffle
import nltk
from src.analysis.df_manager import DataFrameManager
from src.handlers.base_text_handler import TextHandler
from src.tools.source_data_manager import load_from_pickle, save_to_pickle
from src.settings import SOURCE_DATA_DIR, DATAFRAME_FILENAME, QUESTIONS_COLUMN, SEPARATOR, ANSWERS_COLUMN, \
    DATA_MODEL_FILENAME
import numpy as np
from keras.models import Sequential
import tensorflow as tf


text_handler = TextHandler()
df = load_from_pickle(os.path.join(SOURCE_DATA_DIR, DATAFRAME_FILENAME))
df_manager = DataFrameManager(df, text_handler)

df_manager.cut_column_by_splitting(QUESTIONS_COLUMN, SEPARATOR, max_values=1)
df_manager.generate_new_data_ngrams(QUESTIONS_COLUMN, ngram=3, max_ngrams=3)

questions = []
answers = df_manager.df[ANSWERS_COLUMN]
for (idx, row) in df_manager.df.iterrows():
    cleaned_text = text_handler.get_cleaned_text(row[QUESTIONS_COLUMN])
    normalized_words = text_handler.get_normalized_words(cleaned_text)
    questions.append(normalized_words)

documents = []
classes = []
words = nltk.word_tokenize(" ".join([" ".join(x) for x in questions]))

for (idx, question) in enumerate(questions):
    documents.append((question, answers[idx]))
    if answers[idx] not in classes:
        classes.append(answers[idx])

unique_words = nltk.word_tokenize(" ".join(x for x in list(set(words))))

training = []
output_empty = [0] * len(classes)
for doc in documents:
    bag = []
    pattern_words = doc[0]
    for w in unique_words:
        bag.append(1) if w in pattern_words else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

shuffle(training)
training = np.array(training)
train_x = list(training[:, 0])
train_y = list(training[:, 1])

model = Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(len(train_y[0]), activation='softmax'))
optimizer = tf.keras.optimizers.Adam(clipvalue=0.5)
# sgd = tf.keras.optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=2)
model.save(DATA_MODEL_FILENAME, hist)

save_to_pickle(answers, os.path.join(SOURCE_DATA_DIR, 'answers.pkl'))
save_to_pickle(unique_words, os.path.join(SOURCE_DATA_DIR, 'words.pkl'))
save_to_pickle(classes, os.path.join(SOURCE_DATA_DIR, 'classes.pkl'))
print("model created")
