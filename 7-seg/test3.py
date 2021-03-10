from machine import Pin
import time
import utime
import ds1302
from machine import I2C
t=0.2
#  _ - a
# |_|- f,g,b
# |_|- e,d,c

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
    '9':(0,0,0,0,1,0,0)}



segs=(19,14,13,12,11,10,9,8)
the_segs=('a','b','c','d','e','f','g','dec')

digits = (2,3,4,5)
no=1234
s="% 4s" % str(no)

sda=Pin(0)
scl=Pin(1)
clk_pin=18
data_pin=17
ce_pin=16
ds = ds1302.DS1302(clk_pin,data_pin,ce_pin)
i2c = I2C(0, sda=sda, scl=scl, freq=400000)
width=2

while True:
  MM='{:0>{w}}'.format(str(ds.read_datetime()[4]),w=width)
  HH='{:0>{w}}'.format(str(ds.read_datetime()[3]),w=width)
  display_string=(HH + MM)
        #print ("display_string:" + display_string)
  s=display_string
  for digit in range(0,4):
        for loop in range(0,7):
            #print (digits[digit],segments[loop],num[s[digit]][loop])
            place=Pin(digits[digit], Pin.OUT, value=0)
            show=Pin(segs[loop], Pin.OUT, value=num[s[digit]][loop])
        
        Pin(segs[7],Pin.OUT,value=1)
        disp=Pin(digits[digit], Pin.OUT, value=1)
        time.sleep(0.0019)
        disp=Pin(digits[digit], Pin.OUT, value=0)


