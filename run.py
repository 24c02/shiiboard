from gpiozero import Button
import uinput
import time
from mapping import MAPPING

buttons = {}

with uinput.Device(MAPPING.values()) as device:
    for io, key_event in MAPPING.items():
        button = Button(io)
        button.when_pressed = lambda: device.emit(key_event, 1)
        button.when_released = lambda: device.emit(key_event, 0)
        buttons[io] = button

    while True:
        time.sleep(1)