import os
import discord
from dotenv import load_dotenv

from steam_game_check import *

load_dotenv()

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(description="list all commands")
async def help(ctx):
    print("help")
    await ctx.respond("""# commands
- /help
- /steam id1 id2 id3
""")


# @bot.slash_command(description="check steam games for steamids")
# async def steam(ctx, steam_ids_txt:str):
#     print("steam")
#     apikey = os.getenv("APIKEY")
#     steam_ids_split = steam_ids_txt.split()
#     # games = await testGamesAll(apikey, steam_ids_split)
    
#     try:
#         games = await testGamesAll(apikey, steam_ids_split)
#     except Exception as e:
#         await ctx.respond(f"Error fetching games: {str(e)}")
#         return
#     # games = await testGamesAll(apikey, ["76561198259056804", "76561199030951176"])
#     # game_text = "```"
#     # for x in games:
#     #     game_text += x + "\n"
#     # game_text += "```"
#     # await ctx.respond(game_text)

#     game_text = "You bitches all have:\n```"
#     current_message = game_text
#     for game in games:
#         line = game + "\n"
#         # Check if adding this line exceeds the limit
#         if len(current_message) + len(line) + 3 > 2000:  # +3 for the closing ```
#             current_message += "```"
#             await ctx.send(current_message)
#             current_message = game_text + line
#         else:
#             current_message += line
    
#     # Send any remaining message
#     if current_message != game_text:
#         current_message += "```"
#         await ctx.send(current_message)
#         return
    
@bot.slash_command(description="check steam games for steamids")
async def steam(ctx, steam_ids_txt: str):
    print("steam command invoked")
    apikey = os.getenv("STEAM_APIKEY")
    if not apikey:
        # await ctx.respond("API Key is missing. Please set the APIKEY environment variable.")
        return
    await ctx.respond("You bitches all have:")

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
        # Check if adding this line exceeds the limit
        if len(current_message) + len(line) + 3 > 2000:  # +3 for the closing ```
            current_message += "```"
            await ctx.send(current_message)
            current_message = game_text + line
        else:
            current_message += line
    
    # Send any remaining message
    if current_message != game_text:
        current_message += "```"
        await ctx.send(current_message)







the_token = os.getenv("DISCORD_BOT_TOKEN")

bot.run(the_token)
