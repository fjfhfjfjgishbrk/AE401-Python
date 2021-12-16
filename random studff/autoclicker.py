import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 0.03
button = Button.left
button_2 = Button.right
button_3 = Button.middle
start_stop_key = KeyCode(char='`')
exit_key = KeyCode(char='q')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.button_2 = button_2
        self.button_3 = button_3
        self.running = False
        self.program_run = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_run = False

    def run(self):
        while self.program_run:
            while self.running:
                mouse.click(self.button)
                mouse.click(self.button_2)
                mouse.click(self.button_3)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
thread = ClickMouse(delay, button)
thread.start()


def on_press(key):
    if key == start_stop_key:
        if thread.running:
            thread.stop_clicking()
        else:
            thread.start_clicking()
    elif key == exit_key:
        thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()