# Scanner i2c en MicroPython | MicroPython i2c scanner
# Renvoi l'adresse en decimal et hexa de chaque device connecte sur le bus i2c
# Return decimal and hexa adress of each i2c device
# https://projetsdiy.fr - https://diyprojects.io (dec. 2017)

from machine import Pin, I2C
import utime
for i in range(0,39):
    sda=Pin(i)
    scl=Pin(i+1)
    #print("sda: ",sda)
    i2c = I2C(1)
    #utime.sleep_ms(100)
    val = i2c.readfrom_mem(0X76,0XD0, 1)[0]
    print(val)

    print('Scan i2c bus...')
    devices = i2c.scan()

    if len(devices) == 0:
      print("No i2c device !")
    else:
      print('i2c devices found:',len(devices))

      for device in devices:  
        print("Decimal address: ",device," | Hexa address: ",hex(device))