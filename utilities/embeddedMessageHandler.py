from typing import Collection
import discord

class Embedder:

  def __init__(self):
    unlucky = "unlucky"

  def create_normal_embed_message(self, content):
    embed = discord.Embed(
      colour = discord.Colour.dark_gray(),
      description = content
      )
    return embed

  def create_embed_title_description(self, title, content):
    embed = discord.Embed(
      colour = discord.Colour.dark_gray(),
      title = title,
      description = content
      )
    return embed

  def embed_title_description_with_scroll(self, title, content):
    embed = discord.Embed(
      colour = discord.Colour.dark_gray(),
      title = title,
      description = content
      )
    return embed