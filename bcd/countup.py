from machine import Pin
import time

digits=(15,16,14,17)

pos=(12,13,11,10)

latch=Pin(20,Pin.OUT)

a=Pin(digits[0],Pin.OUT)
b=Pin(digits[1],Pin.OUT)
c=Pin(digits[2],Pin.OUT)
d=Pin(digits[3],Pin.OUT)

for i in range(0,4):
    posio=Pin(pos[i],Pin.OUT,value=1)


def int2bcd(input):
    if input<10:
        bcd= "{:0>4}".format(str(bin(input))[2:])
    return bcd



def seg_show(n): 
    #d is most significant bit
    #0001 = 8
    val=int2bcd(n)
    a.value(int(val[3]))
    b.value(int(val[2]))
    c.value(int(val[1]))
    d.value(int(val[0]))



while True:
    #s="% 4s" % str(n)
        #for i in range(0,100):
         #   n=i
         #   num=int2bcd(i)
            #print(num+" a="+num[0]+" b="+num[1]+" c="+num[2]+" d="+num[3])
          #  seg_show(i)
          #  time.sleep(0.5)
       
  n="4115"
  nr = "".join(reversed(str(n)))

  s="% 4s" % str(nr)
  for digit in range(0,4):
    disp=Pin(pos[digit], Pin.OUT, value=0)
    seg_show(int(s[digit]))
    latch.high()
    #time.sleep(0.003)
    disp=Pin(pos[digit], Pin.OUT, value=1)
    latch.low()



    