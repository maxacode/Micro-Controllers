# Connecting to WLAN
#http://192.168.88.154:8266/
from connectToWlan import connectWLAN

ipInfo= connectWLAN()
print(ipInfo)
 
import webrepl
webrepl.start()

