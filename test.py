from typing import Collection
import discord
import os
import json

from utilities.databaseMaintainer import databaseMaintainer
from utilities.wordDetection import WordDetector

maintainer = databaseMaintainer()
detector = WordDetector()

from pathlib import Path

database = json.load(open(Path("database/words.json").absolute()))

print(database)