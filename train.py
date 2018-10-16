import os

import cv2
import tensorflow as tf
from tensorflow import keras
import numpy as np

from argparse import ArgumentParser

from neural_networks.example_convolutional import example_network

LABELS_DICT = {
    'left': 0,
    'right': 1,
    'none': 2
}

def read_arguments():
    parser = ArgumentParser()
    parser.add_argument('-f', '--folder', help='Folder for the image dataset')
    return parser.parse_args()

def main():
    arguments = read_arguments()
    folder = arguments.folder
    images_names = os.listdir(folder)
    image_data = np.array([
        cv2.imread(os.path.abspath(os.path.join(folder, image)), cv2.IMREAD_GRAYSCALE)
        for image in images_names
    ])
    image_data = image_data / 255.0
    labels = [image.split('_')[1].split('.')[0] for image in images_names]
    label_numbers = np.array([LABELS_DICT[label] for label in labels])
    image_shape = image_data.shape
    image_data = image_data.reshape(len(images_names), image_shape[1], image_shape[2], 1)
    neural_net = example_network((image_shape[1], image_shape[2], 1))
    neural_net.fit(
        image_data,
        label_numbers,
        batch_size=100,
        epochs=10,
        validation_split=0.1,
        verbose=1)
    keras.models.save_model(
        neural_net,
        'neural_net.model',
    )
    print('Done!')


if __name__ == '__main__':
    main()
