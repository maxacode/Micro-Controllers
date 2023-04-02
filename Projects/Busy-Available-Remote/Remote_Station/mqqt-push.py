#MQTT test

from network import WLAN 
#from mqtt import MQTTClient 
import machine 
import time
from umqtt.simple import MQTTClient
import connectToWlan

#import connectMQTT

ipInfo = connectToWlan.connectWLAN()
print(ipInfo)


topic = "picow/test"
mqtt_server = b"ce19a0c7e64343b1a22371538db5c506.s2.eu.hivemq.cloud"
def sub_cb(topic, msg): 
   print(msg)
   
#client = MQTTClient("device_id", "poico-sub",user="mqtthivemquser", password="akx-png4wdg6mfu7FED", port=8883) 
print("Attemtpign conn to MQTT")
#client = MQTTClient(b"pcio-sub", mqtt_server, port=1883,user=b"mqtthivemquser", password=b"akx-png4wdg6mfu7FED", ssl=True, ssl_params={'server_hostname':'ce19a0c7e64343b1a22371538db5c506.s2.eu.hivemq.cloud'})
client = MQTTClient(client_id=b"picow_test",
                        server=b"ce19a0c7e64343b1a22371538db5c506.s2.eu.hivemq.cloud",
                        port=8883,
                        user=b"mqtthivemquser2",
                        password=b"akx-png4wdg6mfu7FED",
                        keepalive=7200,
                        ssl=True,
                        ssl_params={'server_hostname':'ce19a0c7e64343b1a22371538db5c506.s2.eu.hivemq.cloud'}
                        )
client.connect()
    
client.set_callback(sub_cb) 
#client.connect()
client.subscribe(topic)
print("Connected and Subscripbed")
 

import utime
while True:
    #openSocketStart()
    #remoteDistanceGetter()
    #callReturn = makeAPICall(getDistanceAPI)
    #    publish("picow/test_ultrasonic_Busy_Avail", str(callReturn))
    #for callReturn in range (0, 10000000):
     #   publish("picow/test", str(callReturn))
    #utime.sleep_us(1)
    try:
        msg = client.check_msg()
        print(msg)
        utime.sleep(1)
    except OSError as e:
        #restart_and_connect()
        utime.sleep(1)
        print("Sleepig")
    #utime.sleep(0.5)

