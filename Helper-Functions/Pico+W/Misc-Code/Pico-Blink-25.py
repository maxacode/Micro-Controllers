

from machine import Pin

led = Pin(25, PIN.OUT) # ONboard LED

led.value(1)

led.toggle() # on if off or off if on.

while True:
    time.sleep(0.5)
    led.toggle()
    
    