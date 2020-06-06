import tensorflow as tf
import tensorflow_addons as tfa

# data set
mnist = tf.keras.datasets.mnist

# download data
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# convert integer to float
x_train, x_test = x_train / 255.0, x_test / 255.0

# linear stack of layers
# Activation - function that activate output layers
#	relu - activation return max(x,0)
# Flatten - выравнивает input
# Dense - data layer
# Dropout - range that apply output
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

# optimization
# function of learning loss
# values types
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)

