# Test LED
# https://docs.micropython.org/en/latest/library/uasyncio.html
# https://www.youtube.com/watch?v=pOB3mH8G2q4&t=247s
from machine import Pin
import uasyncio


led = Pin(16, Pin.OUT)
led.toggle()


async def onBoardLed(duration=.5):
    led.toggle()
    await uasyncio.sleep(duration)
    led.toggle()
    

async def onBoardLedFlash(amount= 5, duration=.1):
    while amount >= 0:
        amount -=1
        led.toggle()
        await uasyncio.sleep(duration)
        led.toggle()
    




