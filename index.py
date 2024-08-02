import os
import discord

from dotenv import load_dotenv

from steam_game_check import *
from utils import *
from warframe_utils import *

load_dotenv()

intents = discord.Intents.default()

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(description="list all commands")
async def help(ctx):
    print("help")
    await ctx.respond("""# commands
- /help
- /steam "id1 name1 id2 name2 id3 name3 ..."
- /wf

to be included:
- /generatepassword

""")

@bot.slash_command(description="Get a wf status")
async def wf(ctx):
    await ctx.defer()
    await ctx.respond(getWf())

@bot.slash_command(description="Generate a random password")
async def generatepassword(ctx, amount=20):
    await ctx.defer()
    await ctx.respond(randomPass(amount))
    
@bot.slash_command(description="check steam games for steamids")
async def steam(ctx, steam_ids_txt: str):
    await ctx.defer()
    print("steam command invoked")
    apikey = os.getenv("STEAM_APIKEY")
    if not apikey:
        return

    steam_ids_split = steam_ids_txt.split()
    if not steam_ids_split:
        await ctx.respond("Please provide valid Steam IDs.")
        return

    try:
        games = await testGamesAll(apikey, steam_ids_split)
    except Exception as e:
        await ctx.respond(f"Error fetching games: {str(e)}")
        return

    game_text = "```"
    current_message = game_text
    for game in games:
        line = game + "\n"
        if len(current_message) + len(line) + 3 > 2000:
            current_message += "```"
            await ctx.send(current_message)
            current_message = game_text + line
        else:
            current_message += line
    
    if current_message != game_text:
        current_message += "```"
        await ctx.send(current_message)

    await ctx.respond("You bitches all have:")

the_token = os.getenv("DISCORD_BOT_TOKEN")

bot.run(the_token)
