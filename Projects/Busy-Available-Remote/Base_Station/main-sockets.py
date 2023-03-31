#MQTT test

import network
import utime
import connectToWlan
import urequests as requests
#from umqtt.simple import MQTTClient

#import connectMQTT


remoteIP = "192.168.88.143"
port = 1234

setBusyAPI = "Busy=Busy"
setAvailableAPI = "Available=Available"
getStatusAPI = "getAvailableStatus"
getDistanceAPI = "getDistance=True"
getDistanceAPIParkignAsistan = "getDistance"
import _thread


topic = "picow/test"
import socket

def startSocket():
    ipInfo = connectToWlan.connectWLAN()
    print(ipInfo)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((remoteIP,port))
    print("connected to: ", remoteIP)
    while True:
        
        msg = client.recv(1024).decode("utf8")
        #print(msg)
        #if int(msg) > 40:
        print(msg)
       # print()

#ultra_thread = _thread.start_new_thread(startSocket, ())

while True:
    startSocket()
#take()
    
from umqtt.simple import MQTTClient


def connectMQTT():
    client = MQTTClient(client_id=b"picow_test",
                        server=b"ce19a0c7e64343b1a22371538db5c506.s2.eu.hivemq.cloud",
                        port=8883,
                        user=b"mqtthivemquser",
                        password=b"akx-png4wdg6mfu7FED",
                        keepalive=7200,
                        ssl=True,
                        ssl_params={'server_hostname':'ce19a0c7e64343b1a22371538db5c506.s2.eu.hivemq.cloud'}
                        )
    client.connect()
    #client.publish("picow_test","test-from-connectMQTT.py")
    #print("Publish Done")
    
    return client

client = connectMQTT()


def publish(topic, value):
    print(topic, " | ", value)
    client.publish(topic,topic + " | " +value)
    print("Publish Done")
    
    
    
#publish(topic, ipInfo)

multiDistances = []

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
            
    distanceValue = float(request.text)

    #multiDistances.append(distanceValue)
   # print(multiDistances)
    
 
        
    if distanceValue >= 800.00:
        distanceValue = 0
    else:        
        
        print(utime.gmtime(), distanceValue)
       # print(162)
        publish(topic, str(distanceValue))
        utime.sleep_us(1)
        #return distanceValue



#while True:
    #openSocketStart()
    #remoteDistanceGetter()
    #callReturn = makeAPICall(getDistanceAPI)
    #    publish("picow/test_ultrasonic_Busy_Avail", str(callReturn))

    startSocket()
    take()
