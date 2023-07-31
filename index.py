import discord
import os
from dotenv import load_dotenv

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

    if message.content.startswith('pong'):
        await message.channel.send('ping !')

# Run the bot with the provided token
client.run(TOKEN)
