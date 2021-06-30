import discord
import random
import os
import youtube_dl
from Server import keep_alive

from discord.ext import commands

client = commands.Bot(command_prefix = '$')
players = {}
general = 829714354152800289

@client.event
async def on_ready():
  channel = client.get_channel(general)
  await channel.send('Ready') 
  print('Ready') 


#Here we include the extensions for the bot
@client.command()
async def load(ctx,extension):
  await ctx.load_extension(f'cogs.{extension}')

#Here we unload the extensions
@client.command()
async def unload(ctx,extension):
  await ctx.unload_extension(f'cogs.{extension}')

#Thiss reload cogs helps in reloading a Cog after edits
@client.command()
async def reload(ctx,extension):
  await ctx.unload_extension(f'cogs.{extension}')
  await ctx.load_extension(f'cogs.{extension}')

#We also load the cogs which we made of our own
for file in os.listdir('./cogs'):
  if file.endswith('.py'):
    client.load_extension(f'cogs.{file[:-3]}')
 
keep_alive()
client.run('ODMwMDg1NjQ0NDk1NzQ5MTIy.YHBjfw.7ie1gM56WieWkIm-Vl7-Mfkt5TA') 