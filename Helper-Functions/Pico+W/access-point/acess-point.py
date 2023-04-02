# Pico W access point mode with index page

# Pico W access point mode with index page

from phew import logging, template, server, access_point, dns
from phew.template import  render_template
from phew.server import redirect
from liljclass import lilJ

import gc
gc.threshold(50000) # setup garbage collection

DOMAIN = "pico.wifi" # This is the address that is shown on the Captive Portal/ Domain that it can be access with instead of IP
apName = "pico-W-lil-J" # Name of the WIFI - SSID

robot = lilJ()

@server.route("/", methods=['GET','POST'])
def index(request):
    try:
        """ Render the Index page and respond to form requests """
        if request.method == 'GET':
            logging.debug(f"GET request from$ {request.headers['user-agent']}")
            return render_template("index.html")
        if request.method == 'POST':
            logging.debug(f"POST request from$ {request.headers['user-agent']}")
           # print(f"request$ {request}")
           # print(f"request eaders user agent$ {request.headers['user-agent']}")
            #text = str(request.form.values())
            text = request.form.get("This-Is-A-Post", None)
            #print(f"text$ {text}")
            logging.debug(f'posted message: {text}')
            
            return render_template("index.html", text=text)
    except Exception as error:
        logging.debug(f"30 Erorr$ {error}")
        return render_template("index.html")

@server.route("/wrong-host-redirect", methods=["GET"])
def wrong_host_redirect(request):
  # if the client requested a resource at the wrong host then present 
  # a meta redirect so that the captive portal browser can be sent to the correct location
  body = "<!DOCTYPE html><head><meta http-equiv=\"refresh\" content=\"0;URL='http://" + DOMAIN + "'/ /></head>"
  logging.debug("body:",body)
  return body

@server.route("/hotspot-detect.html", methods=["GET"])
def hotspot(request):
    """ Redirect to the Index Page """
    return render_template("index.html")

@server.catchall()
def catch_all(request):
    """ Catch and redirect requests """
    if request.headers.get("host") != DOMAIN:
        return redirect("http://" + DOMAIN + "/wrong-host-redirect")

# Set to Accesspoint mode
ap = access_point(apName)  # Change this to whatever Wifi SSID you wish
ip = ap.ifconfig()[0]                   # Grab the IP address and store it
logging.info(f"starting DNS server on {ip}")
dns.run_catchall(ip)                    # Catch all requests and reroute them
server.run()                            # Run the server
logging.info("Webserver Started")



"""
BaCKUP 
# CyberDog 
# Kevin McAleer
# September 2022

from phew import logging, template, server, access_point, dns
from phew.template import  render_template
from phew.server import redirect
import gc
gc.threshold(50000) # setup garbage collection

DOMAIN = "pico.wireless" # This is the address that is shown on the Captive Portal

@server.route("/", methods=['GET','POST'])
def index(request):
    """ Render the Index page and respond to form requests """
    if request.method == 'GET':
        logging.debug("Get request")
        return render_template("index.html")
    if request.method == 'POST':
        text = request.form.get("text", None)
        logging.debug(f'posted message: {text}')
        return render_template("index.html", text=text)

@server.route("/wrong-host-redirect", methods=["GET"])
def wrong_host_redirect(request):
  # if the client requested a resource at the wrong host then present 
  # a meta redirect so that the captive portal browser can be sent to the correct location
  body = "<!DOCTYPE html><head><meta http-equiv=\"refresh\" content=\"0;URL='http://" + DOMAIN + "'/ /></head>"
  logging.debug("body:",body)
  return body

@server.route("/hotspot-detect.html", methods=["GET"])
def hotspot(request):
    """ Redirect to the Index Page """
    return render_template("index.html")

@server.catchall()
def catch_all(request):
    """ Catch and redirect requests """
    if request.headers.get("host") != DOMAIN:
        return redirect("http://" + DOMAIN + "/wrong-host-redirect")

# Set to Accesspoint mode
ap = access_point("Wifi In The Woods")  # Change this to whatever Wifi SSID you wish
ip = ap.ifconfig()[0]                   # Grab the IP address and store it
logging.info(f"starting DNS server on {ip}")
dns.run_catchall(ip)                    # Catch all requests and reroute them
server.run()                            # Run the server
logging.info("Webserver Started")

"""
"""

from phew import server, connect_to_wifi

connect_to_wifi("<ssid>", "<password>")

@server.route("/random", methods=["GET"])
def random_number(request):
  import random
  min = int(request.query.get("min", 0))
  max = int(request.query.get("max", 100))
  return str(random.randint(min, max))

@server.catchall()
def catchall(request):
  return "Not found", 404

server.run()
"""