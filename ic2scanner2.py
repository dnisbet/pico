import machine
from machine import I2C
sda=machine.Pin(1)
scl=machine.Pin(2)

i2c=I2C(0,sda=sda,scl=scl)

devices = i2c.scan()
print(i2c.scan())
if devices:
    for i in devices:
        print(hex(i))