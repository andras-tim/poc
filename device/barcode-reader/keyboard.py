#! /usr/bin/env python3
from Xlib.display import Display
import Xlib
from pprint import pprint
import sys

key_codes = range(0, 255)


def handle_event(event):
    if event.type == Xlib.X.KeyRelease:
        key_code = event.detail
        if key_code in key_codes:
            print("KeyRelease: %d" % key_code)

display = Display()
root = display.screen().root
root.change_attributes(event_mask=Xlib.X.KeyReleaseMask)


for keycode in key_codes:
    root.grab_key(keycode, Xlib.X.AnyModifier, 1, Xlib.X.GrabModeAsync, Xlib.X.GrabModeAsync)

while 1:
    event = root.display.next_event()
    handle_event(event)
