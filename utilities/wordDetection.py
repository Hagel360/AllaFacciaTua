import discord
import numpy as np
import os
import random

class WordDetector:

    def __init__(self):
        self.whitelist = np.genfromtxt("utilities/whitelistedWords.csv", dtype='str', delimiter=',')
        self.imageFolderPath = "pictures/"

    # Checks if the message contains a whitelisted words
    # TODO: Handle cases where there is no spaces such as "mettefrederiksen".
    # TODO: Handle cases with two words, such as "store leder".
    def findWhitelistedWord(self, message):
        messageList = message.lower().split()
        for x in messageList:
            print(x)
            for list in self.whitelist:
                for y in list:
                    print(y)
                    if x == y and x != "0":
                        return True, list[0]
        return False, ""

    #Finds a corresponding picture from the given words, returns a path to a random picture from that folder
    def findPicturePath(self, word):
        pictures = os.listdir(self.imageFolderPath+word)
        randomInt = random.randint(1, len(pictures))
        return self.imageFolderPath+word+"/"+pictures[randomInt]

    def createNewWord(self, word):
        return "test0"

    #Adds a new word to the corresponding "word" list
    def addNewWordtoList(self, message):
        return "Test2"

    #Returns alle the enumorators in the list
    def listallenumorators(self, message):
        message = message.lower()
        for list in self.whitelist:
            for x in list:
                if message == x and message != "0":
                    retval = ""
                    for y in list:
                        if y != '0':
                            retval += str(y) + ", "
                    return True, "The word occur in the database with: " + retval[:-2]
        return True, "The word does not occur in the database"

    #Adds picture to the corresponding "word" folder
    def addPicture(self, word, picture):
        return "Test3"