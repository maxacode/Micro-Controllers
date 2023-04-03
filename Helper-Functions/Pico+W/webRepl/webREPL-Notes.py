# https://github.com/micropython/webrepl

#webrepl_cli.py --help
#webrepl.html

#http://device:8266/ 
#http://micropython.org/webrepl/.
#https://forum.micropython.org/viewtopic.php?t=12684


# 1 Latest firmware (1.19.1 (stable) or latest nightly if not in a new stable version like 1.20)
# 2 Copy boot,manifest,webrepl_cfg, webrepl_setup, webrepl.py, connectToWlan.py filees to root
# 3 Run import connectWlan import webrepl webrepl.start - to set it up initally
"""
    from connectToWlan import connectWLAN
    ipInfo= connectWLAN()
    print(ipInfo)   
    import webrepl
    webrepl.start()

"""
# 4 Reboot - test - access via http://device-IP:8266
# 5 connect via thonny - Select Interpreter - micropython ESP32- web repl: ws://ip:8266 - password
