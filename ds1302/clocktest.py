import utime
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import ds1302
from bme280 import *


I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
sda=machine.Pin(0)
scl=machine.Pin(1)
clk_pin=18
data_pin=17
ce_pin=16
ds = ds1302.DS1302(clk_pin,data_pin,ce_pin)

#clk_pin=14, data_pin=12, ce_pin=13):

def test_main():
    #Test function for verifying basic functionality
    print("Running test_main")
    i2c = I2C(0, sda=sda, scl=scl, freq=400000)
    bme280 = BME280(i2c=i2c)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    time=utime.localtime()
    print(time)
    lcd.putstr("Hello World!")
    utime.sleep(2)
    lcd.clear()
    count = 0
    #write_datetime(self, year, month, day, hour, minute, second, weekday = 1 ):
    while True:
        time = utime.localtime()
        time = ds.read_datetime()
        year=str(ds.read_datetime()[0])
        month=str(ds.read_datetime()[1])
        day=str(ds.read_datetime()[2])
        width=2
        HH='{:0>{w}}'.format(str(ds.read_datetime()[3]),w=width)
        MM='{:0>{w}}'.format(str(ds.read_datetime()[4]),w=width)
        SS='{:0>{w}}'.format(str(ds.read_datetime()[5]),w=width)

        the_date="{day}/{month}/{year}".format(year=str(time[0]),month=str(time[1]),day=str(time[2]))
        #the_time="{HH}".format(HH=str(time[3]))
        the_time = HH + ":" + MM + ":" + SS
        #lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr(the_date)
        lcd.move_to(0,1)
        lcd.putstr(the_time)

        #lcd.putstr("Hi")
        #print("{}/{}/{} {}:{}".format(year, month, day, HH, MM))
        #time = utime.localtime()

        
        #lcd.putstr("{year}/{month}/{day} {HH}:{MM}:{SS}".format(
        #    year=str(time[0]), month=str(time[1]), day=str(time[2]),
        #    HH=str(time[3]), MM=str(time[4]), SS=str(time[5])))
        #lcd.putstr(str(ds.read_datetime()))
        #lcd.blink_cursor_off()
        c_wi=2
        t, p, h = bme280.read_compensated_data()
        t = t / 100
        t = '{:.1f}'.format(t)


        lcd.move_to(11,1)
        temp = t + "c"
        lcd.putstr(temp)

        lcd.move_to(11,0)
        pressure="{:.0f}".format(bme280.read_compensated_data()[1] / 256 / 100) + "mb"
        lcd.putstr(pressure)
        utime.sleep(0.9)

#if __name__ == "__main__":
test_main()
