# i2c_esp.py Test program for asi2c.py. Adapted for uasyncio V3, WBUS DIP28.
# Tests Responder on ESP8266.

# The MIT License (MIT)
#
# Copyright (c) 2018-2020 Peter Hinch
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import uasyncio as asyncio
from machine import Pin, I2C
from .asi2c import Responder
import ujson
import gc
gc.collect()

i2c = I2C(scl=Pin(0),sda=Pin(2))  # software I2C
syn = Pin(5)
ack = Pin(4)
chan = Responder(i2c, syn, ack)

async def receiver():
    sreader = asyncio.StreamReader(chan)
    await chan.ready()
    print('started')
    for _ in range(5):  # Test flow control
        res = await sreader.readline()
        print('Received', ujson.loads(res))
        await asyncio.sleep(4)
    while True:
        res = await sreader.readline()
        print('Received', ujson.loads(res))

async def sender():
    swriter = asyncio.StreamWriter(chan, {})
    txdata = [0, 0]
    while True:
        txdata[0] = gc.mem_free()
        await swriter.awrite(''.join((ujson.dumps(txdata), '\n')))
        txdata[1] += 1
        await asyncio.sleep_ms(1500)
        gc.collect()

asyncio.create_task(receiver())
try:
    asyncio.run(sender())
except KeyboardInterrupt:
    print('Interrupted')
finally:
    asyncio.new_event_loop()
    chan.close()  # for subsequent runs
