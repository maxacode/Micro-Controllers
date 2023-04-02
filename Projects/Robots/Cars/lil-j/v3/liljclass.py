
#imports
from machine import Pin, PWM # access to gpio pins
from time import sleep 

freq= 50

#Class to control lil-j (little junk)
class lilJ():
    name = "Little Junk aka lil-j"

    def __init__ (self, i2c = None, name = None, in1 = None, in2 = None, in3=None, in4=None, default_speed=80): # Add i2c for externals that use it
        if in1 or in2 or in3 or in4 == None: # if input pins arent set we will use basic setup here
            in1 = 28
            in2 = 27
            in3 = 26
            in4 = 22
            
            
            
        
        self.default_speed = default_speed
        print(self.default_speed)
        
        self.motor_A_forward-pin = PWM(Pin(in1, Pin.OUT))
        #Set the motor inputs for the drive board
        self.motor_A_forward = PWM(motor_A_forward-pin)
        self.motor_A_forward.freq(freq)
        self.motor_A_forward.duty_u16(self.default_speed)
        
        self.motor_A_reverse = PWM(Pin(in2))
        self.motor_A_reverse.freq(freq)
        self.motor_A_reverse.duty_u16(self.default_speed)
        
        self.motor_B_forward = PWM(Pin(in3))
        self.motor_B_forward.freq(freq)
        self.motor_B_forward.duty_u16(self.default_speed)
        
        self.motor_B_reverse = PWM(Pin(in4))
        self.motor_B_reverse.freq(freq)
        self.motor_B_reverse.duty_u16(self.default_speed)
        
 
        
        #Set the motor inputs for the drive board
        #self.motor_A_forward = PWM(Pin(in1, Pin.OUT))
       # self.motor_A_forward.frewq(20000)
       # self.motor_A_forward.duty_u16(0)
       # self.motor_A_reverse = Pin(in2, Pin.OUT)
       # self.motor_B_forward = Pin(in3, Pin.OUT)
       # self.motor_B_reverse = Pin(in4, Pin.OUT)

        #Setting Name
        if not name:
            self.name = "picoSMARS"

        print(name)
        # only if i2c is sent
        self.i2c  = i2c
        if i2c:
            if self.i2c.scan() == []:
                raise RuntimeError("No I2C device found")
            #raise error if peripheral is not found

    
    def set_speed(self, speed):
        self.default_speed = speed
        self.motor_A_forward.duty_u16(self.default_speed)
        self.motor_A_reverse.duty_u16(self.default_speed)
        self.motor_B_forward.duty_u16(self.default_speed)
        self.motor_B_reverse.duty_u16(self.default_speed)

    def testSpeed(self, speed=None):
        if speed is not None:
            self.set_speed(speed)
        print(f"Testing speed 0")
        self.motor_A_forward.duty_u16(0)
        self.motor_A_reverse.duty_u16(0)
        self.motor_B_forward.duty_u16(0)
        self.motor_B_reverse.duty_u16(0)
        sleep(1)
            
        for i in range(350, 1023, 10):
            print(f"Testing speed {i}")
            self.motor_A_forward.duty_u16(i)
            self.motor_A_reverse.duty_u16(i)
            self.motor_B_forward.duty_u16(i)
            self.motor_B_reverse.duty_u16(i)
            sleep(.1)
        
        self.setAllMotorsLow()
 


    def setAllMotorsLow(self):
        self.motor_A_forward.duty_u16(0)
        self.motor_A_reverse.duty_u16(0)
        self.motor_B_forward.duty_u16(0)
        self.motor_B_reverse.duty_u16(0)

    # Functions to move robot
    def forward(self, speed=None):
        print(speed)
        if speed is not None:
            self.set_speed(speed)
        self.motor_A_forward.duty_u16(0)
        self.motor_A_reverse.duty_u16(self.default_speed)
        self.motor_B_forward.duty_u16(self.default_speed)
        self.motor_B_reverse.duty_u16(0)
        sleep(2)
        print(speed)
        self.setAllMotorsLow()

    def reverse(self, speed=None):
        if speed is not None:
            self.set_speed(speed)
        self.motor_A_forward.duty_u16(self.default_speed)
        self.motor_A_reverse.duty_u16(0)
        self.motor_B_forward.duty_u16(0)
        self.motor_B_reverse.duty_u16(self.default_speed)
        sleep(0.5)
        self.setAllMotorsLow()

    def turnLeft(self, speed=None):
        if speed is not None:
            self.set_speed(speed)
        self.motor_A_forward.duty_u16(self.default_speed)
        self.motor_A_reverse.duty_u16(0)
        self.motor_B_forward.duty_u16(self.default_speed)
        self.motor_B_reverse.duty_u16(0)
        sleep(0.5)
        self.setAllMotorsLow()
        
    def turnRight(self, speed=None):
        if speed is not None:
            self.set_speed(speed)
        self.motor_A_forward.duty_u16(0)
        self.motor_A_reverse.duty_u16(self.default_speed)
        self.motor_B_forward.duty_u16(0)
        self.motor_B_reverse.duty_u16(self.default_speed)
        sleep(0.5)
        self.setAllMotorsLow()
        
    
    # @property
    # def distance(self):
    #     # Get disance in cm
    #     distance = (self.range_finder.ping()/10) - 5
    #     return distance
    



 