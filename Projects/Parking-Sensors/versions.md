# All version


- 


- Ultrasonic - HC-SR04 -  https://www.ebay.com/itm/185599956834
- JST - 2.54mm JST-XHP 2/3/4/5  - https://www.ebay.com/itm/134230883852
- Display - I2C Display Module 0.91 Inch I2C SSD1306 OLED Display Module Blue I2C OLED Screen Driver DC 3.3V-5V https://www.aliexpress.us/item/3256804805767363.html?spm=a2g0o.detail.1000014.28.32446829E2LVrY&gps-id=pcDetailBottomMoreOtherSeller&scm=1007.40050.281175.0&scm_id=1007.40050.281175.0&scm-url=1007.40050.281175.0&pvid=77f5a580-8964-4b29-ace5-8aef16c866d8&_t=gps-id:pcDetailBottomMoreOtherSeller,scm-url:1007.40050.281175.0,pvid:77f5a580-8964-4b29-ace5-8aef16c866d8,tpp_buckets:668%232846%238110%231995&pdp_npi=3%40dis%21USD%2117.18%217.04%21%21%21%21%21%40210324f116815938974544559ed09c%2112000031266277758%21rec%21US%213039325357
- RGB Led -
- Terminal Block - 5.08mm KF2EDGK KF-2P - https://www.ebay.com/itm/114874147582?var=415017540212

- 18650 Lithium Battery Protection Board Type-c - 


## Version 1/1.5
- Already Made
- Hard wired from all compontents
- 1.5 have JST


## Version 2 - PCB 1.0 
- PCB
- Ultrasonic physical female headers on PCB - 4 PINS
- Display - physical female headers on PCB - 4 Pins
- RGB Led - physical female headers on PCB - 4 Pins
- PICO W - 2 Pins for Ultrasonic, 2 Pins Display, 3 Pins RGB = 7 pins 
- Power via PICO USB Micro connector

Refs:
- https://www.youtube.com/watch?v=5nLONfdh7vw


## Version 3 - PCB 2.0
 Synopsis: A PCB with DIP for PIC10F200 - 2 GPIO's for Ultrasonic Trigger, Echo, 2 more for Red/Green LED, 1 Button to set distance. 
 Red when to STOP, green if coming close(Close enough), flashing red if too close. 

 - Careful when programming, remove Vpp line to USS 
- PCB
- Ultrasonic physical female headers on PCB
    - 3.3v to 5v Operations? Check this
- 1 Button 
- Display - physical female headers on PCB
- RGB Led - physical female headers on PCB
- PIC10F200 - 6pin SOT-23 or 8 DIP
    1 NC    8 GP3/MCLR/VPP
    2 Cdd   7 Vss
    3 GP2   6 NC
    4 GP1   5 GPO/ICSPDAT

    - Operating Current - 175 uA @ 2v 4MHz
    - Standby Current 100 nA @2v
    - OPerating Voltage 2.0 to 5.5 V
     
- Power from JST battery (2AA)
- Battery charging circuit on board (Built into PCB or mountable? with those pre made modules)

ToDo:
1. Check voltage of Ultrasonic sensor to determine battery imput 
2. Test 
3. Check out differnt pics: pic12f629p, pic12f675, pic10f200
4. Save car distance on button press: https://electronics.stackexchange.com/questions/250652/how-to-save-variables-inside-microcontrollers-memory

5. How to set distance:
     1. button on boot/anytime(interupt)
    2. Distance of car (ex: 50cm) then hand in front of sensors goes to (distance < 5cm for 5 seconds will set distance)

6. Test outside. 
    1. RPI Pico Wifi connected to debug and send stats via MQTT? 

7.Paperwork with product:
        - Certifications needed?
        - Instructions 
            - Turn on device
            - Place car in perfect location
            - Stand to the side and hold the button for 3 seconds (Until Green Lights flash)
            - Test sensor by moving the car in/out 
            - Can be changed anytime 'git
        - Warning
            - device is not perfect
            - 10cm to 1400cm range ( get real numbers)
            - 


https://www.ebay.com/itm/324139980479?epid=1804659339&hash=item4b783f96bf:g:-kQAAOSwW35em5Xh



Pads
https://forums.autodesk.com/t5/fusion-360-electronics/adding-a-solder-pad-in-a-schematic/td-p/9840202