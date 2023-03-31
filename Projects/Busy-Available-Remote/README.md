# Busy-or-Available-Remote-Lights


[Updates]

- Local/Base station communicate with Busy/Available Lights
- The Ultrasonic Sensor is not accurate thus glitchy
- May try a better sensor or just do the 2mm wave person detection sensor


Signal if busy or available to speak to a light outside the door from 2 buttons inside the office

Research:

- Wireless Antenna/radio frequency transciever that i have

2 Components

1st - Local Controller:

- Pico W
- Red Button - Busy
- Green Button - Available
- RGB-LED - Connected to Remote Station Status
- - Red - Busy Signal
- - Green - Available (If Battery powered then no lights/deep sleep mode to conserve power)
- - Blue - Motion Detected
- a way to disable motion notifications
- - simple switch on/off
- - latching button
- - secret combo: press red twice then green once yo enable
    motion and red 2 and hreen 2 to disbale motion notifications
- Websit
  - Busy Button
  - Available Button
  - Motion Detected

2nd - Remote Station

- Pico W
- RGB-LED
- - Red - Busy Signal
- - Green - Available (If Battery powered then no lights/deep sleep mode to conserve power)
- Proximity Sensor
- - Passive Infared (PIR) https://www.sparkfun.com/products/13285
- Website
  - Busy Button
  - Available Button

Links:
https://electronics.stackexchange.com/questions/513096/reducing-ir-proximity-sensor-module-power-consumption
https://www.seeedstudio.com/blog/2019/12/19/all-about-proximity-sensors-which-type-to-use/
