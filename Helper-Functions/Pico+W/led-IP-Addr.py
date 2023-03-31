# A simple example that:
# - Connects to a WiFi Network defined by "ssid" and "password"
# - Blinks out the Last OCtet of the IP address from DHCP
"""
3 times on Connect Attempt, 
Long 3 second hold if connected
if Fail sleep 3 seconds then 3 times for 4 attempts then blinks 10 times when failed.
3 fast between octets
X per first # in last octent, etc etc

"""

import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests
from machine import Pin
import time

#on board pin
led = Pin("LED", Pin.OUT)
led.value(1)
time.sleep(.1)
led.value(0)


# Fill in your network name (ssid) and password here:
ssid = 'Tell My Wi-Fi Love Her'
password = 'GodIsGood!'

#wlan.ifconfig() output:
"""
2. Querying the current GMT+0 time:
Fail: ('0.0.0.0', '255.255.255.0', '192.168.0.1', '8.8.8.8')

Success: ('192.168.88.145', '255.255.255.0', '192.168.88.1', '1.1.1.1')


"""
def saveTime():
    a = 95
    file = open("time.txt", "a")
    timeNOw = time.localtime()
    file.write(timeNOw)
    file.flush()
    a -= 5
    #with open("time.txt", "a") as file:
     #   file.write(time.localtime())
        

#saveTime()

file=open("data.txt","w")	# creation and opening of a CSV file in Write mode
# Type Program Logic Here
file.write(str(time.localtime())+",")# Writing data in the opened file
# file.flush()
# Internal buffer is flushed (not necessary if close() function is used)
file.write("test")
file.flush()
# The file is closed

x = 0 
while x < 5:
    global ipInfo
            
    print("Trying to Connect")
    
    for z in range(0, 3):
        led.value(1)
        time.sleep(.3)
        led.value(0)
        time.sleep(.3)

    # Connect to network
    wlan = network.WLAN(network.STA_IF)
    try:
        network.hostname("raspi-pico-w-NUM-1")
    except:
        pass
    
    try:
        
        wlan.connect(ssid, password)
    except Exception as e:
        print(e)
        pass
    
    #wlan.config(essid=ssid, key=password)

    wlan.active(True)
    
    ipInfo = wlan.ifconfig()
    
    
    if "192.168.88.1" in ipInfo:
        print(f"Success: {ipInfo}")
        file.write(str(ipInfo))
        file.flush()
        #file.close()


           ## Display last octed to LED flash
        lastOctet = int(ipInfo[0].split('.')[3])
        print(lastOctet)
        print(str(lastOctet)[0])
        print(str(lastOctet)[1])
        print(str(lastOctet)[2])
        
     
        
        led.value(1)
        time.sleep(3)
        led.value(0) 
        
     
        if len(str(lastOctet)) >= 1:
            print("Len == 3")
            for z in range(0, 3):
                led.value(1)
                time.sleep(.3)
                led.value(0)
                time.sleep(.1)
            time.sleep(1)
            for y in range(0, int(str(lastOctet)[0])):
                print(f"First Int {str(lastOctet)[0]}")
                led.value(1)
                time.sleep(1)
                led.value(0)
                time.sleep(1)
                
        if len(str(lastOctet)) >= 2:
            for z in range(0, 3):
                led.value(1)
                time.sleep(.3)
                led.value(0)
                time.sleep(.1)
            time.sleep(1)
            for y in range(0, int(str(lastOctet)[1])):
                print(f"Second Int {str(lastOctet)[0]}")
                led.value(1)
                time.sleep(1)
                led.value(0)
                time.sleep(1)
                
        if len(str(lastOctet)) == 3:       
            for z in range(0, 3):
                led.value(1)
                time.sleep(.3)
                led.value(0)
                time.sleep(.1)
            
            time.sleep(1)
            for y in range(0, int(str(lastOctet)[2])):
                print(f"Third Int {str(lastOctet)[0]}")
                
                led.value(1)
                time.sleep(1)
                led.value(0)
                time.sleep(1)

            
        print("Done IP Info LED output")
        for z in range(0, 5):
            led.value(1)
            time.sleep(.3)
            led.value(0)
            time.sleep(.1)
        print("BREAK")
        led.value(1)
        break
    
    else:
        time.sleep(3)
        x += 1 
        if x == 5:
            print("Could Not Connect, blinking 10 times")
            for z in range(0, 10):
                led.value(1)
                time.sleep(1)
                led.value(0)
                time.sleep(.5)

 
file.close()


# Example 1. Make a GET request for google.com and print HTML
# Print the html content from google.com
#print("1. Querying google.com:")
#r = urequests.get("http://www.google.com")
#print(r.content)
#r.close()

# Example 2. urequests can also handle basic json support! Let's get the current time from a server
print("\n\n2. Querying the current GMT+0 time:")
#r = urequests.get("http://date.jsontest.com") # Server that returns the current GMT+0 time.
#print(r.json())
 
 
