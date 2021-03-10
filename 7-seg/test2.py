from machine import Pin
import time
import utime

t=0.2
#  _ - a
# |_|- f,g,b
# |_|- e,d,c



aP,bP,cP,dP,eP,fP,gP,decP=(15,14,13,12,11,10,9,8)


a=Pin(aP, Pin.OUT)
b=Pin(bP, Pin.OUT)
c=Pin(cP, Pin.OUT)
d=Pin(dP, Pin.OUT)
e=Pin(eP, Pin.OUT)
f=Pin(fP, Pin.OUT)
g=Pin(gP, Pin.OUT)
dec=Pin(decP, Pin.OUT,value=0)

#digits = (12,11,10,9)
#digits = (9,10,11,12)
digits = (2,3,4,5)
for i in range(0,4):
 di=(Pin(digits[i], Pin.OUT,value=0))

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

segments = (15,16,17,14,13,18,19)

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
    '9':(0,0,0,0,1,0,0)}

def zero():
    a.off()
    b.off()
    c.off()
    d.off()
    e.off()
    f.off()
    g.on()

def one():
    a.on()
    b.off()
    c.off()
    d.on()
    e.on()
    f.on()
    g.on()

def two():
    a.off()
    b.off()
    c.on()
    d.off()
    e.off()
    f.on()
    g.off()
    
def three():
    f.on()
    e.on()
    a.off()
    b.off()
    c.off()
    d.off()
    g.off()
    
def four():
    a.on()
    e.on()
    d.on()
    b.off()
    c.off()
    f.off()
    g.off()
    
def five():
    b.on()
    e.on()
    a.off()
    c.off()
    d.off()
    f.off()
    g.off()
    
def six():
    b.on()
    a.off()
    c.off()
    d.off()
    e.off()
    f.off()
    g.off()

def seven():
    e.on()
    f.on()
    g.on()
    a.off()
    b.off()
    c.off()
    d.on()

def eight():
    a.off()
    b.off()
    c.off()
    d.off()
    e.off()
    f.off()
    g.off()

def nine():
    e.on()
    d.on()
    a.off()
    b.off()
    c.off()
    f.off()
    g.off()

def space():
    e.on()
    d.on()
    a.on()
    b.on()
    c.on()
    f.on()
    g.on()
    
def count(t):
    one()
    time.sleep(t)
    two()
    time.sleep(t)
    three()
    time.sleep(t)
    four()
    time.sleep(t)
    five()
    time.sleep(t)
    six()
    time.sleep(t)
    seven()
    time.sleep(t)
    eight()
    time.sleep(t)
    nine()
    time.sleep(t)
    zero()
    time.sleep(t)
no=1
#(year, month, mday, hour, minute, second, weekday, yearday)
while True:
 #n=time.gmtime()

 #num=n[0]

 s="% 4s" % str(no)
 space()
 for digit in range(0,4):
        for loop in range(0,7):
            #print (digits[digit],segments[loop],num[s[digit]][loop])
            place=Pin(digits[digit], Pin.OUT, value=1)
            show=Pin(segments[loop], Pin.OUT, value=num[s[digit]][loop])

        disp=Pin(digits[digit], Pin.OUT, value=1)
        time.sleep(0.003)
        disp=Pin(digits[digit], Pin.OUT, value=0)
        if (no==9999):
            no=1
        else:
            no=no+1
            
            