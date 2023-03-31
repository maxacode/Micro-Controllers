# Momentary button into Latching with Code
[Inspiration](https://www.youtube.com/watch?v=U6N5pRDOrg4)

## Code

```python
 
import RPi.GPIO as io
import time

io.setmode(io.BOARD)

brownio = 12
whiteio = 16
redio = 18

io.setup(brownio, io.OUT, initial=io.LOW)
io.setup(redio, io.OUT, initial=io.HIGH)

io.setup(whiteio, io.IN, pull_up_down=io.PUD_UP)

for x in range(3):
    print("On")
    io.output(redio, io.LOW)
    io.output(brownio, io.HIGH)
    time.sleep(.5)
    print("Off")
    io.output(redio,io.HIGH)
    io.output(brownio, io.LOW)
    time.sleep(.5)


#Function to switch condition of LED. If on turn off, if off turn on
led_on1 = False
led_on2 = True
def latchingButton(ev=None):
    print("White On" if led_on1 else "Green On!")
    global led_on1, led_on2

    led_on1 = not led_on1
    led_on2 = not led_on2
    
    io.output(brownio, io.HIGH if led_on1 else io.LOW)
    io.output(redio, io.HIGH if led_on2 else io.LOW)

# Listing to event if sharp drop or rise in value

io.add_event_detect(whiteio, io.FALLING, callback=latchingButton, bouncetime=300)

while True:
    time.sleep(1)


```

## Output

```bash
On
Off
On
Off
On
Off
White On!
Gren On
White On!
Gren On
White On!
  
```