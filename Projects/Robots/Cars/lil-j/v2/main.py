# Main code for Lil-j v2 robot:
"""
# V2 - Not Tested 
- Same a v1
- Wifi controll
- pre determied loops (Square, (Small/Big) circle, etc. ) https://www.coderdojotc.org/micropython/kits/maker-pi-rp2040-robot/07b-drive-square-lab/

"""
from index import html
from liljclass import lilJ
import network, socket
from time import sleep

# Connecting to WLAN
from connectToWlan import connectWLAN

ipInfo= connectWLAN()
print(ipInfo)
 


robot = lilJ()


def move_forward():
    print ("Forward")
    robot.forward()

def move_reverse():
    print ("Backward")
    robot.reverse()

def move_stop():
    print ("Stop")
    robot.setAllMotorsLow()
def move_left():
    print ("Left")
    robot.turnLeft()
def move_right():
    print ("Right")
    robot.turnRight()

#Take request and perform according action

# Open socket
while True:
    try:
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
        print(f"except 58: {e}")
        sleep(.1)
    



def serve():
        #Start web server
    while True:
        client, addr = s.accept()
        
        request = client.recv(1024)
        print(request)

        #request = str(request)
        try:
            request = request.split()[1]
            print(request)
        except IndexError:
            pass
        if '/forward?' in request:
            print("serve forward")
            move_forward()
        elif '/left?' in request:
            move_left()
        elif '/stop?' in request:
            move_stop()
        elif '/right?' in request:
            move_right()
        elif '/back?' in request:
            move_reverse()
        else:
            print("NO correct action")
            
        client.send(html)
        client.close()

try:
     
     
    serve()
except KeyboardInterrupt:
    machine.reset()
