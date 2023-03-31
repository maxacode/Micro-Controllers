#Capastive touch test

#base station

import utime
import rp2
from rp2 import PIO, asm_pio
from machine import Pin, mem32, PWM
import connectToWlan

import urequests as requests
 
ipInfo= connectToWlan.connectWLAN()
print(ipInfo)

 


testBoard= False

if testBoard == True:
    
    busyLedPin = 5
    availableLedPin = 6
    blueLedPin = 7
    
elif testBoard == False:
    busyLedPin = 26
    availableLedPin = 27
    #blueLedPin = 26
    busyButtPin = 16
    availableButtPin =0 
    
 
busyButt = Pin(busyButtPin, Pin.IN, Pin.PULL_UP)
availableButt = Pin(availableButtPin, Pin.IN, Pin.PULL_UP)



busyLed = Pin(busyLedPin, Pin.OUT)
availableLed = Pin(availableLedPin, Pin.OUT)
#blueLed = Pin(blueLedPin, Pin.OUT)

busyPWM = PWM(busyLed)
availablePWM = PWM(availableLed)
#bluePWM = PWM(blueLed)

busyPWM.freq(1000)
availablePWM.freq(1000)
#bluePWM.freq(1000)

#bluePWM.duty_u16(20000)
busyPWM.duty_u16(20000)
availablePWM.duty_u16(20000)

import socket, network
#import website

#html = website.html

# Open socket
while True:
    try:
        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        s = socket.socket()
        s.bind(addr)
        s.listen(50)
        print('listening on', addr)
        break
    except Exception as e:
        print(f"except 68: {e}")
        utime.sleep(0)
        pass

        
        
#request = requests.get(url = "192.168.88.147/?Available=Available&duration=")
#http://192.168.88.147/?Busy=Busy&duration=
#request = requests.get(url = "http://192.168.88.147/?Busy=Busy&duration=")
#utime.sleep(2)
#request = requests.get(url = "http://192.168.88.147/?Available=Available&duration=")

#remoteIP = "http://192.168.88.153"
remoteIP = "http://192.168.88.143"

setBusyAPI = "Busy=Busy"
setAvailableAPI = "Available=Available"
getStatusAPI = "getAvailableStatus"
getDistanceAPI = "getDistance=True"

alertDistance = 500
refreshRate = .2

def baseButtonListner():
    #print(f"busy: " , busyButt.value())
    #print("available: ", availableButt.value())
    
    if busyButt.value() == 0 and availableButt.value() == 0:
        print("sleeping until both pressed again")
        availablePWM.duty_u16(0)
        busyPWM.duty_u16(0)
        getStatus()
        utime.sleep(10)
        while True:
            print("in sleep")
            utime.sleep(refreshRate)
            if busyButt.value() == 0 and availableButt.value() == 0:
                
                print("getting outta sleep")
                availablePWM.duty_u16(40000)
                busyPWM.duty_u16(40000)
                utime.sleep(.5)
                getStatus()
                break
            
    elif busyButt.value() == 0:
        makeAPICall(setBusyAPI)
        getStatus()
        
    elif availableButt.value() == 0:
        makeAPICall(setAvailableAPI)
        getStatus()
    
    #print(220)
    remoteDistanceGetter()
    
    utime.sleep(refreshRate)
    
def getStatus():
    res = makeAPICall(getStatusAPI)

    if res.text == "True":
        #availablePWM.duty_u16(4000)
        availablePWM.duty_u16(40000)

        busyPWM.duty_u16(0)

    elif res.text == "False":
        availablePWM.duty_u16(0)
        #busyPWM.duty_u16(4000)
        busyPWM.duty_u16(40000)

        

def makeAPICall(var):
    #print("makeAPIcall Func")

    url = f"{remoteIP}/{var}"
    while True:
        try:
           # print(151)
            request = requests.get(url, timeout=5)
         #   print(153)
            break
        except Exception as E:
            print(E)
           # print(157)
            utime.sleep(1)
        
    #print(160)
    print(request.text)
   # print(162)
    return request

def remoteDistanceGetter():
    #print("remoteDistanceGetter Func")
    request = makeAPICall(getDistanceAPI)
    distance = float(request.text)
    #print(f"Distance: {int(distance/1)} cm")
    if distance <= alertDistance:
        refreshRate = 0
        print("INCOMING")
        for x in range(3):
            utime.sleep(.1)
            availablePWM.duty_u16(60000)
            busyPWM.duty_u16(600000)
            availablePWM.duty_u16(0)
            busyPWM.duty_u16(0)
        getStatus()    
    if distance >= alertDistance:
        #getStatus()
        refreshRate = .2

    #return distance
    utime.sleep(refreshRate)
    

while True:
    #openSocketStart()
    #remoteDistanceGetter()
    getStatus()
    baseButtonListner()

