import tensorflow_datasets as tfds
import tensorflow as tf

dataset, info = tfds.load('imdb_reviews/subwords8k', with_info=True,
                          as_supervised=True)
train_dataset, test_dataset = dataset['train'], dataset['test']

print("*-------------*")
print(train_dataset)
# for i in dir(train_dataset):
# 	print(i)



# encoder = info.features['text'].encoder

# print('Vocabulary size: {}'.format(encoder.vocab_size))

# sample_string = 'Hello TensorFlow.'

# encoded_string = encoder.encode(sample_string)
# print('Encoded string is {}'.format(encoded_string))

# original_string = encoder.decode(encoded_string)
# print('The original string: "{}"'.format(original_string))

# BUFFER_SIZE = 10000
# BATCH_SIZE = 64

# train_dataset = train_dataset.shuffle(BUFFER_SIZE)
# train_dataset = train_dataset.padded_batch(BATCH_SIZE)

# test_dataset = test_dataset.padded_batch(BATCH_SIZE)

# model = tf.keras.Sequential([
#     tf.keras.layers.Embedding(encoder.vocab_size, 64),
#     tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
#     tf.keras.layers.Dense(64, activation='relu'),
#     tf.keras.layers.Dense(1)
# ])

# model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
#               optimizer=tf.keras.optimizers.Adam(1e-4),
#               metrics=['accuracy'])

# history = model.fit(train_dataset, epochs=10,
#                     validation_data=test_dataset, 
#                     validation_steps=30)
