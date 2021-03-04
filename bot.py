#Not a boat it's a bot. I renamed it for fun

#the code on repl.it : https://repl.it/@Yoplayer1py/Encourage-Bot#main.py


import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is Up")

@client.command()
async def hello(ctx):
    await ctx.send("Hi this is a test")

@client.command()
async def how_are_you(ctx):
    await ctx.send("I am up and running.")

@client.command()
async def soure_code(ctx):
    await ctx.send("")

client.run("token's are private I will be making a video on how to use this repo")
