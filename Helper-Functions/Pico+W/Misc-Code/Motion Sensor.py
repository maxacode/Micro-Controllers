


from platform import python_branch


"""python
from gpiozero import MotionSensor, LED
import pygame.mixer
from pygame.mixer import Sound
from signal import pause
from time import sleep

pygame.mixer.init()

pir = MotionSensor(4)
led = LED(3)

print(led)
led.on()
print(led)
print('slee')
sleep(1)
led.off()
print('sleep done')
def detection():
    led.on()
    print("Detected Motion")
    Sound("/home/pi/Desktop/burp.wav").play
def noDetection():
    led.off()
    print("No Motion")
    Sound("/usr/share/gui-pkinst/instfail.wav").play
    
try:
    pir.when_motion = detection
    pir.when_no_motion = noDetection
    
    pause()
    
except KeyboardInterrupt:
    print("keyboar")
    led.off()
    exit()

"""



# 2

from gpiozero import MotionSensor, LED
from signal import pause
import pygame.mixer
from pygame.mixer import Sound
pygame.mixer.init()

print("startup")

pir = MotionSensor(4)
led = LED(3)
print("led on")
led.on()

def detected():
    Sound("/home/pi/Desktop/burp.wav").play
    print("Detected")
    led.off()
    
try:
    pir.when_motion = detected
    
    pir.when_no_motion = led.on
    
    pause()
    
except KeyboardInterupt:
    print("key")
    led.off
    pass