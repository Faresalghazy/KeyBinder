# Program by Fares Al Ghazy started 20/5/2017
# Python script to assign key combinations to bash commands, should run in the background at startup
# Since this program is meant to release bash code, it is obviously non-system agnostic and only works linux systems that use BASH
# This is one file which only creates the GUI, another file is needed to use the info taken by this program

FileName  = 'BinderData.txt'

import tkinter as tk
from ComboDetect import ComboDetector

# Create a class to get pressed keys and print them
KeyManager = ComboDetector()


# Class that creates GUI and takes info to save in file

class MainFrame(tk.Tk):
    # variable to store pressed keys
    KeyCombination = ""
    testcounter = 1
    # function to write to file
    def SaveFunction(self, e1, e2, FileName):
        file = open(FileName, "a")
        combo = e1.get() + '\n'
        performed = e2.get() + '\n'
        file.write(combo)
        file.write(performed)
        file.close()

    def KeysPressed(self, Entry, KeyCombination):
        Entry.config(state="normal")
        Entry.insert(tk.END, "Test")
        print("test "+str(self.testcounter))
        self.testcounter = self.testcounter + 1
        KeyCombination = str (KeyManager.getpressedkeys())
        Entry.delete(0, tk.END)
        Entry.insert(tk.END, KeyCombination)

    # constructor

    def __init__(self, FileName, **kwargs):
        tk.Tk.__init__(self, **kwargs)
        # create GUI to take in key combinations and bash codes, then save them in file
        root = self  # create new window
        root.wm_title("Key binder")  # set title
        #  create labels and text boxes
        KeyComboLabel = tk.Label(root, text="Key combination = ")
        KeyComboEntry = tk.Entry(root)

        # Bind function to entry

        KeyComboEntry.bind('<FocusIn>', lambda e: self.KeysPressed(KeyComboEntry, self.KeyCombination))

        ActionLabel = tk.Label(root, text="Command to be executed = ")
        ActionEntry = tk.Entry(root)
        # place widgets in positions
        KeyComboLabel.grid(row=0, column=0, sticky=tk.E)
        ActionLabel.grid(row=1, column=0, sticky=tk.E)

        KeyComboEntry.grid(row=0, column=1)
        ActionEntry.grid(row=1, column=1)
        # create save button
        SaveButton = tk.Button(root, text="save",
                               command=lambda: self.SaveFunction(KeyComboEntry, ActionEntry, FileName))
        SaveButton.grid(row=2, column=2, sticky=tk.E)


app = MainFrame(FileName)
app.mainloop()