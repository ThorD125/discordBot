# from dbtest import get_list_from_mariadb
from dotenv import load_dotenv
import os
import discord


load_dotenv()

TOKEN = os.getenv('TOKEN')
if TOKEN is None:
    print("Error: Bot token not found in .env file.")
    exit(1)

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command()
async def ping(ctx, url=None):
    if url is None:
        await ctx.send("pong!")
    else:
        await ctx.send(os.popen(f"ping -c 4 {url} ").read())


@bot.slash_command()
async def traceroute(ctx, url=None):
    if url is None:
        await ctx.send("Enter a URL to trace!")
    else:
        await ctx.send(os.popen(f"traceroute {url} ").read())


@bot.slash_command()
async def dnslookup(ctx, url=None):
    if url is None:
        await ctx.send("Enter a URL to trace!")
    else:
        await ctx.send(os.popen(f"dig {url}").read())


@bot.slash_command()
async def generatepassword(ctx, amount=20):
    await ctx.send(os.popen(f"cat /dev/urandom | tr -dc 'A-Za-z0-9!?><,./\-_=+~:;*&^%$#@()[]' | head -c {amount}").read())


@bot.slash_command()
async def test(ctx):
    username = ctx.author.name

    await ctx.send("hi" + username)


bot.run(TOKEN)

