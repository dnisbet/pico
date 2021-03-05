import utime
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import ds1302



I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
sda=machine.Pin(1)
scl=machine.Pin(2)
#ds = ds1302.DS1302(machine.Pin(5),machine.Pin(18),machine.Pin(19))


def test_main():
    #Test function for verifying basic functionality
    print("Running test_main")
    i2c = I2C(0, sda=sda, scl=scl, freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    time=utime.localtime()
    print(time)
    lcd.putstr("Hello World!")
    utime.sleep(2)
    lcd.clear()
    count = 0
    while True:
        time = utime.localtime()
        #year=str(ds.Year())
        #month=str(ds.Month())
        #day=str(ds.Day())
        #HH=str(ds.Hour())
        #MM=str(ds.Minute())
        #year=str(ds.read_datetime()[0])
        #month=str(ds.read_datetime()[1])
        #day=str(ds.read_datetime()[2])
        #HH=str(ds.read_datetime()[3])
        #MM=str(ds.read_datetime()[4])
        #MM="% 2s" % MM
        #HH="% 2s" % HH
        #the_time=[year,month,day,HH,MM]
        
        lcd.clear()
        #print("{}/{}/{} {}:{}".format(year, month, day, HH, MM))
        #time = utime.localtime()
        #lcd.putstr("{}/{}/{} {}:{}".format(year, month, day, HH, MM))
        
        lcd.putstr("{year}/{month}/{day} {HH}:{MM}:{SS}".format(
            year=str(time[0]), month=str(time[1]), day=str(time[2]),
            HH=str(time[3]), MM=str(time[4]), SS=str(time[5])))
        #lcd.putstr(str(ds.read_datetime()))
        lcd.blink_cursor_on()
        lcd.move_to(0,1)
        lcd.putstr("Hi")
        utime.sleep(1)

#if __name__ == "__main__":
test_main()
