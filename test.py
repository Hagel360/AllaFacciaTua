from typing import Collection
import discord
from utilities.helpMessages import helper
from utilities.embeddedMessageHandler import compute_and_send_message
from utilities.wordDetection import WordDetector

_send = compute_and_send_message()
helper = helper()
wordDetecter = WordDetector()

message = "frederiksen"

word = wordDetecter.listallenumorators(message)
print(word)