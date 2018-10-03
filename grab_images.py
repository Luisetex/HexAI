from argparse import ArgumentParser

from screenshot_handler.screen_grabber import ScreenGrabber

def read_arguments():
    parser = ArgumentParser()
    parser.add_argument('-d', '--dest-folder', help='Destination folder for the images')
    parser.add_argument('-m', '--monitor', help='Dimensions for cropped screenshots in the following format: TOPxLEFT_WIDTHxHEIGHT')
    return parser.parse_args()

def screenshot_loop(screen_grabber):
    index = 0
    while True:
        screen_grabber.grab_screenshot(str(index))
        index += 1

def main():
    arguments = read_arguments()
    dest_folder = arguments.dest_folder
    monitor = arguments.monitor
    screen_grabber = ScreenGrabber(dest_folder, monitor=monitor)
    screenshot_loop(screen_grabber)

if __name__ == '__main__':
    main()
