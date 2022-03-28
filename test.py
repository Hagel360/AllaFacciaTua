from typing import Collection
import discord
import os
import json

from utilities.databaseMaintainer import databaseMaintainer
from utilities.wordDetection import WordDetector

maintainer = databaseMaintainer()
detector = WordDetector()

_, path = detector.findWhitelistedWord("svin")
print(detector.findPicturePath(path))

_, path = detector.findWhitelistedWord("mette")
print(detector.findPicturePath(path))