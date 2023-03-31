#Capastive touch test

#remote station

import utime
import rp2
from rp2 import PIO, asm_pio
from machine import Pin, mem32, PWM
import connectToWlan
from hcsr04 import HCSR04
import urequests as requests
 
ipInfo= connectToWlan.connectWLAN()
print(ipInfo)


print("Busy/Availble Remote Station")

testBoard= False

if testBoard == True:
    
    busyLedPin = 17
    availableLedPin = 18
    echoPin = 27
    trigPin = 26
    
elif testBoard == False:
    busyLedPin = 28
    availableLedPin = 27
    blueLedPin = 26
    echoPin = 6
    trigPin = 7
    
#Lower LED value
busyLed = Pin(busyLedPin, Pin.OUT)
availableLed = Pin(availableLedPin, Pin.OUT)
blueLed = Pin(blueLedPin, Pin.OUT)

busyPWM = PWM(busyLed)
availablePWM = PWM(availableLed)
bluePWM = PWM(blueLed)

busyPWM.freq(1000)
availablePWM.freq(1000)
bluePWM.freq(1000)

bluePWM.duty_u16(20000)
busyPWM.duty_u16(20000)
availablePWM.duty_u16(20000)

 

sensor = HCSR04(trigger_pin=trigPin, echo_pin=echoPin)
 
def getdist():
    distance = sensor.distance_cm()
    return distance


print('Distance:', getdist(), 'cm')


import socket, network
import website

html = website.html

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


global available
available = True

def openSocketStart():
    bluePWM.duty_u16(0)
    busyPWM.duty_u16(40000)
    availablePWM.duty_u16(0)
    print("Open Socket Started")
    global available
    while True:
        try:
            cl = ''
            cl, addr = s.accept()
            request = cl.recv(1024)
            print(request)
            requestString = request
            

            if "Busy=Busy" in requestString:
                busyPWM.duty_u16(15000)
                availablePWM.duty_u16(0)
                available = False
                response = "Busy Ok"
                
                
            elif "Available=Available" in requestString:
                busyPWM.duty_u16(0)
                availablePWM.duty_u16(10000)
                available = True

                response = "Available Ok"
                
            elif "reload=Reload" in requestString:         
                response = "Reload Ok"
            
            elif "getDistance=True" in requestString:
                
                response = str(getdist())
                cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
                cl.send(response)
                cl.close()
                continue
            
            elif "getAvailableStatus" in requestString:
                response = str(available)
                cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
                cl.send(response)
                cl.close()
                continue
                
            else:
                print("not a valid request")
                response =  "Invalid Request"
            
        
            print(response)
            distance = str(getdist())
            #response = html % f""
            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            cl.send(html % f"Response:{response} | Status {available}  | Distance: {distance}")
            cl.close()
           # print(str(requestString).split("duration="))
            #utime.sleep(int(requestString.split("=")))
            #request = requests.get("192.168.88.147/?Available=Available&duration=")
                #print(request.url)
        except Exception as error:
                print(error)
                response = "Not Ok - error: " + str(error)
                cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
                cl.send(response)
                cl.close()

        
        
#request = requests.get(url = "192.168.88.147/?Available=Available&duration=")
#http://192.168.88.147/?Busy=Busy&duration=
#request = requests.get(url = "http://192.168.88.147/?Busy=Busy&duration=")
#utime.sleep(2)
#request = requests.get(url = "http://192.168.88.147/?Available=Available&duration=")

while True:
    #print(getdist())
   # utime.sleep(.5)
    openSocketStart()
    


