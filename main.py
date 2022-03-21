import discord
import sys
from ast import arg
from typing import Collection
from utilities.helpMessages import helper
from utilities.embeddedMessageHandler import Embedder
from utilities.wordDetection import WordDetector

_send = Embedder()
helper = helper()
wordDetecter = WordDetector()

def switch_branch(message):
    arguments = [args.lower() for args in message.content.split()]
    # only one argument "!A arg1"
    if(len(arguments) == 2):
        switch_one = {
        "help": helper.help(),
        "milk": helper.milk()
        }
        return switch_one.get(arguments[1], "switch_branch.switch_one Error")

    # more than two arguments "!A arg1 arg2 arg3 etc."
    if(len(arguments) > 2):
        switch_two = {
        "add": wordDetecter.addNewWordtoList(arguments[2], arguments[3]),
        "create": wordDetecter.createNewWord(arguments[2]),
        "find": wordDetecter.listallenumorators(arguments[2])
        }
        return switch_two.get(arguments[1], "switch_branch.switch_one Error")


#Main loop
client = discord.Client()
@client.event
async def on_ready():
    print('Hello, i am {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!A"):
        truthval, retval = switch_branch(message)
        if truthval:
            embed = _send.create_normal_embed_message(retval)
        else:
            embed = helper.help()
        await message.channel.send(embed=embed)
        return

    # If a message contains a whitelisted word, find the corresponding image and post it.
    wordFound, folderName = wordDetecter.findWhitelistedWord(message.content)
    if wordFound:
        picture = discord.File(wordDetecter.findPicturePath(folderName))
        await message.channel.send(file=picture)
        return

if __name__ == "__main__":
    client.run(sys.argv[1])