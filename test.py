from typing import Collection
import discord
import os
import json

from utilities.databaseMaintainer import databaseMaintainer

maintainer = databaseMaintainer()

test_sentence = "jonas store leder"

maintainer.addNewEntry("mette", "frederiksen")
maintainer.addNewEntry("jonas", "qwerty")
maintainer.addNewEntry("qwertty", "jonas")
maintainer.addNewEntry("qwerty", "qwerty")