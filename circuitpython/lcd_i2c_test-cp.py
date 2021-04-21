
import time
import board
import busio


from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from lcd.lcd import CursorMode

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 2

# Initialise I2C bus.
#i2c = busio.I2C(scl=board.GP17, sda=board.GP16)

# Initialise the lcd class

lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)
# Turn backlight on
lcd.backlight = True
# Print a two line message
#lcd.set_cursor_pos(1, 4)
lcd.print("Here I am")

# Wait 5s
time.sleep(5)
#print("LCD Clear")
#lcd.clear()