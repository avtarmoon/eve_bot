import itertools, operator, time, sys, threading
import win32con, ctypes.wintypes, win32gui,win32api
import autopy, Image, ImageGrab

class Hotkey(threading.Thread):

    def run(self):
        global EXIT
        user32 = ctypes.windll.user32
        print "Register exit hotkey"
        if not user32.RegisterHotKey(None, 99, win32con.MOD_WIN, win32con.MOD_ALT):
            '''WIN+ALT, hotkey used to stop the thread'''
            raise RuntimeError
        try:
            msg = ctypes.wintypes.MSG()
            print msg
            while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    if msg.wParam == 99:
                        EXIT = True
                        return
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            user32.UnregisterHotKey(None, 1)

class Pilot():
    def Undock(self):
        print "Ship will undock"
        autopy.mouse.move(885,218)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.05)
    
    def activescanner(self):
        autopy.mouse.move(590,144)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.1)
        autopy.mouse.move(560,144)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.1)
       
    def disablescanner(self):
        autopy.mouse.move(933,39)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.1)
        
    def goto_nextsystem(self):
        autopy.mouse.move(271, 196)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0) 
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        time.sleep(0.1)
        autopy.mouse.move(295, 203)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.1)
   
    def active_accelerationorbit(self):
        pass
    
    def active_surround(self):
        pass
    
    def active_warptotarget(self):
        pass
          
    def check_inspace(self):
        dock_screen = ImageGrab.grab((848,202,908,233))
        hashScreen = get_hash(dock_screen)
        hashBase = get_hash(Image.open("dock.png"))
        dist = hamming_dist(hashScreen, hashBase)
        if dist<10:
            return True
        else:
            print "Ship's already in space"
        
def TopmostMe():
    hwnd = win32gui.GetForegroundWindow()
    (left, top, right, bottom) = win32gui.GetWindowRect(hwnd)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, left, top, right-left, bottom-top, 0)
 
def get_hash(img):
        image = img.convert("L")
        pixels = list(image.getdata())
        avg = sum(pixels) / len(pixels)
        return "".join(map(lambda p : "1" if p > avg else "0", pixels))
        
def hamming_dist(hash1, hash2):
        return sum(itertools.imap(operator.ne, hash1, hash2))


if __name__ == '__main__':
    if len(sys.argv) ==1:
        TopmostMe()
        hotkey=Hotkey()
        hotkey.start()
        pilot=Pilot();
        if pilot.check_inspace():
            pilot.Undock()
        else:
            time.sleep(5)
            pilot.activescanner()
            time.sleep(5)
            pilot.disablescanner()
            time.sleep(5)
            pilot.goto_nextsystem()
    else:
        pass
        