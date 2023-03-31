#MQTT test

import network
import time
#from wlan_codes import *

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
for ssid in wlan.scan():
    print(ssid)
