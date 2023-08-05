# from dbtest import get_list_from_mariadb
from dotenv import load_dotenv
import os
import discord


load_dotenv()

TOKEN = os.getenv('TOKEN')
if TOKEN is None:
    print("Error: Bot token not found in .env file.")

SERVERID = os.getenv('SERVERID')
if SERVERID is None:
    print("Error: Server ID not found in .env file.")

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command()
async def hello(ctx):
    await ctx.respond("Hello!")

bot.run(TOKEN)
