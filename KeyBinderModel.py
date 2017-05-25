import subprocess
class Model:
    #constructor, which only creates the dictionary
    def __init__(self,Filename):
        #create dictionary from passed text file
        self.LoadDict(Filename)
    #function to load dictionary from txt file
    def LoadDict(FileName):
        # need to read in this format : keycombination, command
        DataFile = open(FileName, 'r')
        # create dictionary : key= keycombo, value = dobash
        KeyDictionary = {}
        # iterate through lines of file, even is keycombo, odd is command
        i = int(1)
        for line in DataFile:
            # create a temporary list and string that will later be stored in the dictionary
            temporarylist = [];
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
                KeyDictionary[tuple(temporarylist)] = line  # line being the bash command
        return KeyDictionary

    # function to perform bash script
    def DoBash(SomeText):
        subprocess.call(SomeText,
                        shell=True)  # shell = true is necessary, sometext is the bash command (may also be a .sh file)

    # function to perform an action from a key in a dictionary
    def ExecuteFromDic(self,dictionary, key):
        self.DoBash(dictionary[key])  # perform the bash script of the command returned from the dictionary