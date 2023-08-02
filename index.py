import discord
import os
from dotenv import load_dotenv

from dbtest import get_list_from_mariadb
from discord.ext import commands

# Load the environment variables from the .env file
load_dotenv()

# Get the bot token from the environment variable
TOKEN = os.getenv('TOKEN')
if TOKEN is None:
    print("Error: Bot token not found in .env file.")
    exit(1)

# Define the intents that your bot needs
intents = discord.Intents.default()
intents.message_content = True

# Create a new Discord client with the specified intents
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('dbtest'):
        await message.channel.send(get_list_from_mariadb())

client = commands.Bot(command_prefix='\\', intents=intents)


@client.command()
async def ping(ctx):
    """This is a custom command."""
    await ctx.send("pong!")

# Run the bot with the provided token
client.run(TOKEN)
