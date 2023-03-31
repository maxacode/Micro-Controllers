
### Blinking LED 

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
    io.output(brownio, io.LOW)
    time.sleep(.5)


#Function to switch condition of LED. If on turn off, if off turn on
led_on = Falsed
def latchingButton(ev=None):
    print("Turning Off" if led_on else "Turning On!")
    global led_on
    led_on = not led_on
    io.output(brownio, io.HIGH if led_on else io.LOW)


# Listing to event if sharp drop or rise in value

io.add_event_detect(whiteio, io.FALLING, callback=latchingButton, bouncetime=300)

while True:
    time.sleep(1)

```

In C programming language:

https://github.com/mheidenreich/wiringPiBasics

```c
/*
    Program: wiringPi Basics (blink.c)

    Author:  M. Heidenreich, (c) 2021-2022

    Description: This code is provided in support of the following YouTube tutorial:
                 https://youtu.be/RDAOxX6vqqs
		 
    How to compile: 			gcc -Wall blink.c -lwiringPi -o blink
    How to run compiled program: 	./blink

    This tutorial is an introduction to how to use wiringPi library
	with Raspberry Pi to control LEDs.

    THIS SOFTWARE AND LINKED VIDEO TOTORIAL ARE PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS
    ALL WARRANTIES INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.
    IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES
    OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
    NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
*/

#include <wiringPi.h>
#include <signal.h>

#define GREEN 19
#define RED 26

int blink = 1;

void cleanup(int signo) {
    blink = 0;
}

int main(void) {
    signal(SIGINT, cleanup);
    signal(SIGTERM, cleanup);
    signal(SIGHUP, cleanup);

    wiringPiSetupGpio();
    pinMode(GREEN, OUTPUT);
    pinMode(RED, OUTPUT);

    while (blink) {
        digitalWrite(GREEN, HIGH);
        delay(500);
        digitalWrite(GREEN, LOW);
        digitalWrite(RED, HIGH);
        delay(500);
        digitalWrite(RED, LOW);
    }

    digitalWrite(GREEN, LOW);
    digitalWrite(RED, LOW);

    pinMode(GREEN, INPUT);
    pinMode(RED, INPUT);

    return 0;
}
```


### Blinking LED 

https://gpiozero.readthedocs.io/en/stable/installing.html

sudo apt install python3-gpiozero


```python

#!/usr/bin/python3

from signal import pause
from gpiozero import LED, Button

button = Button(2)
led = LED(3)

try:
    led.source = button.values
    pause()

finally:
    pass

# Or 

red = LED(17)

red.blink()

pause()

