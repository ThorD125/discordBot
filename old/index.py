import os
import discord
import subprocess
from util.py.helper import log, bashCommand
from util.py.env import loadEnv
from util.py.commands import CMDping, CMDtraceroute, CMDdig, CMDranGenPassword, downisit, GETCAT, GETtetrio, GETwf
from util.py.setup import updateSET, restartSET
from util.py.steamgamechecker import steam_logic

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
        await ctx.defer()
        await ctx.respond(CMDping(url))


@bot.slash_command(description="Trace a URL")
async def traceroute(ctx, url=None, amount=15):
    if url is None:
        await ctx.respond("Enter a URL to trace!")
    else:
        await ctx.defer()
        await ctx.respond(CMDtraceroute(url, amount))


@bot.slash_command(description="DNS lookup")
async def dnslookup(ctx, url=None):
    url.replace(" ", "")
    if url is None:
        await ctx.respond("Enter a URL to trace!")
    else:
        await ctx.defer()
        await ctx.respond(CMDdig(url))


@bot.slash_command(description="Generate a random password")
async def generatepassword(ctx, amount=20):
    await ctx.defer()
    await ctx.respond(CMDranGenPassword(amount))


@bot.slash_command(description="Updating the bot")
async def update(ctx):
    await ctx.respond("Updating!")
    log("Updating!")
    updateSET()


@bot.slash_command(description="Restart the bot")
async def restart(ctx):
    await ctx.respond("Restarting!")
    log("Restarting!")
    restartSET()


@bot.slash_command(description="list some nice links")
async def links(ctx):
    await ctx.respond("""# links
- https://www.thor-demeestere.be
- https://github.com/ThorD125""")


@bot.slash_command(description="list all commands")
async def help(ctx):
    await ctx.respond("""# commands
- /ping
- /traceroute
- /dnslookup
- /generatepassword
- /update
- /restart
- /links
- /steamsamegames
""")


@bot.slash_command(description="Is it down for everyone or just me?")
async def isitdown(ctx, url=None):
    if url is None:
        await ctx.respond("Enter a URL to trace!")
    else:
        await ctx.defer()
        await ctx.respond(downisit(url))


@bot.slash_command(description="Get a random cat")
async def cat(ctx):
    await ctx.defer()
    await ctx.respond(GETCAT())


@bot.slash_command(description="Get a tetrio user's stats")
async def tetrio(ctx, user=None):
    if user is None:
        user = ctx.author.name
    await ctx.defer()
    await ctx.respond(GETtetrio(user))


@bot.slash_command(description="Get a wf status")
async def wf(ctx):
    await ctx.defer()
    await ctx.respond(GETwf())


@bot.slash_command(description="Get a list of games names that you and your friends have in common")
async def steamsamegames(ctx, args):
    await ctx.defer()
    await ctx.respond(steam_logic(args.split(" ")))

bot.run(env["TOKEN"])
