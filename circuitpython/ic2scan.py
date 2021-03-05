# This circuitpython example for pi pico shows
#  scanning i2c bus to find multiplexers, and other devices directly attached
#  installing any multiplexer(s) found
#  scanning the multiplexers to discover devices attached to them
# (note some devices have been found to cause i2c.scan() to hang)
# (note some other devices share the tca9548a range.  if you have one attach it to a multiplexer only
#   or this code will think its a multiplexer itself!)

import time
import board
import busio


i2c = busio.I2C(board.GP1, board.GP0)# Create I2C bus as normal
 
def bus_scan(bus, mux, otherdev):
    devices=[]
    while len(devices) < 1:
        devices = bus.scan()
        if len(devices) >0:
            print (len(devices),"devices found. ",end="")
            for l in devices:
                if hex(l)>='0x70'and hex(l)<='0x77':#address range for TCA9548A selectable by A0,1,2 pullup to vcc.
                    tca[l-112]=l #add found address to list of multiplexer candidates
                else:
                    otherdev.append(l)
        else:
            print (" nothing found yet on I2C bus. ",end="")
            time.sleep(1)

l_func = lambda x, y: list((set(x)- set(y))) + list((set(y)- set(x)))# compare lists

#scan the i2c bus and find and instatiate the multiplexers
i2c.unlock()
while not i2c.try_lock():
    pass
print ("I2C bus locked, scanning. ",end="")
#print("ALL I2C addresses found:", [hex(device_address) for device_address in i2c.scan()])
tca=[0,0,0,0,0,0,0,0] #initialise multiplexers addresses,
tmux=[0,0,0,0,0,0,0,0] #initialise objects lists for discovery
otherdev=[]#a list of non-multiplexers found on direct i2c
baselist=[]#a list of everything found direct on i2c
bus_scan(i2c,tca, otherdev) #find devices directly attached to i2c bus
i2c.unlock()
print ('i2c scan complete, I2C bus unlocked')
#print("multiplexer addresses found:", [hex(device_address) for device_address in tca])

for mux in range(len(tca)):
    if tca[mux]!= 0:
        tmux[mux]=adafruit_tca9548a.TCA9548A(i2c, tca[mux]) # Create the TCA9548A object and give it the I2C bus
#
#         if tmux[mux][0].try_lock()==True:
#             time.sleep(0.001)
#             scanlist=i2c.scan()#print('ALL I2C addresses found:', [hex(device_address) for device_address in scanlist])
#         tmux[mux][0].unlock()
#
        print ('tca9548a multiplexer tmux['+str(mux)+'] created on', hex(mux+112))
        baselist.append( mux+112)
print("other I2C address(es) found:", [hex(device_address) for device_address in otherdev],'could be >1 device on an address here')
for device_address in otherdev:
    baselist.append(device_address)
#print (baselist)

#now scan the muxes and channels for devices
for mux in range(len(tca)):
    if tca[mux]!= 0:#print ('scanning mux', mux, 'at',hex(mux+112))
        for channel in range(8):#print ('trying to lock',channel)
            if tmux[mux][channel].try_lock()==True:
                time.sleep(0.001)
                scanlist=i2c.scan()#print('ALL I2C addresses found:', [hex(device_address) for device_address in scanlist])
                chandev=l_func(baselist,scanlist)
                if len(chandev)==1:
                    print('device found on tca9548a tmux['+str(mux)+'] channel',channel,hex(chandev[0]))
            tmux[mux][channel].unlock()