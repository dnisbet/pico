import utime

import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

def test_main():
    #Test function for verifying basic functionality
    #print("Running test_main")
    i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
    #print(hex(i2c.scan()[0]))
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    
    lcd.putstr("It Works!")
    happy_face = bytearray([0x00,0x0A,0x00,0x04,0x00,0x11,0x0E,0x00])
    lcd.custom_char(0, happy_face)
    lcd.putchar(chr(0))
    utime.sleep(0.5)
    lcd.clear()
    count = 0
    while True:
        time = utime.localtime()
        the_date="{day}/{month}/{year}".format(year=str(time[0]),month=str(time[1]),day=str(time[2]))
        #the_time="{HH}".format(HH=str(time[3]))
        width=2
        HH='{:0>{w}}'.format(str(time[3]),w=width)
        SS='{:0>{w}}'.format(str(time[5]),w=width)
        MM='{:0>{w}}'.format(str(time[4]),w=width)
        the_time = HH + ":" + MM + ":" + SS
        lcd.move_to(0,0)
        lcd.putstr(the_date)
        lcd.move_to(0,1)
        lcd.putstr(the_time)
        lcd.move_to(14,0)
        lcd.putstr("Hi")
        lcd.move_to(13,1)
        lcd.putstr("Ro")
        lcd.move_to(15,1)
        lcd.putchar(chr(0))
        utime.sleep(1)

#if __name__ == "__main__":
test_main()

