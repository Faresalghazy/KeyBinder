#this program was created by LadonAl (Alaa Youssef) in 25.May.17
#it detects a combination of pressed key and stores them in a list and prints the list when at least
# one of the keys is released

import time
import pyxhook


class ComboDetector(object):
    combo = []
    comKey = ""
    running = True

    def pres(self, event):
        # appending the ScnCodes of pressed Keys to the combo list
        self.combo.append(event.ScanCode)
        if self.comKey != "":
            self.comKey += "+"
        self.comKey += event.Key

    def rel(self, event):	
        self.running = False

    def __init__(self, combos=[], keys=""):
        time.sleep(0.1)
        self.combo = combos
        self.comKey = keys
       

    def getpressedkeys(self):
        self.running = True
        self.combo = []
        self.dcomKey = ""
        time.sleep(0.15)

        # Create hookmanager
        hookman = pyxhook.HookManager()

        # Define our callback to fire when a key is pressed down or released
        hookman.KeyDown = self.pres

        hookman.KeyUp = self.rel

        # Hook the keyboard
        hookman.HookKeyboard()

        # Start our listener
        hookman.start()

        # Create a loop to keep the application running
        while self.running:
            time.sleep(0.09)  # make the delay longer in case you encounter duplications

        # Close the listener when we are done
        hookman.cancel()
        print("got keys = " + str(self.combo))
        return self.combo

    @staticmethod
    def getkeys(self):
        return self.comKey

#r = ComboDetector()
#print(r.getpressedkeys())
#print(r.getkeys(r))
