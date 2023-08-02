import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

from dbtest import get_list_from_mariadb

load_dotenv()

TOKEN = os.getenv('TOKEN')
if TOKEN is None:
    print("Error: Bot token not found in .env file.")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # if message.content.startswith('dbtest'):
    #     await message.channel.send(get_list_from_mariadb())

client = commands.Bot(
    command_prefix=commands.when_mentioned_or('!'), intents=intents)


@client.command()
async def ping(ctx, url=None):
    if url is None:
        await ctx.send("pong!")
    else:
        await ctx.send(os.popen(f"ping -c 4 {url} ").read())


@client.command()
async def traceroute(ctx, url=None):
    if url is None:
        await ctx.send("Enter a URL to trace!")
    else:
        await ctx.send(os.popen(f"traceroute {url} ").read())


@client.command()
async def dnslookup(ctx, url=None):
    if url is None:
        await ctx.send("Enter a URL to trace!")
    else:
        await ctx.send(os.popen(f"dig {url}").read())


@client.command()
async def generatepassword(ctx, amount=20):
    await ctx.send(os.popen(f"cat /dev/urandom | tr -dc 'A-Za-z0-9!?><,./\-_=+~:;*&^%$#@' | head -c {amount})").read())


client.run(TOKEN)
