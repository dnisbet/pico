import utime
from machine import Pin



amber_led = Pin(15, Pin.OUT)
green_led = Pin(14, Pin.OUT)
red_led = Pin(12, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(11, Pin.OUT)



    #Test function for verifying basic functionality
leds = [amber_led,green_led,red_led]
print ("Turn on all leds")
for led in leds:
    led.on()