from machine import Pin
from utime import sleep

#  _ - a
# |_|- f,g,b
# |_|- e,d,c

#    _   _       _   _   _   _   _   _       _                  
# |  _|  _| |_| |_  |_    | |_| |_| | |  _  |_   _   _   _   _  
# | |_   _|   |  _|.|_|   | |_|  _| |_|     |_  |   |   |_| |   


            #a,b,c,d,e,f,g,d1
segments = (25,14,15,25,14,25,25,13)
#7seg_segment_pins (14,16,13,3,5,11,15,7)


for segment in segments:
    Pin(segment,Pin.OUT)
    
    

    
num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)} 

