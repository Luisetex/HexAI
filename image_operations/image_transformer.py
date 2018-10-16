import os

import cv2

def rgb_to_grayscale(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

def shrink_image(image, scale=4):
    scale = 1/scale
    shrinked_image = cv2.resize(
        image,
        None,
        fx=scale,
        fy=scale,
        interpolation=cv2.INTER_AREA
    )
    return shrinked_image

def preprocess_image(image_path, scale, dest_folder):
    folder, image_name = image_path.split('/')
    original_image = cv2.imread(os.path.abspath(image_path))
    grayscaled = rgb_to_grayscale(original_image)
    shrinked = shrink_image(grayscaled, scale)
    cv2.imwrite('/'.join((dest_folder, image_name)), shrinked)
