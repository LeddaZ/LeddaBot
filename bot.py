# LeddaBot
# Converts text into the regional indicator emojis and does other stuff
# Made with Python and pycord (https://github.com/Pycord-Development/pycord)

# Import required libraries
import math
import os
from process_uptime import getuptime
import time
from discord.ext import commands
from dotenv import load_dotenv

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
        if x == 'o':
            response += ':o2: '
        elif x == ' ':
            response += '   '
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

# pls pol command
@bot.event
async def on_message(message):
    if message.content.lower() == 'pls pol':
        global msg
        msg = await message.channel.send('https://imgur.com/U1N67Ai.png')
        await msg.add_reaction("🔨")

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
