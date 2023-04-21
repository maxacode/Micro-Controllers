
def testLeds():
    ledRedPin=21
    ledGreenPin=20
    ledBluePin=19


    from machine import Pin
    from time import sleep

    red = Pin(ledRedPin, Pin.OUT)
    green = Pin(ledGreenPin, Pin.OUT)
    blue = Pin(ledBluePin, Pin.OUT)

    leds = [red, green, blue]


    red.value(0)
    green.value(0)
    blue.value(0)


    for x in leds:
        print(f'{x} is ON')
        x.toggle()
        sleep(.3)
        x.toggle()

    sleep(.3)
    print('All on')
    red.value(0)
    green.value(0)
    blue.value(0)
