import utime
from machine import I2C
from machine import Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
sda=Pin(17, Pin.OUT)
scl=Pin(16, Pin.OUT)


amber_led = Pin(15, Pin.OUT)
green_led = Pin(14, Pin.OUT)
red_led = Pin(12, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(11, Pin.OUT)




def test_main():
    #Test function for verifying basic functionality
    leds = [amber_led,green_led,red_led]
    print ("Turn on all leds")
    for led in leds:
        led.toggle()
    print("Running test_main")
    i2c = I2C(0) #GP8, GP9
    i2c.scan()
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    
    lcd.putstr("It Works!")
    utime.sleep(2)
    lcd.clear()
    count = 0
    while True:
        lcd.clear()
        time = utime.localtime()
        lcd.putstr("{year}/{month}/{day} {HH}:{MM}".format(
            year=str(time[0]), month=str(time[1]), day=str(time[2]),
            HH=str(time[3]), MM=str(time[4]), SS=str(time[5])))
        if count % 10 == 0:
            print("Turning cursor on")
            lcd.show_cursor()
        if count % 10 == 1:
            print("Turning cursor off")
            lcd.hide_cursor()
        if count % 10 == 2:
            print("Turning blink cursor on")
            lcd.blink_cursor_on()
        if count % 10 == 3:
            print("Turning blink cursor off")
            lcd.blink_cursor_off()                    
        if count % 10 == 4:
            print("Turning backlight off")
            lcd.backlight_off()
        if count % 10 == 5:
            print("Turning backlight on")
            lcd.backlight_on()
        if count % 10 == 6:
            print("Turning display off")
            lcd.display_off()
        if count % 10 == 7:
            print("Turning display on")
            lcd.display_on()
        if count % 10 == 8:
            print("Filling display")
            lcd.clear()
            string = ""
            for x in range(32, 32+I2C_NUM_ROWS*I2C_NUM_COLS):
                string += chr(x)
            lcd.putstr(string)
        count += 1
        utime.sleep(2)

#if __name__ == "__main__":
test_main()