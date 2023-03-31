
#blink two LEDs
#red LED = 22/Gp17
#green LED = 21/GP16
#whiteLed = 24/GP18
#buzzerIO = 25/GP 19
#23 Grnd
#greenButt = 10/GP7
#redButt 16/Gp12

import time
from machine import Pin

wLed = 28
obLed = 25
#rLed = 17
rButt = 27
#gLed = 16
gButt = 28
#buzz = 19

#redLed = Pin(rLed, Pin.OUT)
#greenLed = Pin(gLed, Pin.OUT)
onBoardLed = Pin(obLed, Pin.OUT)
whiteLed = Pin(wLed, Pin.OUT)

onBoardLed.value(1)

#buzzer = Pin(buzz, Pin.OUT)

redButton = Pin(rButt, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(gButt, Pin.IN, Pin.PULL_DOWN)
#buzzer = Pin(buzz, Pin.IN, Pin.PULL_UP)

#allLeds = [redLed, greenLed, onBoardLed]



while True:
    whiteLed.value(0)
 

    redLed.value(redButton.value())
    greenLed.value(greenButton.value())
    
    if greenButton.value() == 1 and redButton.value() == 1:
        print("White LED on")
        whiteLed.value(1)
    else:
        #print("White LED off")
        whiteLed.value(0)
    time.sleep(.5)
 

for LED in allLeds:
    print(f' {LED} is: {LED}')
    LED.toggle()
    print(redButton.value())
    print(greenButton.value())

    time.sleep(1)
    
    #LED.toggle()

    
    


