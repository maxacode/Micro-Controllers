#ULTRASONIC GARAGE PARKING ASSISTANT
# Tesla

import _thread
from machine import Pin
import utime
import network, socket

versionNumber = 1.9

triggerPin = 8
echoPin = 9
greenPin = 27
redPin= 28
bluePin = 26
withDisplay = False

global justright, toclose
trigger = Pin(triggerPin, Pin.OUT)
echo = Pin(echoPin, Pin.IN)


justright = Pin(greenPin, Pin.OUT)
toclose = Pin(redPin, Pin.OUT)
tofar = Pin(bluePin, Pin.OUT)

red = "toclose"
green = "justright"
blue = "tofar"
 

import website

html = website.html



import connectToWlan

ssid = 'Tell My Wi-Fi Love Her'
password = 'GodIsGood!'

ipInfo= connectToWlan.connectWLAN(ssid, password)
print(ipInfo)

from machine import Pin

if withDisplay:
    from machine import I2C
    from ssd1306 import SSD1306_I2C
    import framebuf
    WIDTH = 128
    HEIGHT = 32
    sclPin = 17
    sdaPin = 16
    i2c = I2C(0, scl = Pin(sclPin), sda = Pin(sdaPin), freq=400000)
    display = SSD1306_I2C(WIDTH, HEIGHT, i2c)
    display.text(f"WiFi Network: ", 0, 0)
    display.text(ssid, 0, 10)
    display.text("5 Seconds Only", 0, 20)
    display.show()
        

import time





# Distance varaibles
global justrightcm, toclosecm, tofarcm

def getConfigs():
    #with open("config.ini", "r") as data:
    with open("config.py", "r") as data:
    
        dataDict = data.read().split()
        
        global justrightcm, toclosecm, tofarcm


        justrightcm= int(dataDict[0].split("=", 1)[1])
        tofarcm= int(dataDict[1].split("=", 1)[1])
        toclosecm= int(dataDict[2].split("=", 1)[1])

        print(justrightcm, tofarcm, toclosecm)
        
getConfigs()


justright.value(1)
toclose.value(1)




 

def showDisplay():
    try:
        #while True:+=\
        print("showing display")
        display.fill(0)

        display.text('Grg Prk Asst',0,0)
        # temperature = read_temp()
        ipAddr = ipInfo.split(",")[0][7:-1]
        display.text(ipAddr,0,9)
        #display.text("test123456789abc",0,18)
        #display.text("test2",0,24)
        display.text(f"JR {justrightcm} TF{tofarcm} TC{toclosecm}", 0, 17)
        display.text(f"{distance} cm",0,25)

        display.show()
        # display.fill(0)
    except:
        pass
        
    

    

  
    


    
#utime.sleep(3)

 
# Open socket
while True:
    try:
        print(53)
        
        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
      #  print(addr)
      #  print(55)
        s = socket.socket()
      #  print(57)
        s.bind(addr)
       # print(59)
        s.listen(50)
        print('listening on', addr)
        if withDisplay:
            display.fill(0)
            display.text("Connection Est", 0,10)
            display.text(str(versionNumber),0,20)
            display.show()
        
        break
    except Exception as e:
        print(f"except 68: {e}")
        if withDisplay:

            display.fill(0)
            display.text(f"Excep 68: {e}", 0, 10)
            display.text("Please Reboot", 0, 20)
            display.show()

        utime.sleep(.1)
        pass
    


