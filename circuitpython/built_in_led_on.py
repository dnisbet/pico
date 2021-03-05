"""
Button and LED example for Pico. Turns on LED when button is pressed.

REQUIRED HARDWARE:
* Button switch on pin GP13.
* LED on pin GP14.
"""
import time
import board
import digitalio
import pwmio

amber_led = digitalio.DigitalInOut(board.GP14)
amber_led.direction = digitalio.Direction.OUTPUT
green_led = digitalio.DigitalInOut(board.GP15)
green_led.direction = digitalio.Direction.OUTPUT
red_led = digitalio.DigitalInOut(board.GP12)
red_led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

buzzer = pwmio.PWMOut(board.GP11, frequency=660, duty_cycle=0, variable_frequency=True)

button_pressed = False

def waiting_for_button(duration):
    global button_pressed  # pylint: disable=global-statement
    end = time.monotonic() + duration
    while time.monotonic() < end:
        if button.value:
            button_pressed = True
            
while True:
    if button_pressed:
        red_led.value = True
        for _ in range(10):
            buzzer.duty_cycle = 2 ** 15
            waiting_for_button(0.2)
            buzzer.duty_cycle = 0
            waiting_for_button(0.2)
        button_pressed = False
    red_led.value = True
    waiting_for_button(5)
    amber_led.value = True
    waiting_for_button(2)
    red_led.value = False
    amber_led.value = False
    green_led.value = True
    waiting_for_button(5)
    green_led.value = False
    amber_led.value = True
    waiting_for_button(3)
    amber_led.value = False