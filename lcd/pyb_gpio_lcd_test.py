"""Implements a HD44780 character LCD connected via pyboard GPIO pins."""

from machine import Pin
import utime, time
from pyb_gpio_lcd import GpioLcd

#rs = Pin(0,Pin.OUT)
#e = Pin(1,Pin.OUT)
#d4 = Pin(2,Pin.OUT)
#d5 = Pin(3,Pin.OUT)
#d6 = Pin(4,Pin.OUT)
#d7 = Pin(5,Pin.OUT)

# Wiring used for this example:
#
#  1 - Vss (aka Ground) - Connect to one of the ground pins on you pyboard.
#  2 - VDD - I connected to VIN which is 5 volts when your pyboard is powered via USB
#  3 - VE (Contrast voltage) - I'll discuss this below
#  4 - RS (Register Select) connect to Y12 (as per call to GpioLcd)
#  5 - RW (Read/Write) - connect to ground
#  6 - EN (Enable) connect to Y11 (as per call to GpioLcd)
#  7 - D0 - leave unconnected
#  8 - D1 - leave unconnected
#  9 - D2 - leave unconnected
# 10 - D3 - leave unconnected
# 11 - D4 - connect to Y5 (as per call to GpioLcd)
# 12 - D5 - connect to Y6 (as per call to GpioLcd)
# 13 - D6 - connect to Y7 (as per call to GpioLcd)
# 14 - D7 - connect to Y8 (as per call to GpioLcd)
# 15 - A (BackLight Anode) - Connect to VIN
# 16 - K (Backlight Cathode) - Connect to Ground
#
# On 14-pin LCDs, there is no backlight, so pins 15 & 16 don't exist.
#
# The Contrast line (pin 3) typically connects to the center tap of a
# 10K potentiometer, and the other 2 legs of the 10K potentiometer are
# connected to pins 1 and 2 (Ground and VDD)
#
# The wiring diagram on the following page shows a typical "base" wiring:
# http://www.instructables.com/id/How-to-drive-a-character-LCD-displays-using-DIP-sw/step2/HD44780-pinout/
# Add to that the EN, RS, and D4-D7 lines.



lcd = GpioLcd(rs_pin=Pin(0,Pin.OPEN_DRAIN),
                  enable_pin=Pin(1,Pin.OPEN_DRAIN),
                  d4_pin=Pin(2,Pin.OPEN_DRAIN),
                  d5_pin=Pin(3,Pin.OPEN_DRAIN),
                  d6_pin=Pin(4,Pin.OPEN_DRAIN),
                  d7_pin=Pin(5,Pin.OPEN_DRAIN),
                  num_lines=2, num_columns=16)
    #print ("putstr")
while True:
    lcd.putstr("It Works!\nSecond Line")
    lcd.putstr("Hello World")