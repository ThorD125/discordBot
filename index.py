import os
import discord
import subprocess

from util.py.helper import log
from util.py.env import loadEnv


env = loadEnv()

bot = discord.Bot()


@bot.event
async def on_ready():
    log(f"We have logged in as {bot.user}")


def bashCommand(command):
    return subprocess.check_output(command, shell=True, text=True)


@bot.slash_command(description="Pong a URL")
async def ping(ctx, url=None):
    log(f"URL: {url}")
    if url is None:
        await ctx.respond("pong!")
    else:
        await ctx.respond(bashCommand(f"ping -c 4 {url} "))


# @bot.slash_command(description="Trace a URL")
# async def traceroute(ctx, url=None):
#     if url is None:
#         await ctx.respond("Enter a URL to trace!")
#     else:
#         await ctx.respond(bashCommand(f"traceroute {url} "))


# @bot.slash_command(description="DNS lookup")
# async def dnslookup(ctx, url=None):
#     if url is None:
#         await ctx.respond("Enter a URL to trace!")
#     else:
#         await ctx.respond(bashCommand(f"dig {url}"))


# @bot.slash_command(description="Generate a random password")
# async def generatepassword(ctx, amount=20):
#     await ctx.respond(bashCommand(f"cat /dev/urandom | tr -dc 'A-Za-z0-9!?><,./\-_=+~:;*&^%$#@()[]' | head -c {amount}"))


# @bot.slash_command(description="Updating the bot")
# async def update(ctx):
#     await ctx.respond("Updating!")
#     log("Updating!")
#     bashCommand(f"./update.sh")

# @bot.slash_command(description="Restart the bot")
# async def restart(ctx):
#     await ctx.respond("Restarting!")
#     log("Restarting!")
#     bashCommand(f"./util/sh/restart.sh")



    


bot.run(env["TOKEN"])

