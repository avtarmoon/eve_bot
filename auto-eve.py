import itertools, operator, time, sys, threading
import win32con, ctypes.wintypes, win32gui,win32api
import autopy, Image, ImageGrab

from pilot import *
from top import *
    
if __name__ == '__main__':
    if len(sys.argv) ==1:
        TopmostMe()
        hotkey=Hotkey()
        hotkey.start()
        
        pilot=Pilot();
        if pilot.check_inspace():
            pilot.active_undock()
        else:
            pass