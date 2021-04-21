import utime

import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=400000)
    #print(hex(i2c.scan()[0]))
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

led = machine.Pin(25, machine.Pin.OUT)

def show_time(col):
    global lcd
    time = utime.localtime()
    the_date="{day}/{month}/{year}".format(year=str(time[0]),month=str(time[1]),day=str(time[2]))
    #the_time="{HH}".format(HH=str(time[3]))
    width=2
    HH='{:0>{w}}'.format(str(time[3]),w=width)
    SS='{:0>{w}}'.format(str(time[5]),w=width)
    MM='{:0>{w}}'.format(str(time[4]),w=width)
    the_time = HH + ":" + MM + ":" + SS
    lcd.move_to(col,0)
    lcd.putstr(the_date)
    lcd.move_to(col,1)
    lcd.putstr(the_time)

def test_main():
    #Test function for verifying basic functionality
    #print("Running test_main")
    
    lcd.putstr("It Works!")
    happy_face = bytearray([0x00,0x0A,0x00,0x04,0x00,0x11,0x0E,0x00])
    lcd.custom_char(0, happy_face)
    lcd.putchar(chr(0))
    utime.sleep(0.5)
    lcd.clear()
       # The End
    lcd.custom_char(4, bytearray([7, 12, 24, 16, 22, 22, 22, 16]))
    lcd.custom_char(1, bytearray([28, 6, 3, 1, 13, 13, 13, 1]))
    lcd.custom_char(2, bytearray([16, 20, 20, 23, 19, 24, 12, 7]))
    lcd.custom_char(3, bytearray([1, 1, 5, 29, 25, 3, 6, 28]))
    lcd.clear()
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr('\x04')
    lcd.putstr('\x01')
    lcd.move_to(3,1)

    lcd.move_to(0, 1)
    lcd.putstr('\x02')
    lcd.putstr('\x03')
    
    lcd.move_to(5,0)
    lcd.putstr('The')
    lcd.move_to(5,1)
    lcd.putstr('End')
    count = 0
    lcd.clear()
    utime.sleep(1)
    

    
    #lcd.home()

while True:
    show_time(1)
    utime.sleep(0.5)

#if __name__ == "__main__":
#test_main()


