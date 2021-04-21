# needs circuitpython and adafruit_hid

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import busio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode

 
print("---Pico Pad Keyboard---")

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)
# Turn backlight on
lcd.backlight = True



kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

pins = [
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
]
 
MEDIA = 1
KEY = 2

keymap = {
    (1): (KEY, [Keycode.CONTROL, Keycode.TAB],"Next Tab"),
    (0): (KEY, [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB],"Prev Tab"),
    (2): (KEY, [Keycode.F5],"Refresh"),
    (3): (KEY, [Keycode.CONTROL, Keycode.W],"Close Tab"),

}
switches = [0, 1, 2, 3]

for i in range(4):
    switches[i] = DigitalInOut(pins[i])
    switches[i].direction = Direction.INPUT
    switches[i].pull = Pull.UP
 
switch_state = [0, 0, 0, 0,]

while True:
    for button in range(4):
        if switch_state[button] == 0:
            if not switches[button].value:
                print(keymap[button][2])
                lcd.clear()
                lcd.print(keymap[button][2])
                try:
                    if keymap[button][0] == KEY:
                        kbd.press(*keymap[button][1])
                    else:
                        cc.send(keymap[button][1])
                except ValueError:  # deals w six key limit
                    pass
                switch_state[button] = 1
 
        if switch_state[button] == 1:
            if switches[button].value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.release(*keymap[button][1])
 
                except ValueError:
                    pass
                switch_state[button] = 0
 
    time.sleep(0.01)  # debounce


