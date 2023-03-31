#network library
#pico W
# V1.0 done
# connect to SSID up to 10 attempts then fails.
#USAGE:
# import connectToWlan - thats it. (No NAME==MAIN so code runs directly)

print("Starting Up Device")

import network
import socket
import time
from machine import Pin

led = Pin("LED", Pin.OUT)
led.value(1)

print("Starting WLAN Connection")

ssid = 'Tell My Wi-Fi Love Her'
password = 'GodIsGood!'

def connectWLAN():
    global ipInfo
    
    led = Pin("LED", Pin.OUT)
    led.value(1)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
 
    #wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        print(wlan.status())
        led.toggle()
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for WLAN Connection...')
        time.sleep(1)
        
        
        # Handle connection error
    if wlan.status() != 3:
        print('customRaise: network connection failed')
        
    else:
        print('Connected')
        status = wlan.ifconfig()
        ipInfo = ( f'IP Details = {str(status)}')
        ipAddr = status[0]
        print(ipAddr)
        
        return(ipInfo)
    
connectWLAN()

