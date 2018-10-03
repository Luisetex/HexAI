import cv2

def rgb_to_grayscale(image_path):
    folder, image_name = image_path.split('/')
    original_image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('_'.join((folder, 'gray', image_name)), grayscale_image)
