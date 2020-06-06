import tensorflow_datasets as tfds
import tensorflow as tf
import json

f = open("data/marked/1.txt", "r")
mark1 = json.loads(f.read())
f.close()

tf_dataset = tf.data.Dataset.from_tensor_slices(mark1["full"])
ts_dataset = tf.data.Dataset.from_tensor_slices(mark1["slim"])
vector_size = len(mark1["vector"])

test_dataset = tf.data.Dataset.from_tensor_slices(mark1["full"])

BUFFER_SIZE = 10000
BATCH_SIZE = 64

tf_dataset = tf_dataset.shuffle(BUFFER_SIZE)
tf_dataset = tf_dataset.padded_batch(BATCH_SIZE)
ts_dataset = ts_dataset.padded_batch(BATCH_SIZE)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vector_size, 64),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              optimizer=tf.keras.optimizers.Adam(1e-4),
              metrics=['accuracy'])

history = model.fit(tf_dataset, epochs=10,
                    validation_data=ts_dataset, 
                    validation_steps=30)

print(vector_size)