import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")

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

client.run("ODA2MTMyOTM0OTI2MjcwNDg1.YBk_zA.ikNr2Dskonowx4Yjxcv7cRJy1lo")