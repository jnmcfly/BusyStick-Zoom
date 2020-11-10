from blinkstick import blinkstick
import random
import psutil

stick = blinkstick.find_first()

def zoom():
    zoomPID = 0
    while True:
        for proc in psutil.process_iter():
            if proc.name() == "zoom":
                zoomPID = proc.pid
        if zoomPID in (p.pid for p in psutil.net_connections()):
            stick.morph(name="red")
        else:
            stick.morph(name="green")
        pass
    pass

zoom()