from machine import Pin
import time
led = Pin(25, Pin.OUT)

from machine import Pin, PWM
from utime import sleep
buzzer = PWM(Pin(15))
buzzer.freq(500)



CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}


def dot():
    led.value(1)
    buzzer.duty_u16(1000)
    buzzer.freq(1760)
    time.sleep(0.2)
    led.value(0)
    buzzer.duty_u16(0)
    time.sleep(0.2)

def dash():
    led.value(1)
    buzzer.duty_u16(1000)
    buzzer.freq(400)
    time.sleep(0.5)
    buzzer.duty_u16(0)
    led.value(0)
    time.sleep(0.2)

while True:
    input = input('What would you like to send? ')
    for letter in input:
            for symbol in CODE[letter.upper()]:
                if symbol == '-':
                    dash()
                elif symbol == '.':
                    dot()
                else:
                    time.sleep(0.5)
            time.sleep(1)
            
