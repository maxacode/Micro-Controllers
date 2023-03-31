# Multi switch - Dip switch
# 1 up - Ezra game
# 2 up - who's faster
# Todo:
# Split them up into seperate libraries and just import/call function when needed. 
#blink two LEDs
#red LED = 22/Gp17
#green LED = 21/GP16
#whiteLed = 24/GP18
#buzzerIO = 25/GP 19
#23 Grnd
#greenButt = 10/GP7
#redButt 16/Gp12

from machine import Pin
from time import sleep
import random

#import connectToWLAN
#import website


#print(connectToWLAN.ssid)

ssid = 'Tell My Wi-Fi Love Her'
password = 'GodIsGood!'


#dconnectToWLAN.connectWLAN(ssid, password)

dipvar1 = 3
dipvar2 = 2

#wLed = 28
 
rButt = 18
gButt = 26
 
 
rRGB = 15
gRGB = 28
bRGB = 1

#redLed = Pin(rLed, Pin.OUT)
#greenLed = Pin(gLed, Pin.OUT)
onBoardLed = Pin("LED", Pin.OUT)
#whiteLed = Pin(wLed, Pin.OUT)

 

reRGB = Pin(rRGB, Pin.OUT)
grRGB = Pin(gRGB, Pin.OUT)
blRGB = Pin(bRGB, Pin.OUT)
dip1 = Pin(dipvar1, Pin.IN, Pin.PULL_UP)
dip2 = Pin(dipvar2, Pin.IN, Pin.PULL_UP)


reRGB.value(0)
grRGB.value(0)
blRGB.value(0)

onBoardLed.value(1)
reRGB.value(1)
sleep(.2)
reRGB.value(0)
grRGB.value(1)
sleep(.2)
grRGB.value(0)
blRGB.value(1)
sleep(.2)

onBoardLed.value(1)
reRGB.value(0)
grRGB.value(0)
blRGB.value(0)


#buzzer = Pin(buzz, Pin.OUT)

redButton = Pin(rButt, Pin.IN, Pin.PULL_UP)
greenButton = Pin(gButt, Pin.IN, Pin.PULL_UP)


#buzzer = Pin(buzz, Pin.IN, Pin.PULL_UP)

#allLeds = [redLed, greenLed, onBoardLed]

def ezraLedGame():
    while True:
        reRGB.value(0)
        grRGB.value(0)
        blRGB.value(0)

        login_state = redButton.value()
        login_state2 = greenButton.value()
        if login_state == False and login_state2 == False:
            print("Both On")
            for x in range(0, 3):
                reRGB.value(1)
                grRGB.value(1)
                blRGB.value(0)

                sleep(.2)
                reRGB.value(0)
                grRGB.value(0)
                blRGB.value(1)
                sleep(.1)
                
        elif login_state == False:
            print("Red on")
            for x in range(0, 3):
                reRGB.value(1)
                sleep(.1)
                reRGB.value(0)
                sleep(.1)
            
        elif login_state2 == False:
            grRGB.value(1)
            #print("green on")
            
     

def speedGame():
    print("Speed game")
    
    
    while True:
        reRGB.value(0)
        grRGB.value(0)
        blRGB.value(0)
        print("Starting Game")
        #print(f"Green: {greens} \n Red: {reds}")
        time = random.uniform(2, 7)
        sleep(time)
        print("LED ON")
        blRGB.value(1)
        
        
        #greenButton.irq(trigger=Pin.IRQ_RISING, handler=greenWon)
        #redButton.irq(trigger=Pin.IRQ_RISING, handler=redWon)
        
        while True:
            
            if greenButton.value() == 0:
                # += 1
                blRGB.value(0)
                print("Player Green wins!")
                #tprint(f"Green: {greens}")
                
                grRGB.value(1)
                sleep(2)
                
                break
            
            if redButton.value() == 0:
                #reds += 1
                blRGB.value(0)
                print("Player Red wins!")
                #tprint(f"Red: {reds}")
                
                reRGB.value(1)
                sleep(2)
                break
            
                
            
     
       
        
        
if __name__ == "__main__":
    #connectToWLAN.connectWLAN(ssid, password, 'FO')


    print(f'dip 1. ON {dip1.value()}')
    print(f'dip 2. ON {dip2.value()}')

    if not dip1.value():
        
        print(f'dip 1. ON {dip1.value()}')
        print("ezra game")
        for x in range(0, 3):
            reRGB.value(1)
            grRGB.value(1)
            sleep(.5)
            reRGB.value(0)
            grRGB.value(0)
            sleep(.2)
            
        
        ezraLedGame()

    elif not dip2.value():
        print(f'dip 2. ON {dip2.value()}')
        print("Starting SPeed game")
        for x in range(0, 5):
            blRGB.value(0)
            sleep(.3)
            blRGB.value(1)
            sleep(.65)
            
        speedGame()
        
    else:
        print("None of the dips in right config, running Ezras Game")
       # ezraLedGame()


 