```


## Pyton Interactive Shell

```python
Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import gpiozero
>>> led = LED(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'LED' is not defined
>>> led = gpiozero.LED(2)
>>> led
<gpiozero.LED object on pin GPIO2, active_high=True, is_active=False>
>>> led.on 
<bound method DigitalOutputDevice.on of <gpiozero.LED object on pin GPIO2, active_high=True, is_active=False>>
>>> led
<gpiozero.LED object on pin GPIO2, active_high=True, is_active=False>
>>> led.off
<bound method DigitalOutputDevice.off of <gpiozero.LED object on pin GPIO2, active_high=True, is_active=False>>
>>> led.on()
>>> led
<gpiozero.LED object on pin GPIO2, active_high=True, is_active=True>
>>> 
```

Notes:
- `led.on()` and `led.off()` are bound methods.
- 'led' is a variable that points to the object.
- led.on `has to be a function ()`
- Can use Mappings of GPIO pins to physical pins on the board.
- - \>>> led = LED(17)
- - \>>> led = LED("GPIO17")
- - \>>> led = LED("BCM17")
- - \>>> led = LED("BOARD11")
- - \>>> led = LED("WPI0")
- - \>>> led = LED("J8:11")


### PWM Pulse width modulation - Variable Brightness

![](/assets/led_bb.svg)

```python

pi@octopi:~ $ cat pwmLedZero.py 
#!/usr/bin/python3


import gpiozero as io
from time import sleep

led = io.PWMLED(2)


'''
while True:
	led.value = 0
	sleep(.5)
	led.value = .5 # half brightness
	sleep(1)
	led.value = 1 # full
	sleep(1)
'''
count = 0 
xs = (x * 0.1 for x in range(0, 14))
xs = list(xs)

x = 0
while x > 0:
	print(x)
	led.value = x
	x += .1
	sleep(.3)
	
		
		
while True:
	for x in xs:
		print(count)
		count += 1
		led.value = x
		sleep(.1)
	
	for x in xs.reverse():
		print(count)
		count -= 1
		led.value = x
		sleep(.1)
	continue

# OR

from gpiozero import PWMLED
from signal import pause

led = PWMLED(2)

led.pulse()

pause()

```

Output
``` bash
pi@octopi:~ $ python3 pwmLedZero.py 
0
1
2
3
4
5
6
7
....
100
```
 

### Button

![](/assets/button_bb.svg)

Check if a Button is pressed:

```python
from gpiozero import Button

button = Button(2)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")

```

Wait for a button to be pressed before continuing:

```python
from gpiozero import Button

button = Button(2)

button.wait_for_press()
print("Button was pressed")
```

Run a function every time the button is pressed:

```python
from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello!")

button = Button(2)

button.when_pressed = say_hello

pause()

```
>> ### Note: that the line button.when_pressed = say_hello does not run the function say_hello, rather it creates a reference to the function to be called when the button is pressed. Accidental use of button.when_pressed = say_hello() would set the when_pressed action to None (the return value of this function) which would mean nothing happens when the button is pressed.

Similarly, functions can be attached to button releases:

```python
from gpiozero import Button
from signal import pause
button = Button(3)

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")


button.when_pressed = say_hello
button.when_released = say_goodbye

pause()
```

### Turn on an LED when a Button is pressed:

![](/assets/led_button_bb.svg)

```python

from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()
# Alternatively:

from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

led.source = button

pause()`


```

### Latching button 

```python
button.when_pressed = led.toggle

pause()

```


### Button and Camera

Resources:
- https://raspberrypi-guide.github.io/programming/install-opencv.html
- https://raspberrypi-guide.github.io/electronics/using-usb-webcams
- https://systemrequest.net/index.php/258/
- 
```python
from gpiozero import Button
from datetime import datetime
from signal import pause
import os

button = Button(2)

print("Starting Image Capture via Button Program")

def capture():
    print("starting capture")
    timestamp = datetime.now().isoformat()
    command = f"ffmpeg -f v4l2 -video_size 1280x720 -i /dev/video1 -frames 1 IMAGE-{timestamp[10:19].replace(':','-')}.jpg"

    os.system(command)
    print("Image captured")

button.when_pressed = capture

pause()

```
![](/assets/IMAGE-T20-34-44.jpg)


### Button to start script.py

```python
pi@octopi:~ $ python3
Python 3.7.3 (default, Jan 22 2021, 20:04:44) 

>>> import gpiozero as io

>>> butt = io.Button(3)

>>> def runCameraScript():
...     import os
...     os.system("python3 pic.py")
...     print("Starting Program")
... 

>>> butt.when_pressed = runCameraScript

>>> Starting Image Capture via Button Program
starting capture
ffmpeg version 4.1.9-0+deb10u1+rpt1 Copyright (c) 2000-2022 the FFmpeg developers


````

![](/assets/IMAGE-T20-40-26.jpg)


###  Shutdown button
The Button class also provides the ability to run a function when the button has been held for a given length of time. This example will shut down the Raspberry Pi when the button is held for 2 seconds:

```python
from gpiozero import Button
from subprocess import check_call
from signal import pause

def shutdown():
    check_call(['sudo', 'poweroff'])

shutdown_btn = Button(17, hold_time=2)
shutdown_btn.when_held = shutdown

pause()

```

### LEDBoard - Collection of LED's 
![](/assets/ledboard_bb.svg)

A collection of LEDs can be accessed using LEDBoard:

```python
from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(2, 3, 4, 14)

leds.on()
sleep(1)
leds.off()
sleep(1)
leds.value = (1, 0, 1, 1)
sleep(1)
leds.blink()

pause()

# Using LEDBoard with pwm=True allows each LED’s brightness to be controlled:

from gpiozero import LEDBoard
from signal import pause

leds = LEDBoard(2, 3, 4, 14, pwm=True)

leds.value = (0.2, 0.4, 0.6, 1.0)

pause()

```
[See more LEDBoard examples in the advanced LEDBoard recipes.](https://gpiozero.readthedocs.io/en/stable/recipes_advanced.html#ledboard-advanced)


### LEDBarGraph 
![](/assets/ledbargraph_bb.svg)

A collection of LEDs can be treated like a bar graph using [LEDBarGraph:](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph)

```python
from gpiozero import LEDBarGraph
from time import sleep
from __future__ import division  # required for python 2

graph = LEDBarGraph(2, 3, 4, 14, pwm=True)

graph.value = 1  # (1, 1, 1, 1, 1, 1)
sleep(1)
graph.value = 1/2  # (1, 1, 1, 0, 0, 0)
sleep(1)
graph.value = -1/2  # (0, 0, 0, 1, 1, 1)
sleep(1)
graph.value = 1/3  # (1, 0, 0, 0, 0, 0)
sleep(1)
graph.value = 2/3  # (1, 0, 0, 0, 0, 0)
graph.value = 2/4  # (1, 0, 0, 0, 0, 0)

graph.value = -1  # (1, 1, 1, 1, 1, 1)
sleep(1)
```

Note values are essentially rounded to account for the fact LEDs can only be on or off when pwm=False (the default).

However, using LEDBarGraph with pwm=True allows more precise values using LED brightness:

```python
from gpiozero import LEDBarGraph
from time import sleep
from __future__ import division  # required for python 2

graph = LEDBarGraph(5, 6, 13, 19, 26, pwm=True)

graph.value = 1/10  # (0.5, 0, 0, 0, 0)
sleep(1)
graph.value = 3/10  # (1, 0.5, 0, 0, 0)
sleep(1)
graph.value = -3/10  # (0, 0, 0, 0.5, 1)
sleep(1)
graph.value = 9/10  # (1, 1, 1, 1, 0.5)
sleep(1)
graph.value = 95/100  # (1, 1, 1, 1, 0.75)
sleep(1)

```

### LEDCharDisplay

![](/assets/led_char_display_bb.svg)

A common [7-segment](https://en.wikipedia.org/wiki/Seven-segment_display) display can be used to represent a variety of characters using LEDCharDisplay (which actually supports an arbitrary number of segments):

```python
from gpiozero import LEDCharDisplay
from time import sleep

display = LEDCharDisplay(21, 20, 16, 22, 23, 24, 12, dp=25)

for char in '321GO':
    display.value = char
    sleep(1)

display.off()
Alternatively:

from gpiozero import LEDCharDisplay
from signal import pause

display = LEDCharDisplay(21, 20, 16, 22, 23, 24, 12, dp=25)
display.source_delay = 1
display.source = '321GO '

pause()
```

### 1602A LCD Display Old Way
- https://www.openhacks.com/uploadsproductos/eone-1602a1.pdf
- https://www.youtube.com/watch?v=x066WTiz9Fw

![](/assets/1602A.png)

![](/assets/1602A-PinMapping.png)

# or Alternative IC2

VSS = Grnd
VDD = 5v pin 1
V0 = Ground 
RS = 2
rw  = GRND
E = 3

D4 = 4
D5 = 14
D6 = 15 
D7 = 18
A = Positive
K = Negative 


Modules: 
- lcd_string(string, line)
- lcd_bytes(line, command)

```python
import os
import lcd #lcd.py file. 
>>> lcd.lcd_init()
>>> lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)

