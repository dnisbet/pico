from machine import I2C
from machine import Pin
from bmp280 import BMP280

sda=Pin(21)
scl=Pin(22)
#bus = I2C(1)

i2c = I2C(0, sda=sda, scl=scl)

bmp = BMP280(i2c_bus=1,addr=0x76)

bmp.use_case(BMP280_CASE_WEATHER)
bmp.oversample(BMP280_OS_HIGH)

bmp.temp_os = BMP280_TEMP_OS_8
bmp.press_os = BMP280_PRES_OS_4

bmp.standby = BMP280_STANDBY_250
bmp.iir = BMP280_IIR_FILTER_2

bmp.spi3w = BMP280_SPI3W_ON

bmp.power_mode = BMP280_POWER_FORCED
# or 
bmp.force_measure()

bmp.power_mode = BMP280_POWER_NORMAL
# or 
bmp.normal_measure()
# also
bmp.in_normal_mode()

bmp.power_mode = BMP280_POWER_SLEEP
# or 
bmp.sleep()

print(bmp.temperature)
print(bmp.pressure)

#True while measuring
bmp.is_measuring

#True while copying data to registers
bmp.is_updating