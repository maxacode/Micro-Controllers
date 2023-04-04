#https://www.youtube.com/watch?v=Xch1VZgfH5c&t=307
 #https://techtotinker.com/2021/08/044-micropython-technotes-infrared-receiver/

#https://github.com/peterhinch/micropython_ir

# More details can be found in TechToTinker.blogspot.com 
# George Bantique | tech.to.tinker@gmail.com

import time
from machine import Pin
#from ir_rx import NEC_16

import ir_rx.nec
#from ir_rx.acquire import test

#while True:
   # print("new Test")
   # test()

def callback(data, addr, ctrl):
    if data > 0:  # NEC protocol sends repeat codes.
        print('Data {:02x} Addr {:04x}'.format(data, addr))

ir = NEC_16(Pin(4, Pin.IN), callback)
