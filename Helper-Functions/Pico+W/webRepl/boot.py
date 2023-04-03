# Connecting to WLAN
#http://192.168.88.154:8266/
# test file
# test from thonny web repl

from connectToWlan import connectWLAN

ipInfo= connectWLAN()
print(ipInfo)
 
import webrepl
webrepl.start()

