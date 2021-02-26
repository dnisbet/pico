from machine import ADC,Pin
from utime import sleep
temp_sensor = ADC(4)
temperature = temp_sensor.read_u16()
to_volts = 3.3 / 65535
temperature = temperature * to_volts
celsius_degrees = 27 - (temperature - 0.706) / 0.001721
print (celsius_degrees)
led = Pin(25, Pin.OUT)
led.on()
message = input("enter text to decipher:")
#message = 'GIEWIVrGMTLIVrHIQS' #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      else:
         translated = translated + symbol
   print('Hacking key #%s: %s' % (key, translated))

