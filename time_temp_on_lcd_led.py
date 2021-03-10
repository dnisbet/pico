import utime
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import ds1302
from bme280 import *
import _thread


I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
sda=machine.Pin(0)
scl=machine.Pin(1)
clk_pin=18
data_pin=17
ce_pin=16
ds = ds1302.DS1302(clk_pin,data_pin,ce_pin)

t=0.2
#  _ - a
# |_|- f,g,b
# |_|- e,d,c

num = {' ':(1,1,1,1,1,1,1,1),
    '0':(0,0,0,0,0,0,1,1),
    '1':(1,0,0,1,1,1,1,1),
    '2':(0,0,1,0,0,1,0,1),
    '3':(0,0,0,0,1,1,0,1),
    '4':(1,0,0,1,1,0,0,1),
    '5':(0,1,0,0,1,0,0,1),
    '6':(0,1,0,0,0,0,0,1),
    '7':(0,0,0,1,1,1,1,1),
    '8':(0,0,0,0,0,0,0,1),
    '9':(0,0,0,0,1,0,0,1)}



segs=(19,14,13,12,11,10,9,8)
the_segs=('a','b','c','d','e','f','g','dec')
#display_string=''

digits = (2,3,4,5)

#s="% 4s" % str(no)


def seg(display_string,count=1):
    for digit in range(0,4):
        for loop in range(0,7):
          #place=machine.Pin(digits[digit], machine.Pin.OUT, value=0)
          #print (digits[digit],num[display_string[digit]][loop])
          #print ("loop: " + str(loop))
          #print ("num[display_string[digit]][loop]: " + str(num[display_string[digit]][loop]))
          show=machine.Pin(segs[loop], machine.Pin.OUT, value=num[display_string[digit]][loop]) 
        disp=machine.Pin(digits[digit], machine.Pin.OUT, value=1)
        time.sleep(0.0015)
        disp=machine.Pin(digits[digit], machine.Pin.OUT, value=0)



    
#clk_pin=14, data_pin=12, ce_pin=13):

def test_main():
    #Test function for verifying basic functionality
    #print("Running test_main")
    i2c = I2C(0, sda=sda, scl=scl, freq=400000)
    bme280 = BME280(i2c=i2c)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    #time=utime.localtime()
    #print(time)
    #lcd.putstr("Hello World!")
    #utime.sleep(0.2)
    lcd.clear()
    count = 0
    width=2
    #write_datetime(self, year, month, day, hour, minute, second, weekday = 1 ):
    while True:
        #time = utime.localtime()
        time = ds.read_datetime()
        #seg(display_string)
        #year=str(ds.read_datetime()[0])
        #month=str(ds.read_datetime()[1])
        #day=str(ds.read_datetime()[2])
        #width=2
        HH='{:0>{w}}'.format(str(ds.read_datetime()[3]),w=width)
        MM='{:0>{w}}'.format(str(ds.read_datetime()[4]),w=width)
        SS='{:0>{w}}'.format(str(ds.read_datetime()[5]),w=width)
        display_string=(HH + MM)
        #print ("display_string:" + display_string)
        #_thread.start_new_thread(seg,(display_string,0))
        seg(display_string)
        the_date="{day}/{month}/{year}".format(year=str(time[0]),month=str(time[1]),day=str(time[2]))
        #the_time="{HH}".format(HH=str(time[3]))
        the_time = HH + ":" + MM + ":" + SS
        #lcd.clear()
        lcd.move_to(0,0)
        seg(display_string)
        lcd.putstr(the_date)
        seg(display_string)
        lcd.move_to(0,1)
        seg(display_string)
        lcd.putstr(the_time)
        seg(display_string)
        #lcd.putstr("Hi")
        #print("{}/{}/{} {}:{}".format(year, month, day, HH, MM))
        #time = utime.localtime()
        #display_string=(HH + MM)
        #print ("display_string:" + display_string)
        #seg(display_string)
        
        #lcd.putstr("{year}/{month}/{day} {HH}:{MM}:{SS}".format(
        #    year=str(time[0]), month=str(time[1]), day=str(time[2]),
        #    HH=str(time[3]), MM=str(time[4]), SS=str(time[5])))
        #lcd.putstr(str(ds.read_datetime()))
        #lcd.blink_cursor_off()
        t, p, h = bme280.read_compensated_data()
        seg(display_string)
        t = t / 100
        t = '{:.1f}'.format(t)
        seg(display_string)


        lcd.move_to(11,1)
        seg(display_string)
        temp = t + "c"
        lcd.putstr(temp)
        seg(display_string)

        lcd.move_to(11,0)
        seg(display_string)
        pressure="{:.0f}".format(bme280.read_compensated_data()[1] / 256 / 100) + "mb"
        seg(display_string)
        lcd.putstr(pressure)
        seg(display_string)
        
        
test_main()
