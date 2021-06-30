import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
from replit import db

class Server_feat(commands.Cog):

  #constructor
  def __init__(self,client):
    self.client = client

  #This is basically an error handler
  @commands.Cog.listener()
  async def on_message_error(ctx, error):
    if isinstance(error, commands.MissingRequieredArgument):
      await ctx.send("Please enter all the arguments")
    elif isinstance(error, commands.MissingPermissions):
      await ctx.send("You do not have the Permission!")
    else:
      await ctx.send("Invalid Command")

  #Command to ban a member
  @commands.command()
  #@commands.has_permissions(manage_messages = True)
  async def ban(self, ctx, member = discord.Member,  *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'Banned {member.mention}')

  #Command to kick a member from the server
  @commands.command()
  #@commands.has_permissions(manage_messages = True)
  async def kick(self, ctx, member = discord.Member, * ,reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'Kicked {member.mention}')

  #Command to unban a particular member
  @commands.command()
  #@commands.has_permissions(manage_messages = True)
  async def unban(self, ctx, member):
    banned_users = await ctx.guild.bans()
    mem_name, mem_hash = member.split('#')

    for user in banned_users:
      if (mem_name, mem_hash) == (user.name, user.discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.mention}')
        return

def setup(client):
  client.add_cog(Server_feat(client))