from machine import Pin
import time

digits=(15,16,14,17)


latch=Pin(20,Pin.OUT)
latch.low()
a=Pin(digits[0],Pin.OUT)
b=Pin(digits[1],Pin.OUT)
c=Pin(digits[2],Pin.OUT)
d=Pin(digits[3],Pin.OUT)




def int2bcd(input):
    bcd= "{:0>4}".format(str(bin(input))[2:])
    return bcd



def seg_show(n):
    
    #d is most significant bit
    #0001 = 8
    val=int2bcd(n)
    #print(val)
    a.value(int(val[3]))
    b.value(int(val[2]))
    c.value(int(val[1]))
    d.value(int(val[0]))
    
while True:
  for i in range(0,10):
    num=int2bcd(i)
    #print(num+" a="+num[0]+" b="+num[1]+" c="+num[2]+" d="+num[3])
    seg_show(i)
    time.sleep(0.5)
    