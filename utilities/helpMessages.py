import discord
from utilities.embeddedMessageHandler import Embedder

_send = Embedder()

class helper:

  def help(self):
    return _send.create_normal_embed_message("Fill later")

  def milk(self):
    return _send.create_embed_title_description("Drink :milk:","")