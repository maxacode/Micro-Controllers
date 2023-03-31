from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()

button_sounds = {
    Button(2): Sound("/home/pi/Desktop/burp.wav"),
    Button(3): Sound("/usr/share/gui-pkinst/instfail.wav"),
}

for button, sound in button_sounds.items():
    print(f"playing {sound} for {button}")
    button.when_pressed = sound.play

pause()