>>> lcd.lcd_string("I Love You", 2)

>>> lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
>>> lcd.lcd_string("Soooooo Much!!", 2)

>>> lcd.GPIO.cleanup()
```

Test
    
```python
import sys
sys.path.append('/home/pi/lcd')
import lcd
lcd.lcd_init()
lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
lcd.lcd_string("Raspberry Pi", 2)
lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
lcd.lcd_string("Model B+", 2)
lcd.GPIO.cleanup()

```

### RPiSpy (Works the best so far)

[RPiSpy Code](/assets/LCD-Display_lcd_py/Display-Clock-CPU-IP.py)
 

```python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#  lcd_16x2.py
#  16x2 LCD Test Script
#
# Author : Matt Hawkins, Leon Anavi
# Date   : 06/04/2015
#
# http://www.raspberrypi-spy.co.uk/
# http://anavi.org/

```

### Circuit Python 

https://docs.circuitpython.org/projects/charlcd/en/latest/
https://docs.circuitpython.org/projects/bundle/en/latest/drivers.html

```python
# LCD_RS = 2
# LCD_E  = 3
# LCD_D4 = 4
# LCD_D5 = 14
# LCD_D6 = 15
# LCD_D7 = 18

import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

lcd_rs = digitalio.DigitalInOut(board.D3)
lcd_en = digitalio.DigitalInOut(board.D5)
lcd_d4 = digitalio.DigitalInOut(board.D7)
lcd_d5 = digitalio.DigitalInOut(board.D8)
lcd_d6 = digitalio.DigitalInOut(board.D10)
lcd_d7 = digitalio.DigitalInOut(board.D12)
lcd_backlight = digitalio.DigitalInOut(board.D11)

