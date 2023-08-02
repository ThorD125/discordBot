import discord
from discord.ext import commands
from discord_slash import SlashCommand

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
    command_prefix=commands.when_mentioned_or('\\'), intents=intents)
slash = SlashCommand(bot, sync_commands=True)


@slash.slash(name="ping", description="Responds with pong!")
async def ping(ctx):
    await ctx.send("pong!")

client.run(TOKEN)
