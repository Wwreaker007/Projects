import discord
from discord.ext import commands


#Here we define an extension which is a COG
class Basic_feat(commands.Cog):

  #The contructor for signing in the client
  def __init__(self,client):
    self.client = client

  #This command is used to clear the last 'n' texts
  @commands.command()
  #@commands.has_permissions(manage_messages = True)
  async def clear(self, ctx, amount=5):
    await ctx.channel.purge(limit=amount)

#Setting up the class as follows
def setup(client):
  client.add_cog(Basic_feat(client))