def openSocket():
    global justrightcm, tofarcm, toclosecm
    print("opensocket started")
    # Listen for connections, serve client
    while True:
    
        
       # print("justrightcm line 96: ", justrightcm)

        cl, addr = s.accept()

       # print('client connected from', addr)
        request = cl.recv(1024)
        #print("request:")
        print(request)
        request = str(request)
        
        
 
       
        if "justrightAdd" in request:
            print("justrightAdd")
            justrightcm += 5
            print(justrightcm)
            
        elif "justrightMinus" in request:
            print("justrightMinus")
            justrightcm -= 5
            print(justrightcm)
            
        if "tofarAdd" in request:
            print("tofarAdd")
            tofarcm += 5
            print(tofarcm)
            
        elif "tofarMinus" in request:
            print("tofarMinus")
            tofarcm -= 5
            print(tofarcm)
        
        if "tocloseAdd" in request:
            print("tocloseAdd")
            toclosecm += 5
            print(toclosecm)
            
        elif "tocloseMinus" in request:
            print("tocloseMinus")
            toclosecm -= 5
            print(toclosecm)
        
        newConfig = f"""
    justrightcm={justrightcm}
    tofarcm={tofarcm}
    toclosecm={toclosecm}
    """
        if withDisplay:

            display.fill(0)
            display.text(f"justrightcm={justrightcm}", 0, 0)
            display.text(f"tofarcm={tofarcm}", 0, 9)
            display.text(f"toclosecm={toclosecm}", 0, 16)
            display.text(f"{addr}[3:-3]", 0,25)
            display.show()
        
        print(newConfig)
        with open('config.py', 'w') as data:
            data.write(newConfig)
        
         
        #getConfigs()
            
        #ledState = "LED is OFF" if led.value() == 0 else "LED is ON" # a compact if-else statement

        # Create and send response
        
        response = html % f"{distanceOutput} <br> Just Right Distance {justrightcm} cm <br> To Far Distance: {tofarcm} cm <br> To Close Distance: {toclosecm} cm"
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
   

        
  




def ultra(echo, trigger, justright, toclose, tofar, utime, withDisplay):
    

    print("ultra start")
    
    #from hcsr04 import HCSR04

   # sensor = HCSR04(trigger_pin=8, echo_pin=9)


    while True:
        #global justright, toclose
        #justright.value(1)
        #toclose.value(1)
        tofar.value(1)

        global distance
        trigger.low()
        utime.sleep_us(2)
        trigger.high()
        utime.sleep_us(5)
        trigger.low()
    # print(echo.value())
    # print(trigger.value())
        
        # try:
        print("Trying sensor")
        while echo.value() == 0:
            print("echo = 0 ")
            signaloff = utime.ticks_us()

        while echo.value() == 1:
            print("echo = 1 ")
            
            signalon = utime.ticks_us()

        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2

        #distance = sensor.distance_mm()

        print('Distance:', distance, 'cm')
        #print(f"Distance: {distance}")
            #break
        # except Exception as E:
        #     print(f"---\n {E} --- \n No connection to UltraSonic Sensor - Trying again in 2 Seconds")
        #     utime.sleep(1)
            
        
        #chanign folor of LED based on distancec
        if distance <= toclosecm:
            print("TOOO CLOSE")
            justright.value(0)
            toclose.value(1)
            tofar.value(0)
            
        elif distance <= justrightcm:
            print("just right")
            justright.value(1)
            toclose.value(0)
            tofar.value(0)
            
            
        elif distance <= tofarcm:
            print("to Far")
            justright.value(0)
            toclose.value(0)
            tofar.value(1)
            
        global distanceOutput
        distanceOutput =  f"The distance from object is {distance} cm"
        if withDisplay:
            showDisplay()
            
        print(distanceOutput)
        utime.sleep(1)
        #continue
        #openSocket()
        #print(ipInfo)

            
         
         
#while True:
#utime.sleep(2)
#openSocket_thread = _thread.start_new_thread(openSocket, ())
print('starting ultra thread')

ultra_thread = _thread.start_new_thread(ultra, (echo, trigger, justright, toclose,tofar, utime, withDisplay))
#ultra(echo, trigger, justright, toclose,tofar, utime, withDisplay)
print("starting openSocket function")
openSocket()  





#while True:
    #print("ultra Function Call")
#ultra()
#    utime.sleep(1)
   
print("end")

