"""
LDR Test
"""

import time
from ldr import LDR
 
 
bluePin = 16
greenPin = 17
redPin  = 18

ldrPin = 26

ldr = LDR(ldrPin)
print(ldr.percent())
print(ldr.raw())

 

from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket

# Initialize MicroDot
app = Microdot()
Response.default_content_type = 'text/html'
 



#Take request and perform according action
@app.route('/')
async def index(request):
    return render_template('index.html')


@app.route('/ws')
@with_websocket
async def read_sensor(request, ws):
    while True:
#         data = await ws.receive()
        time.sleep(.1)
        await ws.send(str(ldr.percent()))

# Static CSS/JSS
@app.route("/static/<path:path>")
def static(request, path):
    if ".." in path:
        # directory traversal is not allowed
        return "Not found", 404
    return send_file("static/" + path)


# shutdown
@app.get('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'


if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        pass

    
 
