from typing import Collection
import discord
import os
from utilities.helpMessages import helper
from utilities.embeddedMessageHandler import Embedder
from utilities.wordDetection import WordDetector
from utilities.databaseMaintainer import databaseMaintainer

_send = Embedder()
helper = helper()
wordDetecter = WordDetector()
Maintainer = databaseMaintainer()
message = "frederiksen"

Maintainer.addNewEntry("mette", "mommy")
