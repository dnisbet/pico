from machine import Pin, PWM
from utime import sleep
import time
buzzer = PWM(Pin(11))
buzzer.freq(200)


duty = 0
direction = 1
for _ in range(8 * 256):
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    buzzer.duty_u16(duty * duty)
    time.sleep(0.001)