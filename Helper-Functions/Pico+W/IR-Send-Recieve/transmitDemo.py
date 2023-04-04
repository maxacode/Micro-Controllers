# Control LED's from controlLED.py

#  17 for IR output and pins 18 and 19 for pushbuttons

from machine import Pin
from ir_tx.nec import NEC
nec = NEC(Pin(17, Pin.OUT, value = 0))
#print("Sending 0, 58")

from time import sleep
valueToTurnOff = 99

allSends = {'redIR': 88, 'greenIR': 89, 'blueIR': 69}

while True:
    # all off
    for index, (key,data) in enumerate(allSends.items()):
        print(f"Sending key: {key} - xdata:{data} + {valueToTurnOff} ")
        nec.transmit(00, data +valueToTurnOff)  # address == 1, data == 2
        sleep(1)
 
        
    for index, (key,data) in enumerate(allSends.items()):
        print(f"Sending key: {key} - xdata:{data} ")
        nec.transmit(00, data)  # address == 1, data == 2
        sleep(1)
        print(f"Sending key: {key} - xdata:{data} ")
        nec.transmit(00, data)  # address == 1, data == 2
        sleep(1)
        print()
