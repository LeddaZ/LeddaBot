# LeddaBot
# Converts text into the regional indicator emojis and does other stuff
# Made with Python and pycord (https://github.com/Pycord-Development/pycord)

# Import required libraries
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
        global msg
        msg = await message.channel.send('https://imgur.com/U1N67Ai.png')
        await msg.add_reaction("🔨")

# Bonk/unbonk Pol on reaction
@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message == msg and user != bot.user:
        await msg.edit('https://i.imgur.com/HEXHJnV.png')

@bot.event
async def on_raw_reaction_remove(reaction):
    await msg.edit('https://imgur.com/U1N67Ai.png')

# Run the bot
bot.run(TOKEN)
