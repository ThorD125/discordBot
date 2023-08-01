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

    if message.content.startswith('ping'):
        await message.channel.send('pong !')

    if message.content.startswith('dbtest'):
        await message.channel.send(get_list_from_mariadb())

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_member_update(before, after):
    # Check if the username has changed
    if before.name != after.name:
        # Add your desired prefix here
        prefix = "PREFIX_"
        new_username = prefix + after.name

        try:
            # Attempt to update the username
            await after.edit(nick=new_username)
        except discord.Forbidden:
            print(f"Unable to change the username of {after.name} due to missing permissions.")
        except discord.HTTPException:
            print(f"An error occurred while changing the username of {after.name}.")


# Run the bot with the provided token
client.run(TOKEN)
