# Code to run lil-j with the lil-j class

from machine import Pin, PWM
from liljclass import lilJ
from time import sleep
 
 
# # i2s setup
# sda = Pin(0)
# scl = Pin(1)
# id = 0
# # i2c = I2C(id=id, sda=sda, scl=scl)
# # robot = lilJ(i2c=i2c)


robot = lilJ()

# def avoid():
#     while True: 
#         if robot.distance >= 5:
#             robot.forward()
#             print("forward")      
#         else:
#             robot.backward()
#             robot.turnRight()
#             print("Back and right")

def motor_test():
    while True:
        print("Testing Left")
        robot.turnLeft()
        sleep(1)
        print("Testing Right ")
        robot.turnRight()
        sleep(1)
        print("Testing Forward")
        robot.forward()
        sleep(1)
        print("Testing Reverse ")
        robot.reverse()
        sleep(1)
    
def motor_stop():
    robot.setAllMotorsLow()


motor_test()

