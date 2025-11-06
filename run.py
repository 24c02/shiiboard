from gpiozero import Button
import uinput
import time
from mapping import MAPPING

buttons = {}

with uinput.Device(MAPPING.values()) as device:
    for io, key_event in MAPPING.items():
        button = Button(io)
        button.when_pressed = lambda: uinput.emit(key_event, 1)
        button.when_released = lambda: uinput.emit(key_event, 0)
        buttons[io] = button

    while True:
        time.sleep(1)