
#blink two LEDs
#Works!
# Version 1.0.0 Done
# 

import time
from machine import Pin
from time import sleep
import random

wLed = 28
 
rButt = 27
 
gButt = 26
 

#redLed = Pin(rLed, Pin.OUT)
#greenLed = Pin(gLed, Pin.OUT)
onBoardLed = Pin("LED", Pin.OUT)
whiteLed = Pin(wLed, Pin.OUT)

whiteLed.value(1)
onBoardLed.value(1)
sleep(1)
whiteLed.value(0)
onBoardLed.value(0)

#buzzer = Pin(buzz, Pin.OUT)

redButton = Pin(rButt, Pin.IN, Pin.PULL_UP)
greenButton = Pin(gButt, Pin.IN, Pin.PULL_UP)
#buzzer = Pin(buzz, Pin.IN, Pin.PULL_UP)

#allLeds = [redLed, greenLed, onBoardLed]


#allLeds = [redLed, greenLed, onBoardLed]

def greenWon(pin):
    print("Green Won")
    print(pin)
    
def redWon():
    print("Red Won")
    


while True:
    print("Starting Game")
    #print(f"Green: {greens} \n Red: {reds}")
    time = random.uniform(3, 10)
    onBoardLed.value(0)
    sleep(time)
    print("LED ON")
    whiteLed.value(1)
    onBoardLed.value(1)
    
    #greenButton.irq(trigger=Pin.IRQ_RISING, handler=greenWon)
    #redButton.irq(trigger=Pin.IRQ_RISING, handler=redWon)
    
    while True:
        
        if greenButton.value() == 0:
            # += 1

            print("Player Green wins!")
            #tprint(f"Green: {greens}")
            
            for x in range(0, 5):
                whiteLed.value(0)
                onBoardLed.value(0)
                sleep(.6)
                whiteLed.value(1)
                onBoardLed.value(1)
                sleep(.2)

            
            break
        
        if redButton.value() == 0:
            #reds += 1
            print("Player Red wins!")
            #tprint(f"Red: {reds}")
            
            for x in range(0, 2):
                whiteLed.value(0)
                onBoardLed.value(0)
                sleep(1)
                whiteLed.value(1)
                onBoardLed.value(1)
                sleep(2)
            
            #print(str(datetime.now())[14:])
            break
        

    whiteLed.value(0)
    onBoardLed.value(0)

 
    

