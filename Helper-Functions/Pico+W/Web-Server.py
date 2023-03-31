#Web server test
from machine import Pin
#network library to connect to WIFI
import network
import socket
import time

#button 13
butt = 13
whiteled = 14

led = Pin(whiteled, Pin.OUT)
ledStatus = "White Led Status: Unknown"

button = Pin(butt, Pin.IN, Pin.PULL_UP)
led.value(1)

ssid = 'Tell My Wi-Fi Love Her'
password = 'GodIsGood!'


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)


html = """<!DOCTYPE html><html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
.buttonGreen { background-color: #4CAF50; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; }
.buttonRed { background-color: #D11D53; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; }
text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
</style></head>
<body><center><h1>Control Panel</h1></center><br><br>
<form><center>
<center> <button class="buttonGreen" name="led" value="on" type="submit">LED ON</button>
<br><br>
<center> <button class="buttonRed" name="led" value="off" type="submit">LED OFF</button>
</form>
<br><br>
<br><br>
<p>%s<p></body></html>
"""

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
    raise RuntimeError('customRaise: network connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print( f'ip = {str(status)}')
    

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
        pass

# Listen for connections, serve client
while True:
    try:       
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print("request:")
        print(request)
        request = str(request)
        
        
        led_on = request.find('led=on')
        led_off = request.find('led=off')
        
        print( 'led on = ' + str(led_on))
        print( 'led off = ' + str(led_off))
        
        if led_on == 8:
            print("led on")
            led.value(1)
        elif led_off == 8:
            print("led off")
            led.value(0)
        
        ledState = "LED is OFF" if led.value() == 0 else "LED is ON" # a compact if-else statement
        
        if button.value() == 1: # button not pressed
            print("button NOT pressed")
            buttonState = "Button is NOT pressed"
        else:
            print("button pressed")
            buttonState = "Button is pressed"
        
        # Create and send response
        stateis = ledState + " and " + buttonState
        response = html % stateis
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
  
    except OSError as e:
        cl.close()
        pass
        print('connection closed')
        
    except KeyboardInterrupt:
        cl.close()
        exit


