# https://www.youtube.com/watch?v=BkmIUqccwDw

# Reciver
from machine import Pin, UART
from time import sleep
rx = UART( )
 


#Transmitter
from machine import Pin
from time import sleep

transmit = Pin(17, Pin.IN)

while True:
    transmit.value(1)
    sleep(1)
    transmit.value(0)
    sleep(.5)Helper-Functions/Pico+W/webRepl/manifest.py