#testClass.py
# Take IR On - then off/special flash

#testClass.py

import time
from machine import Pin
#from pyb import LED
from ir_rx.nec import NEC_8  # NEC remote, 8 bit addresses

blue = Pin(0, Pin.OUT)
red = Pin(1, Pin.OUT)
green = Pin(2, Pin.OUT)
red.toggle()
    
# 88 red, 89 green, 69 blue
redIR= '88'
greenIR = '89'
blueIR = '69'
offFactor = 99

redIROff= '188'
greenIROff = '187'
blueIROff = '168'

irOff = {'redIROff': 188,'greenIROff': 187, 'blueIRoff': 168}
"""
withOUT Data 188 Addr 0
REd toggleed

withOUT Data 187 Addr 0

withOUT Data 168 Addr 0"""
def flashLed(led, count=3, speed= 0.5 ):
    print(f"Flashing: led: {led} count: {count}")
    while count >= 0:
        count-=1
        led.toggle()
        time.sleep(speed)
        led.toggle()
        time.sleep(speed)
   
def callback(data, addr, ctrl):
    if data < 0:  # NEC protocol sends repeat codes.
        pass
        print('Repeat code.')
    else:
       # print("With OUT :02x and :04x")
        print('withOUT Data {} Addr {}'.format(data, addr))
        if redIR in str(data):
            print("REd toggleed")
            red.toggle()
        elif greenIR in str(data):
            print("GREEN toggleed")
            green.toggle()
        elif blueIR in str(data):
            print("BLUE toggleed")
            blue.toggle()
        
        if redIROff in str(data):
            print("REd OFF toggleed")
            flashLed(red)
        elif greenIROff in str(data):
            print("GREEN OFF toggleed")
            flashLed(green)
        elif blueIROff in str(data):
            print("BLUE OFF toggleed")
            flashLed(blue, 6, 0.2)
        
  
            
           
            
            
            
            
        #print("With :02x and :04x")
        #print('WITH Data {:04x} Addr {:04x}'.format(data, addr))
        #print()
        print()
ir = NEC_8(Pin(16, Pin.IN), callback)



while True:
    time.sleep_ms(500)
    #red.toggle()
    #red.toggle()
    


