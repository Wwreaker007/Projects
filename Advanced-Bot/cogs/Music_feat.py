import discord
import random
import youtube_dl
import os
from replit import db
import asyncio
from discord.ext import commands

#List of the url to play
url_list = ["https://www.youtube.com/watch?v=bdE_SyHad90",
            "https://www.youtube.com/watch?v=U9pGr6KMdyg"]

#Function to run till end of the song
def endSong(guild, path):
  os.remove(path)

#Now we make use of replit database for storing the songs and playlists
def add_song(value):
  req, url = value.split(",",1)
  author, song = req.split("-",1)

  #Converting into lower case to avoid issues
  author = author.lower()
  song = song.lower()

  #We also add the song to an random list
  if "all" in db.keys():
    rand_list = db["all"]
    rand_list.append(song)
    db["all"] = rand_list
  else:
    db["all"] = [song]

  #If the author is present in the keys 
  if author in db.keys():
    song_list = db[author]
    song_list.append(song)
    db[author] = song_list
    db[song] = url
  else:
    new_list = []
    new_list.append(song)
    db[author] = new_list
    db[song] = url

#We now make new functions to play different songs
class Music_feat(commands.Cog):

  #Constructor
  def __init__(self,client):
    self.client = client
    self.general_vc = 829714354152800290
    #self.looping = True

  #Command to join the voice channel
  @commands.command()
  async def join(self, ctx):
    channel = self.client.get_channel(self.general_vc)
    await channel.connect()
  
  #Command to leave the voice channel
  @commands.command()
  async def leave(self, ctx):
    channel = self.client.get_channel(self.general_vc)
    if channel.is_playing() == True:
      await asyncio.sleep(1)
      await ctx.send('Please wait for the song to finish.')
    else:
      await channel.disconnect()

  #Command to add a song to the db
  @commands.command()
  async def add(self, ctx, *,name):
    add_song(name)
    await ctx.send('**Song **added!')

  #This function is used to run a particular playlist
  @commands.command(pass_context=True)
  async def playrandom(self, ctx):

    #These are the functions for best audio
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    
    path = str
    guild = ctx.message.guild
    channel = self.client.get_channel(self.general_vc)
    voice_client = await channel.connect()

    #Now we use all the songs in the database
    songs_list = db["all"]
    
    for song_name in songs_list:
      url = db[song_name.lower()]
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        file = ydl.extract_info(url, download=True)
        path = str(file['title']) + "-" + str(file['id'] + ".mp3")

        voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

        await ctx.send(f'**Music: **{url}')

      while voice_client.is_playing():
          await asyncio.sleep(1)
    
    if voice_client.is_playing() == False:
      await voice_client.disconnect()
      print("Disconnected")
      print(path)

  #This function is used to run a particular playlist
  @commands.command(pass_context=True)
  async def playlist(self, ctx, playlist):

    #These are the functions for best audio
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    
    #Connecting to the channel
    path = str
    guild = ctx.message.guild
    channel = self.client.get_channel(self.general_vc)
    voice_client = await channel.connect()

    #Now we extract the songs from the playlist
    songs_list = db[playlist.lower()]
    
    for song_name in songs_list:
      url = db[song_name.lower()]
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        file = ydl.extract_info(url, download=True)
        path = str(file['title']) + "-" + str(file['id'] + ".mp3")

        voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

        await ctx.send(f'**Music: **{url}')

      while voice_client.is_playing():
          await asyncio.sleep(1)
    
    if voice_client.is_playing() == False:
      await voice_client.disconnect()
      print("Disconnected")
      print(path)

  #This function helps in playing a author list
  @commands.command(pass_context=True)
  async def playauth(self, ctx, *, author):

    #These are the functions for best audio
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    
    #Connected to the voice client
    path = str
    guild = ctx.message.guild
    channel = self.client.get_channel(self.general_vc)
    voice_client = await channel.connect()

    #Now we take the list of the songs by that author and play randomly
    author_list = db[author.lower()]
    random.shuffle(author_list)

    #We now loop for each song in the author list
    for song_name in author_list:
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = db[song_name.lower()]
        file = ydl.extract_info(url, download=True)
        path = str(file['title']) + "-" + str(file['id'] + ".mp3")

        voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

        await ctx.send(f'**Music: **{url}')

      while voice_client.is_playing():
          await asyncio.sleep(1)
    
    if voice_client.is_playing() == False:
      await voice_client.disconnect()
      print("Disconnected")
      print(path)
  
  #This is used for playing a particular song.
  @commands.command(pass_context=True)
  async def play(self, ctx, *, name):

    #These are the functions for best audio
    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    
    #Connected to the voice channel
    path = str
    guild = ctx.message.guild
    channel = self.client.get_channel(self.general_vc)
    voice_client = await channel.connect()

    await ctx.send(name)
    req, loop = name.split(",", 1)
    author,song_name = req.split("-",1)
    
    author = author.lower()
    song_name = song_name.lower()

    #Here we check of we have the song, or else we to add the song
    if author not in db.keys():
      await ctx.send("Please use '$add' to add the song")
      return

    url = db[song_name]
    val = int(loop)
    if val == -1:
      val = 20

    #We do this for the valing music
    while(val >= 1):
      val = val - 1
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        file = ydl.extract_info(url, download=True)
        path = str(file['title']) + "-" + str(file['id'] + ".mp3")

        voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

        await ctx.send(f'**Music: **{url}')

      while voice_client.is_playing():
          await asyncio.sleep(1)
    
    if voice_client.is_playing() == False:
      await voice_client.disconnect()
      print("Disconnected")
      print(path)

def setup(client):
  client.add_cog(Music_feat(client))  