import time
from machine import Pin

led = Pin(25, Pin.OUT) # ONboard LED

led.value(1)

led.toggle() # on if off or off if on.

n = 0

while True:
    print(f"13 times {n} is {13*n}")
    time.sleep(0.5)
    led.toggle()
    
    


