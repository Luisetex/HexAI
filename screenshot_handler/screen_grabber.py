from keyboard_handler.keyboard_reader import get_pressed_key

import mss
import mss.tools


class ScreenGrabber:
    def __init__(self, dest_folder, monitor=None):
        self.dest_folder = dest_folder+'/'
        self.monitor = monitor if monitor is None else self.__parse_monitor(monitor)
        self.sct = mss.mss()
        self.sct.compression_level = 0
    
    def __parse_monitor(self, monitor):
        position, size = monitor.split('_')
        top, left = position.split('x')[0], position.split('x')[1]
        width, height = size.split('x')[0], size.split('x')[1] 
        return {'top': top, 'left': left, 'width': width, 'height': height}

    def __grab_fullscreen(self, output_path):
        self.sct.shot(output=output_path)

    def __grab_part_screen(self, output_path):
        sct_img = self.sct.grab(self.monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, level=0, output=output_path)

    def __get_screenshot_name(self, index):
        return index + get_pressed_key()

    def grab_screenshot(self, index):
        output_path = self.dest_folder + self.__get_screenshot_name(index)
        if self.monitor is None:
            self.__grab_fullscreen(output_path)
        else:
            self.__grab_part_screen(output_path)
