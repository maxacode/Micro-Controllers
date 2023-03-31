#ULTRASONIC GARAGE PARKING ASSISTANT


import _thread
from machine import Pin
import utime
import network, socket

triggerPin = 14
echoPin = 15
bluePin = 19
greenPin =20
redPin= 21


trigger = Pin(triggerPin, Pin.OUT)
echo = Pin(echoPin, Pin.IN)
tofar = Pin(bluePin, Pin.OUT)
justright = Pin(greenPin, Pin.OUT)
toclose = Pin(redPin, Pin.OUT)

red = "toclose"
green = "justright"
blue = "tofar"

# Distance varaibles
global justrightcm, toclosecm, tofarcm

def getConfigs():
    with open("config.ini", "r") as data:
        dataDict = data.read().split()
        
        global justrightcm, toclosecm, tofarcm


        justrightcm= int(dataDict[0].split("=", 1)[1])
        tofarcm= int(dataDict[1].split("=", 1)[1])
        toclosecm= int(dataDict[2].split("=", 1)[1])

        print(justrightcm, tofarcm, toclosecm)
        
getConfigs()


justright.value(1)
toclose.value(1)
tofar.value(1)


import website

html = website.html



import connectToWlan

ssid = 'Tell My Wi-Fi Love Her'
password = 'GodIsGood!'

ipInfo= connectToWlan.connectWLAN(ssid, password)
print(ipInfo)



 
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
                 
     
        break
    except Exception as e:
        print(f"except 68: {e}")
        utime.sleep_us(5)
        pass

def openSocket():
    global justrightcm, tofarcm, toclosecm

    # Listen for connections, serve client
    while True:
    
        
        print("justrightcm line 96: ", justrightcm)

        cl, addr = s.accept()

       # print('client connected from', addr)
        request = cl.recv(1024)
        #print("request:")
        print(request)
        request = str(request)
        
        
       # led_on = request.find('led=on')
       # led_off = request.find('led=off')
        
        #print( 'led on = ' + str(led_on))
       # print( 'led off = ' + str(led_off))
       
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
            tofarcmd += 5
            print(tofar)
            
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
        print(newConfig)
        with open('config.ini', 'w') as data:
            data.write(newConfig)
        
        #getConfigs()
            
        #ledState = "LED is OFF" if led.value() == 0 else "LED is ON" # a compact if-else statement

        # Create and send response
        
        response = html % f"{distanceOutput} <br> Just Right Distance {justrightcm} cm <br> To Far Distance: {tofarcm} cm <br> To Close Distance: {toclosecm} cm"
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
   

        
  




def ultra():
    

   #print("ultra start")
    while True:
        justright.value(1)
        toclose.value(1)
        tofar.value(1)
        
        trigger.low()
        utime.sleep_us(2)
        trigger.high()
        utime.sleep_us(5)
        trigger.low()
       # print(echo.value())
       # print(trigger.value())
        while echo.value() == 0:
           signaloff = utime.ticks_us()
           #print(signaloff)
        while echo.value() == 1:
           signalon = utime.ticks_us()
          # print(signalon)
        timepassed = signalon - signaloff
       # print(timepassed)
        distance = (timepassed * 0.0343) / 2
        
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
        print(distanceOutput)
        utime.sleep(3)
        #openSocket()
        #print(ipInfo)
         
         
#while True:
utime.sleep(2)
#openSocket_thread = _thread.start_new_thread(openSocket, ())
ultra_thread = _thread.start_new_thread(ultra, ())
openSocket()
     





#while True:
    #print("ultra Function Call")
#ultra()
#    utime.sleep(1)
   
print("end")
