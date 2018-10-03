import keyboard


def get_pressed_key(file_extension='.png'):
    key = '_none' + file_extension
    if keyboard.is_pressed('left'):
        key = '_left' + file_extension
    elif keyboard.is_pressed('right'):
        key = '_right' + file_extension
    return key
