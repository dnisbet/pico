import utime

import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import DS1302

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
sda=machine.Pin(0)
scl=machine.Pin(1)
ds = DS1302.DS1302(machine.Pin(5),machine.Pin(18),machine.Pin(19))
ds.start()

def test_main():
    #Test function for verifying basic functionality
    print("Running test_main")
    i2c = I2C(0, sda=sda, scl=scl, freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
   
    lcd.putstr("Hello World!")
    utime.sleep(2)
    lcd.clear()
    count = 0
    while True:
        year=str(ds.Year())
        month=str(ds.Month())
        day=str(ds.Day())
        HH=str(ds.Hour())
        MM=str(ds.Minute())
        the_time=[year,month,day,HH,MM]
        lcd.clear()
        
        time = utime.localtime()
        lcd.putstr("{}/{}/{} {}:{}".format(year, month, day, HH, MM))
        #lcd.putstr("{year}/{month}/{day} {HH}:{MM}".format(
        #    year=str(time[0]), month=str(time[1]), day=str(time[2]),
        #    HH=str(time[3]), MM=str(time[4]), SS=str(time[5])))
        lcd.blink_cursor_on()
        lcd.move_to(0,1)
        lcd.putstr("Hi")
        utime.sleep(5)

#if __name__ == "__main__":
test_main()
