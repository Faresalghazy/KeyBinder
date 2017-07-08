# Program by Fares Al Ghazy
# Script to link key combinations to bash scripts

import subprocess


# function to perform bash script

def DoBash(SomeText):
    subprocess.call(SomeText,
                    shell=True)  # shell = true is necessary, sometext is the bash command (may also be a .sh file)

#create dictionary from text file
def LoadDict(FileName):
    # need to read in this format : keycombination, command
    DataFile = open(FileName, 'r')
    # create dictionary : key= keycombo, value = dobash
    KeyDictionary = {}
    # iterate through lines of file, even is keycombo, odd is command
    i = int(1)
    for line in DataFile:
        # create a temporary list and string that will later be stored in the dictionary
        temporarylist = []
        # if the line is even, then find the key combination
        if i % 2:
            length = len(line)
            # keys seperated by plus sign
            indexofplus = line.find('+')
            while (indexofplus >= 0) and (indexofplus < length):
                tempstring = line[:indexofplus]
                temporarylist.extend(tempstring)
                indexofplus = line.find('+')
        # if line is odd
        else:
            # then add items to dictionary
            KeyDictionary[tuple(temporarylist)] = line.rstrip()  # line being the bash command, rstrip() removes the newline character
    DataFile.seek(0)  # so we are able to work with the file again, returns location of reading to the top of the file
    return KeyDictionary



