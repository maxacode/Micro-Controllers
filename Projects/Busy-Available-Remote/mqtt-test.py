#MQTT testf

import network
import utime
import connectToWlan
import urequests as requests
#from umqtt.simple import MQTTClient

#import connectMQTT

ipInfo = connectToWlan.connectWLAN()
print(ipInfo)


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
    client.publish(topic,value)
    print("Publish Done")
    
    
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

    multiDistances.append(distanceValue)
    print(multiDistances)
    
    if len(multiDistances) >= 10:
        print("10 in multidisnaces")
    if distanceValue >= 800.00:
        distanceValue = 0
        
        
    
    
    print(utime.gmtime(), distanceValue)
   # print(162)
    return distanceValue

remoteIP = "http://192.168.88.143"

setBusyAPI = "Busy=Busy"
setAvailableAPI = "Available=Available"
getStatusAPI = "getAvailableStatus"
getDistanceAPI = "getDistance=True"
getDistanceAPIParkignAsistan = "getDistance"


while True:
    #openSocketStart()
    #remoteDistanceGetter()
    callReturn = makeAPICall(getDistanceAPI)
    #    publish("picow/test_ultrasonic_Busy_Avail", str(callReturn))
    publish("picow/test", str(callReturn))
    utime.sleep_us(1)



