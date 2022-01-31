# LeddaBot
# Converts text into the regional indicator emojis and does other stuff
# Made with Python and pycord (https://github.com/Pycord-Development/pycord)

# Import required libraries
import discord
import os
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
        # Add red emoji for A and B
        if x == 'a' or x == 'b' :
            response += ':' + x.lower() + ': '
        elif x == ' ':
            response += '   '
        else:
            response += ':regional_indicator_' + x.lower() + ': '
    await ctx.send(response)

# pls pol command
@bot.event
async def on_message(message):
    if message.content == 'pls pol':
        await message.channel.send('https://i.imgur.com/HEXHJnV.png')

# Run the bot
bot.run(TOKEN)
