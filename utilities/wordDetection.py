import discord
import numpy as np
import os
import random
import json

class WordDetector:

    def __init__(self):
        self.database = json.load(open("database/words.json"))
        self.imageFolderPath = "pictures/"

    # Checks if the message contains a whitelisted word that is in the database
    def findWhitelistedWord(self, message):
        sentence = message.lower()
        database = self.database
        for names in database["Names"]:
            for trigger in database["Names"][names][0]["triggers"]:
                if sentence.find(trigger) >= 0:
                    return True, database["Names"][names][1]["folder"]
        return False, ""

    #Finds a corresponding picture from the given words, returns a path to a random picture from that folder
    def findPicturePath(self, word):
        try:
            pictures = os.listdir(self.imageFolderPath+word)
            randomInt = random.randint(1, len(pictures))
            return self.imageFolderPath+word+"/"+pictures[randomInt]
        except:
            print("Folder not found")

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