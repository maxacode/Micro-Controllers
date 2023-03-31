#rgbLED Strip - 12v + R+G+B
# control rgbLED with 4 pins: +12v, R,G,B

from machine import Pin
from time import sleep

green = Pin(15, Pin.OUT)
red = Pin(13, Pin.OUT)
blue = Pin(14, Pin.OUT)
red.value(0)
green.value(0)
blue.value(0)


# go through all of them 
red.value(1)
sleep(2)
red.value(0)
green.value(1)

sleep(2)
green.value(0)
blue.value(1)


# all ON - CYAN/White
sleep(2)
green.value(1)
red.value(1)




