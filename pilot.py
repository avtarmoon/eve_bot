import time, win32con, win32api
import autopy, Image, ImageGrab
import itertools, operator



class Pilot():

    def get_hash(img):
        image = img.convert("L")
        pixels = list(image.getdata())
        avg = sum(pixels) / len(pixels)
        return "".join(map(lambda p : "1" if p > avg else "0", pixels))
        
    def hamming_dist(hash1, hash2):
        return sum(itertools.imap(operator.ne, hash1, hash2))
    
    def active_undock(self):
        print "Ship will undock"
        autopy.mouse.move(885,218)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.05)
    
    def active_scanner(self):
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
       
    def active_disable_scanner(self):
        autopy.mouse.move(933,39)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.1)
        
    def active_goto_next_system(self):
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
    
    def active_surround_target(self):
        pass
    
    def active_warp_to_target(self,flag):
        pass

    def active_del_duplicate_target(self):
        pass

    def check_flying(self):
        pass
    
    def check_battle(self):
        pass

    def check_inspace(self):
        dock_screen = ImageGrab.grab((848,202,908,233))
        hashScreen = self.get_hash(dock_screen)
        hashBase = self.get_hash(Image.open("dock.png"))
        dist = self.hamming_dist(hashScreen, hashBase)
        if dist<10:
            return True
        else:
            print "Ship's already in space"
    
    def check_target(self):
        stack = {}
        hashC1 = self.get_hash(Image.open("C1.png"))
        hashC2 = self.get_hash(Image.open("C2.png"))
        hashC3 = self.get_hash(Image.open("C3.png"))
        hashC4 = self.get_hash(Image.open("C4.png"))
        
        for x in range(0,20,1):
            target_screen = ImageGrab.grab((725,237+x*20,781,254+x*20))
            hashScreen = get_hash(target_screen)
            distC1 = hamming_dist(hashScreen, hashC1)
            distC2 = hamming_dist(hashScreen, hashC2)
            distC3 = hamming_dist(hashScreen, hashC3)
            distC4 = hamming_dist(hashScreen, hashC4)
            
            if distC1<10:
                stack.append[x:1]
            elif distC2<10:
                stack.append[x:2]
            elif distC3<10:
                stack.append[x:3]
            elif distC4<10:
                stack.append[x:4]
            else:
                stack.append[x:0]
                
        if max(stack.items(), key=lambda x:x[1])[1]>=1:
            return max(stack.items(), key=lambda x:x[1])[0] 
        
