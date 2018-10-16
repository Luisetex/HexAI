import tensorflow as tf
from tensorflow import keras

import numpy as np


def example_network(input_shape):
    model = keras.Sequential(
        [
            keras.layers.Convolution2D(32, 3, 3, input_shape=input_shape, activation=tf.nn.relu),
            keras.layers.MaxPooling2D(pool_size=(2, 2)),
            keras.layers.Flatten(),
            keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dense(3, activation=tf.nn.softmax)
        ]
    )
    model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
    return model
