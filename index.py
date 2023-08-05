import os
import discord

from util.py.helper import log
from util.py.env import loadEnv


env = loadEnv()

bot = discord.Bot()


@bot.event
async def on_ready():
    log(f"We have logged in as {bot.user}")


@bot.slash_command(description="Pong a URL")
async def ping(ctx, url=None):
    if url is None:
        await ctx.respond("pong!")
    else:
        await ctx.respond(os.popen(f"ping -c 4 {url} ").read())


@bot.slash_command( description="Trace a URL")
async def traceroute(ctx, url=None):
    if url is None:
        await ctx.respond("Enter a URL to trace!")
    else:
        await ctx.respond(os.popen(f"traceroute {url} ").read())


@bot.slash_command(description="DNS lookup")
async def dnslookup(ctx, url=None):
    if url is None:
        await ctx.respond("Enter a URL to trace!")
    else:
        await ctx.respond(os.popen(f"dig {url}").read())


@bot.slash_command(description="Generate a random password")
async def generatepassword(ctx, amount=20):
    await ctx.respond(os.popen(f"cat /dev/urandom | tr -dc 'A-Za-z0-9!?><,./\-_=+~:;*&^%$#@()[]' | head -c {amount}").read())


@bot.slash_command(description="Updating the bot", guild_ids=[env["SERVERID"]])
async def update(ctx):
    await ctx.respond("Updating!")
    log("Updating!")
    os.popen(f"./update.sh").read()

@bot.slash_command(description="Restart the bot", guild_ids=[env["SERVERID"]])
async def restart(ctx):
    await ctx.respond("Restarting!")
    log("Restarting!")
    os.popen(f"./util/sh/restart.sh").read()



    


bot.run(env["TOKEN"])

