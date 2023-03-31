
#imports
from machine import Pin # access to gpio pins
from time import sleep 


#Class to control lil-j (little junk)
class lilJ():
    name = "Little Junk aka lil-j"

    def __init__ (self, i2c = None, name = None, in1 = None, in2 = None, in3=None, in4=None): # Add i2c for externals that use it
        if in1 or in2 or in3 or in4 == None: # if input pins arent set we will use basic setup here
            in1 = 2
            in2 = 3
            in3 = 4
            in4 = 5
        
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
        sleep(0.5)
        lilJ.setAllMotorsLow()
        
    def reverse(self):
        self.motor_A_forward.high()
        self.motor_A_reverse.low()
        self.motor_B_forward.low()
        self.motor_B_reverse.high()
        sleep(0.5)
        lilJ.setAllMotorsLow()

    def turnLeft(self):
        self.motor_A_forward.high()
        self.motor_A_reverse.low()
        self.motor_B_forward.high()
        self.motor_B_reverse.low()
        sleep(0.5)
        lilJ.setAllMotorsLow()
        
    def turnRight(self):
        self.motor_A_forward.low()
        self.motor_A_reverse.high()
        self.motor_B_forward.low()
        self.motor_B_reverse.high()
        sleep(0.5)
        lilJ.setAllMotorsLow()

    # @property
    # def distance(self):
    #     # Get disance in cm
    #     distance = (self.range_finder.ping()/10) - 5
    #     return distance
    