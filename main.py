from discord.ext import commands
import discord

from apod import random_image

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot Loaded")


@client.command()
async def ping(ctx):
    await ctx.send("Pong")


@client.command()
async def apod(ctx):
    image_filename, page_source = random_image()
    await ctx.send(file=discord.File(image_filename))
    await ctx.send(page_source)


@client.command()
async def quit(ctx):
    await client.close()

token = open("token", "r").read()
print(token)
client.run(token)