# Game for Raspberry Pi Zero H
# Two Button Red/Green + 3 Led's Red/Green/White
# Who presses thier button faster gets a point. 

# Buildings Blocks:
"""

#blink two LEDs
#red LED = 22/Gp17
#green LED = 21/GP16
#23 Grnd
#greenButt = 10/GP7
#redButt 16/Gp12

import time
from machine import Pin

obLed = 25
rLed = 17
rButt = 12
gLed = 16
gButt = 7


redLed = Pin(rLed, Pin.OUT)
greenLed = Pin(gLed, Pin.OUT)
onBoardLed = Pin(obLed, Pin.OUT)

redButton = Pin(rButt, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(gButt, Pin.IN, Pin.PULL_DOWN)

allLeds = [redLed, greenLed, onBoardLed]

for LED in allLeds:
    print(f' {LED} is: {LED}')
    LED.toggle()
    print(redButton.value())
    print(greenButton.value())

    time.sleep(1)
    
    #LED.toggle()

    
    
"""