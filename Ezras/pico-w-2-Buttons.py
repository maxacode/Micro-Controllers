
# Ezra Game
# Pico W
# Red button blinks it X times
# Green button is a momentary switch - can change to Latching with .toggle()

import time
from machine import Pin
from time import sleep
import random

import connectToWLAN
import website


#print(connectToWLAN.ssid)

ssid = 'Tell My Wi-Fi Love Her'
password = 'GodIsGood!'


#dconnectToWLAN.connectWLAN(ssid, password)


wLed = 28
 
rButt = 27
 
gButt = 26
 
wRGB = 21
rRGB = 20
gRGB = 19
bRGB = 18

#redLed = Pin(rLed, Pin.OUT)
#greenLed = Pin(gLed, Pin.OUT)
onBoardLed = Pin("LED", Pin.OUT)
whiteLed = Pin(wLed, Pin.OUT)

 
whRGB = Pin(wRGB, Pin.OUT)
reRGB = Pin(wRGB, Pin.OUT)
grRGB = Pin(gRGB, Pin.OUT)
blRGB = Pin(bRGB, Pin.OUT)


whiteLed.value(1)
onBoardLed.value(1)
reRGB.value(1)
grRGB.value(1)
blRGB.value(1)

sleep(1)
whiteLed.value(0)
onBoardLed.value(0)

#buzzer = Pin(buzz, Pin.OUT)

redButton = Pin(rButt, Pin.IN, Pin.PULL_UP)
greenButton = Pin(gButt, Pin.IN, Pin.PULL_UP)
#buzzer = Pin(buzz, Pin.IN, Pin.PULL_UP)

#allLeds = [redLed, greenLed, onBoardLed]

def ezraLedGame():
    for x in range(0, 3):
        whiteLed.value(1)
        sleep(.2)
        whiteLed.value(0)
        sleep(.1)
    while True:
        whiteLed.value(0)
        login_state = redButton.value()
        login_state2 = greenButton.value()
        if login_state == False:
            for x in range(0, 3):
                whiteLed.value(1)
                sleep(.3)
                whiteLed.value(0)
                sleep(.2)
            print("Red on")
        elif login_state2 == False:
            
            whiteLed.value(1)
            #print("green on")
       
        
if __name__ == "__main__":
    connectToWLAN.connectWLAN(ssid, password, 'FO')
    ezraLedGame()

 