lcd_columns = 16
lcd_rows = 2

lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

lcd.message = "Hello\nCircuitPython"


```


### Traffic Lights LCD
![](/assets/traffic_lights_bb.svg)

A full traffic lights system.

Using a TrafficLights kit like Pi-Stop:

```python

from gpiozero import TrafficLights
from time import sleep

lights = TrafficLights(2, 3, 4)

lights.green.on()

while True:
    sleep(10)
    lights.green.off()
    lights.amber.on()
    sleep(1)
    lights.amber.off()
    lights.red.on()
    sleep(10)
    lights.amber.on()
    sleep(1)
    lights.green.on()
    lights.amber.off()
    lights.red.off()

# Alternatively:

from gpiozero import TrafficLights
from time import sleep
from signal import pause

lights = TrafficLights(2, 3, 4)

def traffic_light_sequence():
    while True:
        yield (0, 0, 1) # green
        sleep(10)
        yield (0, 1, 0) # amber
        sleep(1)
        yield (1, 0, 0) # red
        sleep(10)
        yield (1, 1, 0) # red+amber
        sleep(1)

lights.source = traffic_light_sequence()

pause()
```

Using LED components:

```python

from gpiozero import LED
from time import sleep

red = LED(2)
amber = LED(3)
green = LED(4)

green.on()
amber.off()
red.off()

while True:
    sleep(10)
    green.off()
    amber.on()
    sleep(1)
    amber.off()
    red.on()
    sleep(10)
    amber.on()
    sleep(1)
    green.on()
    amber.off()
    red.off()
```



### Reaction Game

![](/assets/reaction_game_bb.svg)

![](/assets/quick-reaction-circuit.png)

https://pypi.org/project/art/
g

When you see the light come on, the first person to press their button wins!

```python
from gpiozero import Button, LED
from time import sleep
import random
from datetime import datetime
from art import *

tprint("Start your Fingersssss ")

led = LED(14)
led.on()
sleep(1)
led.off()
green = Button(2)
red = Button(3)

reds = 0
greens = 0

while True:
   # print("Starting Game")
   # print(f"Green: {greens} \n Red: {reds}")
    time = random.uniform(5, 10)
    sleep(time)
    print(str(datetime.now())[14:])
    led.on()

    while True:
        if green.is_pressed:
            greens += 1

            #print("Player Green wins!")
            tprint(f"Green: {greens}")

            print(str(datetime.now())[14:])
            break
        
        if red.is_pressed:
            reds += 1
            #print("Player Red wins!")
            tprint(f"Red: {reds}")
            
            print(str(datetime.now())[14:])
            break
        

    led.off()

```
https://projects.raspberrypi.org/en/projects/python-quick-reaction-game

See Quick Reaction Game for a full resource.


### Distance Sensor

```python
from gpiozero import DistanceSensor
from time import sleep
# Echo = 4

# Trig = 3 

sensor = DistanceSensor(4, 3)

while True:
    print('Distance to nearest object is', str(sensor.distance)[:4], 'm')
    sleep(1)

```