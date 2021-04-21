from machine import Pin
import time
import utime
from bme280 import *
from machine import I2C

#  _ - a
# |_|- f,g,b
# |_|- e,d,c

"""
Refactored code as setting the temp variable can't happen every led refresh loop as it switches it off for too long.
So only get a new sensor reading every 50 `ticks` and display that.
Put the display code in it's own function too.
"""

num = {' ':(1,1,1,1,1,1,1),
    '0':(0,0,0,0,0,0,1),
    '1':(1,0,0,1,1,1,1),
    '2':(0,0,1,0,0,1,0),
    '3':(0,0,0,0,1,1,0),
    '4':(1,0,0,1,1,0,0),
    '5':(0,1,0,0,1,0,0),
    '6':(0,1,0,0,0,0,0),
    '7':(0,0,0,1,1,1,1),
    '8':(0,0,0,0,0,0,0),
    '9':(0,0,0,0,1,0,0),
    'c':(1,1,1,0,0,1,0)}


#  _ - a
# |_|- f,g,b
# |_|- e,d,c

# - 14 a GP14
# - 16 b GP10
# - 13 c GP19
# - 3  d GP12
# - 5  e GP11
# - 11 f GP13
# - 15 g GP9
# - 7  dp GP21
segs=(14,10,19,12,11,13,9,16)
segments=segs
the_segs=('a','b','c','d','e','f','g','dec')

digits = (2,3,4,5)
no=1234


sda=Pin(0)
scl=Pin(1)


#ds = ds1302.DS1302(clk_pin,data_pin,ce_pin)
i2c = I2C(0, sda=sda, scl=scl, freq=400000)
width=2
bme280 = BME280(i2c=i2c)

def show_number(val):
    digits=[0,0,0]
    abs_val = abs(val)
    temp_val = abs_val



def seg(display_string,count=1):
    display_string="% 4s" % str(display_string)
    for digit in (0,2,1,3):
        for loop in range(7):
          place=Pin(digits[digit], Pin.OUT, value=0)
          if digit == 1:
              decimal=Pin(segs[7],Pin.OUT,value=0)
          else: decimal=Pin(segs[7],Pin.OUT,value=1)
          
          show=Pin(segs[loop], Pin.OUT, value=num[display_string[digit]][loop])
        disp=Pin(digits[digit], Pin.OUT, value=1)
        time.sleep(0.001)
        disp=Pin(digits[digit], Pin.OUT, value=0)

def seg(display_string,kind):
    for digit in (0,2,3,1):
        for loop in range(0,7):
          place=Pin(digits[digit], Pin.OUT, value=0)
          if digit == 1 and kind=='temp':
              decimal=Pin(segs[7],Pin.OUT,value=0)
          else: decimal=Pin(segs[7],Pin.OUT,value=1)
          #print (loop)
          #print(num[display_string[digit]][loop])
          show=Pin(segments[loop], Pin.OUT, value=num[display_string[digit]][loop])
          #time.sleep(0.01)
        disp=Pin(digits[digit], Pin.OUT, value=1)
        time.sleep(0.002)
        disp=Pin(digits[digit], Pin.OUT, value=0)



t= '{:.0f}'.format(bme280.read_compensated_data()[0] / 10)


p= '{:4d}'.format(int(bme280.read_compensated_data()[1] / 256 / 100))
#p= int(bme280.read_compensated_data()[1] / 256 / 100)
i=0
while True:
    i=0
    t_end = time.time() + 10
    
    while time.time() < t_end:
        t= '{:.0f}'.format(bme280.read_compensated_data()[0] / 10)
        t_end_2 = time.time() + 1
        while time.time() < t_end_2:
            seg(t+'c','temp')

    t_end = time.time() + 10
    p= '{:4d}'.format(int(bme280.read_compensated_data()[1] / 256 / 100))
    while time.time() < t_end:
        seg(str(p),'pres')
        i+=1
    

