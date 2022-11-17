# LeddaBot
# Converts text into the regional indicator emojis and does other stuff
# Made with Python and pycord (https://github.com/Pycord-Development/pycord)

# Import required libraries
from discord.ext import commands
from dotenv import load_dotenv
from process_uptime import getuptime
import git
import math
import os
import psutil
import random
import time

# Read bot token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set command prefix
bot = commands.Bot(command_prefix='!')

# !emoji command
# Reads every character from the string (argument) and adds the
# corresponding emoji to a string
@bot.command(name='emoji', help='Converts text into the regional indicator emojis')
async def emojiConverter(ctx, arg):
    response = ''
    for x in arg:
        # Add red emoji for A, B and O
        if x == 'a' or x == 'b':
            response += ':' + x.lower() + ': '
        elif x == 'o':
            response += ':o2: '
        elif x == ' ':
            response += '   '
        elif not x.isalpha():
            response += x
        else:
            response += ':regional_indicator_' + x.lower() + ': '
    await ctx.send(response)

# !hog command
# Sends an hog rider gif
# HOOOOG RIIIIIDEEEEEEEEEEEEEER
@bot.command(name='hog', help='Sends an hog rider gif')
async def hogRider(ctx):
    await ctx.send('https://tenor.com/view/clash-of-clans-hog-rider-call-gif-4169590')

# !uptime command
# Shows bot uptime
@bot.command(name='uptime', help='Shows bot uptime')
async def showUptime(ctx):
    uptime = getuptime()
    hr = math.floor(uptime/(60*60))
    min = math.floor(uptime % (60*60) / 60)
    sec = math.floor(uptime % 60)
    # Adds zero to min and sec if necessary
    if (min < 10):
        min = "0" + str(min)
    if (sec < 10):
        sec = "0" + str(sec)
    response = str(hr) + ":" + str(min) + ":" + str(sec) + " (h:mm:ss)"
    await ctx.send(response)

# !rand command
# Returns a random integer between two values
@bot.command(name='rand', help='Returns a random integer between two values')
async def randNum(ctx, min, max):
    try:
        msg = random.randint(int(min), int(max))
        pass
    except ValueError:
        msg = "Error: one or both arguments are not integers."
        pass

    await ctx.send(msg)

# !yn command
# Returns yes or no
@bot.command(name='yn', help='Returns yes or no')
async def yesNo(ctx):
    n = random.randint(0, 1)
    if (n == 0):
        msg = "No"
    else:
        msg = "Yes"

    await ctx.send(msg)

# !info command
# Shows bot info
@bot.command(name='info', help='Shows bot info')
async def botInfo(ctx):
    # Memory usage
    process = psutil.Process()
    mem = str(round(process.memory_info().vms/1024/1024, 2))

    # Commit hash
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha

    await ctx.send("**LeddaBot**\nCommit `" + sha[0:8] + "`\nMemory usage: " + mem + " MB\nSource: https://github.com/LeddaZ/LeddaBot")

# Error handler for the !rand command
@randNum.error
async def randNum_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("Error: missing maximum number.")

# Commands that detect text
@bot.event
async def on_message(message):
    
    # pls pol
    if message.content.lower() == 'pls pol':
        global msg
        msg = await message.channel.send('https://imgur.com/U1N67Ai.png')
        await msg.add_reaction("🔨")
        
    # Mudae claim detector
    if "are now married!" in message.content:
        msg = ":champagne: Viva gli sposi! :champagne:"
        await message.channel.send(msg, reference=message)

    # You should keep yourself safe... NOW!
    if "kys" in message.content.lower():
        msg = 'https://i.kym-cdn.com/photos/images/original/002/229/998/1f4'
        await message.channel.send(msg, reference=message)

    # stocazzo
    if "stocazzo" in message.content.lower():
        msg = 'OOOOOOOOOOOOOOOOOOOOOOOOO'
        await message.channel.send(msg, reference=message)

    # Prevents commands from being blocked
    await bot.process_commands(message)

# Bonk/unbonk Pol on reaction
@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message == msg and user != bot.user:
        await msg.edit(content='https://i.imgur.com/SU0FVDH.png')
        time.sleep(0.4)
        await msg.edit(content='https://i.imgur.com/HEXHJnV.png')

@bot.event
async def on_raw_reaction_remove(reaction):
    await msg.edit(content='https://imgur.com/U1N67Ai.png')

# Run the bot
bot.run(TOKEN)
