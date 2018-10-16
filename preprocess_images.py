import os

from image_operations import image_transformer

from argparse import ArgumentParser

from screenshot_handler.screen_grabber import ScreenGrabber

def read_arguments():
    parser = ArgumentParser()
    parser.add_argument('-f', '--folder', help='Folder for the original images')
    parser.add_argument('-d', '--dest-folder', help='Destination folder for the images')
    parser.add_argument('-s', '--scale', help='Scale for image shrinking')
    return parser.parse_args()

def main():
    arguments = read_arguments()
    folder = arguments.folder
    dest_folder = arguments.dest_folder
    scale = int(arguments.scale)
    for _, _, images in os.walk(folder):
        for image in images:
            if image.startswith('.') is False:
                image_transformer.preprocess_image('/'.join((folder, image)), scale, dest_folder)

if __name__ == '__main__':
    main()
