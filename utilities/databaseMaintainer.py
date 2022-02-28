from operator import indexOf
import numpy as np
import os

class databaseMaintainer:

    def __init__(self):
        self.database = np.genfromtxt("utilities/whitelistedWords.csv", dtype='str', delimiter=',')
        self.imageFolderPath = "pictures/"

    # Finds the first avaible empty spot for new word to be added, returns -1 if there is none.
    def findEmptySpotIndex(self, row):
        try:
            return indexOf(row, "0")
        except:
            return -1

    def addNewEntry(self, word1, word2):
        for rows in self.database:
            for y in rows:
                if word1 == y:
                    index = self.findEmptySpotIndex(rows)
                    if index < 0:
                        rows.append(word2)
                elif word2 == y:
                    index = self.findEmptySpotIndex(rows)
                    if index < 0:
                        rows.append(word1)
                else:
                    return "Word does not exist"
        self.fixUnevenRows()

    def fixUnevenRows(self):
        return "test"

    def createNewEntry(self, word):
        for rows in self.database:
            for y in rows:
                if word == y:
                    return "Word already exist in database, cannot be added"
        self.database.append(word)

    def createNewFolder(self, word):
        return "test"
    
    def addNewPicture(self, word, picture):
        return "test"