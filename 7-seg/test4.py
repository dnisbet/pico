from machine import Pin, Timer
import time
import utime


t=0.2
#  _ - a
# |_|- f,g,b
# |_|- e,d,c




digits = (2,3,4,5)
#for i in range(0,4):
# di=(Pin(digits[i], Pin.OUT))
# di.on()
def dig1():
    di=Pin(digits[0], Pin.OUT,0)
def dig2():
    di=Pin(digits[1], Pin.OUT,0)
def dig3():
    di=Pin(digits[2], Pin.OUT,0)
def dig4():
    di=Pin(digits[3], Pin.OUT,0)
def reset(i):
        di=(Pin(digits[i], Pin.OUT,0))


segments=(14,10,19,12,11,13,9,16)
#  _ - a
# |_|- f,g,b
# |_|- e,d,c
num = {' ':(1,1,1,1,1,1,1),
    '0':(0,0,0,0,0,0,1),
    '1':(1,0,0,1,1,1,1),
    '2':(0,0,1,0,0,1,0),
    '3':(0,0,0,0,1,1,0),
    '4':(1,0,0,1,1,0,0),
    '5':(0,1,0,0,1,0,0),
    '6':(0,1,0,0,0,0,0),
    '7':(0,0,0,1,1,1,1),
    '8':(0,0,0,0,0,0,0),
    '9':(0,0,0,0,1,0,0),
    'A':(0,0,0,1,0,0,0),
    'a':(0,0,0,0,0,1,0),
    'b':(1,1,0,0,0,0,0),
    'c':(1,1,1,0,0,1,0),
    'd':(1,0,0,0,0,1,0),
    'E':(0,1,1,0,0,0,0),
    'f':(0,1,1,1,0,0,0),
    'g':(0,1,0,0,0,0,1),
    'h':(1,0,0,1,0,0,0),
    'n':(1,1,0,1,0,1,0),
    'r':(1,1,1,1,0,1,0),
    'S':(0,1,0,0,1,0,0),
    't':(1,1,1,0,0,0,0),
    'y':(1,0,0,0,1,0,0),
    'i':(1,1,1,1,0,0,1),
    'o':(1,1,0,0,0,1,0),
    'u':(1,1,0,0,0,1,1)
       }




#(year, month, mday, hour, minute, second, weekday, yearday)
def countdown(start):
   i=start
   while (i>0):  
     s="% 4s" % str(i)
     space()
     for digit in range(0,4):
        for loop in range(0,7):
            #print (digits[digit],segments[loop],num[s[digit]][loop])
            place=Pin(digits[digit], Pin.OUT, value=1)
            show=Pin(segments[loop], Pin.OUT, value=num[s[digit]][loop])
        disp=Pin(digits[digit], Pin.OUT, value=1)
        time.sleep(0.003)
        disp=Pin(digits[digit], Pin.OUT, value=0)
     i=i-1

def countup(start):
   i=1
   j=start
   jj="% 4s" % str(j)
   while (i<start):  
     s="% 4s" % str(i)
     space()
     for digit in range(0,4):
        for loop in range(0,7):
            #print (digits[digit],segments[loop],num[s[digit]][loop])
            place=Pin(digits[digit], Pin.OUT, value=1)
            show=Pin(segments[loop], Pin.OUT, value=num[s[digit]][loop])
        
        disp=Pin(digits[digit], Pin.OUT, value=1)
        time.sleep(0.003)
        disp=Pin(digits[digit], Pin.OUT, value=0)
        if (i<start):
            i=i+1
        else:
            i=i+start
        #disp=Pin(digits[0], Pin.OUT, value=0)

def seg():
    for digit in range(0,4):
        for loop in range(0,7):
          place=Pin(digits[digit], Pin.OUT, value=0)
          #print (digits[digit],num[display_string[digit]][loop])
          show=Pin(segments[loop], Pin.OUT, value=num[display_string[digit]][loop]) 
        disp=Pin(digits[digit], Pin.OUT, value=1)
        time.sleep(0.003)
        disp=Pin(digits[digit], Pin.OUT, value=0)

led = Pin(25,Pin.OUT)




def go(timer):
    led.on()
    countdown(brushTime)
    
 

while True:
    led.off()
    for i in range(0,100):
        display_string = ' tth'
        seg()
        i+=1


