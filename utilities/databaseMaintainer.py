from operator import indexOf
import numpy as np
import os
import json

class databaseMaintainer:

    def __init__(self):
        self.database = json.load(open("database/words.json"))
        self.imageFolderPath = "pictures/"

    """
    Function checks if input word1 or word2 exists in the JSON database
    """
    def detectIfEntryExist(self, word1, word2):
        wordsFound = ([False, ""], [False, ""])
        for name in self.database["Names"]:
            for triggers in self.database["Names"][name][0]["triggers"]:
                if word1.find(triggers) >= 0:
                    wordsFound[0][0] = True
                    wordsFound[0][1] = name
                if word2.find(triggers) >= 0:
                    wordsFound[1][0] = True
                    wordsFound[1][1] = name
        #Both words existed, thus cannot be added
        if wordsFound[0][0] and wordsFound[1][0]:
            return True, None, None
        #Word 2 can be added to dictionary with word 1
        elif wordsFound[0][0]:
            return True, word2, wordsFound[0][1]
        #Word 1 can be added to dictionary with word 2
        elif wordsFound[1][0]:
            return True, word1, wordsFound[1][1]
        #Both words were not found in any dictionary
        else:
            return False, None, None

    """
    Adds a entry to the JSON database
    Checks firstly if the words is not already added somewhere in the database
    """
    def addNewEntry(self, word1, word2):
        wordCanBeAdded, word, jsonObject = self.detectIfEntryExist(word1, word2)
        if wordCanBeAdded:
            if word is None:
                print("Both words cannot be added, as they both exists in the database")
                return ""
            print("adding", word, "to JSON object", jsonObject)
            return ""
        else: 
            print("No inputs matching any words in database")
            return ""

    """
    Creates a new entry to the JSON database
    Checks firstly if the words is not already added somewhere in the database
    """
    def createNewEntry(self, word):
        
        return ""
    
    """
    Creates a new folder to the database
    """
    def createNewFolder(self, word):
        return ""
    
    """
    Adds a picture to the corresponding picture folder    
    """
    def addNewPicture(self, word, picture):
        return ""