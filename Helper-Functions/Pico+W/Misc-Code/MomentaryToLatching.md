# Momentary button into Latching with Code
[Inspiration](https://www.youtube.com/watch?v=U6N5pRDOrg4)

## Code

```python
import RPi.GPIO as io
import time

io.setmode(io.BOARD)

brownio = 12
whiteio = 16

io.setup(brownio, io.OUT, initial=io.LOW)
io.setup(whiteio, io.IN, pull_up_down=io.PUD_UP)

for x in range(3):
    print("On")
    io.output(brownio, io.HIGH)
    time.sleep(.5)
    print("Off")
```

## Output

```bash
pi@octopi:~ $ python buttonLED.py 
buttonLED.py:25: SyntaxWarning: name 'led_on' is used prior to global declaration
  global led_on
buttonLED.py:9: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  io.setup(brownio, io.OUT, initial=io.LOW)
On
Off
On
Off
On
Off
Turning On!
Turning Off
Turning On!
Turning Off
Turning On!
```