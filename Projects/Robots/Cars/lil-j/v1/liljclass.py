
#imports
from machine import Pin # access to gpio pins
from time import sleep 


#Class to control lil-j (little junk)
class lilJ():
    name = "Little Junk aka lil-j"

    def __init__ (self, i2c = None, name = None, in1 = None, in2 = None, in3=None, in4=None): # Add i2c for externals that use it
        if in1 or in2 or in3 or in4 == None: # if input pins arent set we will use basic setup here
            in1 = 28
            in2 = 27
            in3 = 26
            in4 = 22
        
        #Set the motor inputs for the drive board
        self.motor_A_forward = Pin(in1, Pin.OUT)
        self.motor_A_reverse = Pin(in2, Pin.OUT)
        self.motor_B_forward = Pin(in3, Pin.OUT)
        self.motor_B_reverse = Pin(in4, Pin.OUT)

        #Setting Name
        if not name:
            self.name = "picoSMARS"

        # only if i2c is sent
        self.i2c  = i2c
        if i2c:
            if self.i2c.scan() == []:
                raise RuntimeError("No I2C device found")
            #raise error if peripheral is not found

    def setAllMotorsLow(self):
        self.motor_A_forward.low()
        self.motor_B_forward.low()
        self.motor_A_reverse.low()
        self.motor_B_reverse.low()
        
    # Functions to move robot
    def forward(self):
        self.motor_A_forward.low()
        self.motor_A_reverse.high()
        self.motor_B_forward.high()
        self.motor_B_reverse.low()
        sleep(5)
        lilJ.setAllMotorsLow(self)
        
    def reverse(self):
        self.motor_A_forward.high()
        self.motor_A_reverse.low()
        self.motor_B_forward.low()
        self.motor_B_reverse.high()
        sleep(0.5)
        lilJ.setAllMotorsLow(self)

    def turnLeft(self):
        self.motor_A_forward.high()
        self.motor_A_reverse.low()
        self.motor_B_forward.high()
        self.motor_B_reverse.low()
        sleep(0.5)
        lilJ.setAllMotorsLow(self)
        
    def turnRight(self):
        self.motor_A_forward.low()
        self.motor_A_reverse.high()
        self.motor_B_forward.low()
        self.motor_B_reverse.high()
        sleep(0.5)
        lilJ.setAllMotorsLow(self)

    # @property
    # def distance(self):
    #     # Get disance in cm
    #     distance = (self.range_finder.ping()/10) - 5
    #     return distance
    




"""
PWM Contorl

#imports
from machine import Pin, PWM  # access to gpio pins and PWM
from time import sleep

#Class to control lil-j (little junk)
class lilJ():
    name = "Little Junk aka lil-j"

    def __init__(self, i2c=None, name=None, in1=None, in2=None, in3=None, in4=None, default_speed=50): # Add i2c for externals that use it
        if in1 or in2 or in3 or in4 == None: # if input pins arent set we will use basic setup here
            in1 = 2
            in2 = 3
            in3 = 4
            in4 = 5
        
        self.default_speed = default_speed

        #Set the motor inputs for the drive board
        self.motor_A_forward = PWM(Pin(in1), freq=50, duty=self.default_speed)
        self.motor_A_reverse = PWM(Pin(in2), freq=50, duty=self.default_speed)
        self.motor_B_forward = PWM(Pin(in3), freq=50, duty=self.default_speed)
        self.motor_B_reverse = PWM(Pin(in4), freq=50, duty=self.default_speed)

        #Setting Name
        if not name:
            self.name = "picoSMARS"

        # only if i2c is sent
        self.i2c  = i2c
        if i2c:
            if self.i2c.scan() == []:
                raise RuntimeError("No I2C device found")
            #raise error if peripheral is not found

    def set_speed(self, speed):
        self.default_speed = speed
        self.motor_A_forward.duty(self.default_speed)
        self.motor_A_reverse.duty(self.default_speed)
        self.motor_B_forward.duty(self.default_speed)
        self.motor_B_reverse.duty(self.default_speed)

    def stop(self):
        self.motor_A_forward.duty(0)
        self.motor_A_reverse.duty(0)
        self.motor_B_forward.duty(0)
        self.motor_B_reverse.duty(0)

    # Functions to move robot
    def forward(self, speed=None):
        if speed is not None:
            self.set_speed(speed)
        self.motor_A_forward.duty(0)
        self.motor_A_reverse.duty(self.default_speed)
        self.motor_B_forward.duty(self.default_speed)
        self.motor_B_reverse.duty(0)
        sleep(0.5)
        self.stop()

    def reverse(self, speed=None):
        if speed is not None:
            self.set_speed(speed)
        self.motor_A_forward.duty(self.default_speed)
        self.motor_A_reverse.duty(0)
        self.motor_B_forward.duty(0)
        self.motor_B_reverse.duty(self.default_speed)
        sleep(0.5)
        self.stop()

    def turnLeft(self, speed=None):
        if speed is not None:
            self.set_speed(speed)
        self.motor_A_forward.duty(self.default_speed)
        self.motor_A_reverse.duty(0)
        self.motor_B_forward.duty(self.default_speed)
        self.motor_B_reverse.duty(0)
      

        
--------------fdsfhgdjsdasdfhgjhdsagefaDBfzngmdhkf 

class lilJ():
    name = "Little Junk aka lil-j"

    def __init__ (self, i2c = None, name = None, in1 = None, in2 = None, in3=None, in4=None):
        if in1 or in2 or in3 or in4 == None:
            in1 = 2
            in2 = 3
            in3 = 4
            in4 = 5
        
        self.motor_A_forward = Pin(in1, Pin.OUT)
        self.motor_A_reverse = Pin(in2, Pin.OUT)
        self.motor_A_pwm = PWM(self.motor_A_forward)
        self.motor_B_forward = Pin(in3, Pin.OUT)
        self.motor_B_reverse = Pin(in4, Pin.OUT)
        self.motor_B_pwm = PWM(self.motor_B_forward)

        if not name:
            self.name = "picoSMARS"

        self.i2c  = i2c
        if i2c:
            if self.i2c.scan() == []:
                raise RuntimeError("No I2C device found")

    def setAllMotorsLow(self):
        self.motor_A_pwm.duty_u16(0)
        self.motor_B_pwm.duty_u16(0)
        self.motor_A_reverse.low()
        self.motor_B_reverse.low()
        
    def forward(self, speed=32768):
        self.motor_A_pwm.duty_u16(speed)
        self.motor_A_reverse.high()
        self.motor_B_pwm.duty_u16(speed)
        self.motor_B_reverse.low()
        sleep(0.5)
        self.setAllMotorsLow()
        
    def reverse(self, speed=32768):
        self.motor_A_pwm.duty_u16(speed)
        self.motor_A_reverse.low()
        self.motor_B_pwm.duty_u16(speed)
        self.motor_B_reverse.high()
        sleep(0.5)
        self.setAllMotorsLow()

    def turnLeft(self, speed=32768):
        self.motor_A_pwm.duty_u16(speed)
        self.motor_A_reverse.low()
        self.motor_B_pwm.duty_u16(speed)
        self.motor_B_reverse.low()
        sleep(0.5)
        self.setAllMotorsLow()
        
    def turnRight(self, speed=32768):
        self.motor_A_pwm.duty_u16(speed)
        self.motor_A_forward.low()
        self.motor_B_pwm.duty_u16(speed)
        self.motor_B_forward.low()
        sleep(0.5)
        self.setAllMotorsLow()

        """
