# 3 LED's with 1 button
[Inspiration](https://www.youtube.com/watch?v=U6N5pRDOrg4)

## Code

```python
import RPi.GPIO as io
import time

io.setmode(io.BOARD)

brownio = 12
whiteio = 16
redio = 18
orangeio = 11

io.setup(brownio, io.OUT, initial=io.LOW)
io.setup(redio, io.OUT, initial=io.LOW)
io.setup(orangeio, io.OUT, initial=io.LOW)

io.setup(whiteio, io.IN, pull_up_down=io.PUD_UP)

for x in range(3):
	for x in (brownio, redio, orangeio):
    		print(x, ": is on")
    		io.output(x, io.HIGH)
    		time.sleep(.5)
    		io.output(x, io.LOW)
    		time.sleep(.5)


#Function to switch condition of LED. If on turn off, if off turn on
led_on1 = False
led_on2 = False
led_on3 = False

# x is the counter for the Button. Every button pushed will increment x. Looping through all the Scenarios below. 
# !!! NEED to find more efficeint way to do this !!!

x = 0
def threeButtons(ev=None):
    global x
    if x == 0:
        print("Green On!")
        io.output(brownio, io.HIGH)
        io.output(orangeio, io.LOW)
        x = 1
    elif x == 1:
        print("White On!")
        io.output(brownio, io.LOW)
        io.output(redio, io.HIGH)
        x = 2
    elif x == 2:
        print("Yellow On!")
        io.output(redio, io.LOW)
        io.output(orangeio, io.HIGH)
        x = 3
    elif x == 3:
	print("All On!")
	io.output(redio, io.HIGH)
	io.output(brownio, io.HIGH)
	x = 4
    elif x == 4:
	print("All Off!")
	for x in (orangeio, redio, brownio):
		time.sleep(.3)
		print(x, ": is off")
		io.output(x, io.LOW)
	x = 0
    else:
        print("Error")
        x = 0
# Listing to event if sharp drop or rise in value

io.add_event_detect(whiteio, io.FALLING, callback=threeButtons, bouncetime=800)

while True:
    time.sleep(1)
```

## Output

```bash
 
pi@octopi:~ $ python 3led.py 
3led.py:11: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  io.setup(brownio, io.OUT, initial=io.LOW)
3led.py:12: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  io.setup(redio, io.OUT, initial=io.LOW)
3led.py:13: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  io.setup(orangeio, io.OUT, initial=io.LOW)
(12, ': is on')
(18, ': is on')
(11, ': is on')
(12, ': is on')
(18, ': is on')
(11, ': is on')
(12, ': is on')
(18, ': is on')
(11, ': is on')
Green On!
White On!
Yellow On!
All On!
All Off!
(11, ': is off')
(18, ': is off')
(12, ': is off')
```