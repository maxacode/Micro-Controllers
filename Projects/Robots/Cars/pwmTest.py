import machine
import time

pin = machine.Pin(27, machine.Pin.OUT)
pwm = machine.PWM(pin)
pwm.freq(50)
 
pwm.duty_u16(51)
time.sleep(1)
for d in range(14000,75000, 1000):
    print(d)
    pwm.duty_u16(d)
    time.sleep(0.2)
pwm.duty_u16(0)
 
