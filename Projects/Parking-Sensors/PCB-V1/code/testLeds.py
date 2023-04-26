
def testLeds():
    ledRedPin=21
    ledGreenPin=20
    ledBluePin=19
    sleepTime= 1



    from machine import Pin
    from time import sleep

    red = Pin(ledRedPin, Pin.OUT)
    green = Pin(ledGreenPin, Pin.OUT)
    blue = Pin(ledBluePin, Pin.OUT)
    
    red.value(0)
    green.value(0)
    blue.value(0)

    leds = [red, green, blue]


    red.value(0)
    green.value(0)
    blue.value(0)


    for x in leds:
        print(f'{x} is ON')
        x.toggle()
        sleep(sleepTime)
        x.toggle()
    
    print("All On")
    red.value(1)
    green.value(1)
    blue.value(1)
    
    sleep(sleepTime)
    
    print('All Off')
    red.value(0)
    green.value(0)
    blue.value(0)


while True:
    testLeds()



