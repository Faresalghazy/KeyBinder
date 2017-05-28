#this program was created by LadonAl (Alaa Youssef) in 25.May.17
#it detects a combination of pressed key and stores them in a list and prints the list when at least
# one of the keys is released

import time
import pyxhook

combo = []

s = ""

def pres(event):
    # appending the ScnCodes of pressed Keys to the combo list
    combo.append(event.ScanCode)
    global s
    if s != "":
        s += "+"
    s += event.Key


def rel(event):
    global running
    running = False


# Create hookmanager
hookman = pyxhook.HookManager()

# Define our callback to fire when a key is pressed down or released
hookman.KeyDown = pres

hookman.KeyUp = rel

# Hook the keyboard
hookman.HookKeyboard()

# Start our listener
hookman.start()

# Create a loop to keep the application running
running = True
while running:
    time.sleep(0.05)#make the delay shorter in case you encounter duplications

# Close the listener when we are done
hookman.cancel()
print(combo)
print(s)
