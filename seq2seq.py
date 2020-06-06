import tensorflow as tf
import tensorflow_addons as tfa
import string
import re
import numpy as np

def load_document(filename):
	file = open(filename, mode="rt", encoding="utf-8")
	text = file.read()
	file.close()
	return text;

def clean_data(text):
	spaces_dash = re.compile("([\s+-])")
	only_chars = re.compile("([^а-я^А-Я ])")
	whitespaces = re.compile("\s+")

	sub = spaces_dash.sub(" ", text)
	sub = only_chars.sub("", sub)
	sub = whitespaces.sub(" ", sub)

	words = sub.split(" ")

	for i in range(len(words)):
		words[i] = words[i].lower()

	# words.insert(0, "<start>")
	# words.append("<end>")

	return words

def vectorText(textArray):
	counter = 0
	out = {}

	for word in textArray:
		if word not in out:
			out[word] = counter
			counter += 1

	return out

t = load_document("instruction_data.txt")
clean = clean_data(t)
vector = vectorText(clean)

test_dataset = vector

BUFFER_SIZE = 10000
BATCH_SIZE = 64

train_dataset = train_dataset.shuffle(BUFFER_SIZE)
train_dataset = train_dataset.padded_batch(BATCH_SIZE)

test_dataset = test_dataset.padded_batch(BATCH_SIZE)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(encoder.vocab_size, 64),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])


print(clean)