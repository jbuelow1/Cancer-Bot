import discord
from discord.ext import commands

import os, sys, traceback
from six.moves import configparser
import datetime

"""This is a multi file example showcasing many features of the command extension and the use of cogs.
These are examples only and are not intended to be used as a fully functioning bot. Rather they should give you a basic
understanding and platform for creating your own bot.
These examples make use of Python 3.6.2 and the rewrite version on the lib.
For examples on cogs for the async version:
https://gist.github.com/leovoel/46cd89ed6a8f41fd09c5
Rewrite Documentation:
http://discordpy.readthedocs.io/en/rewrite/api.html
Rewrite Commands Documentation:
http://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html
Familiarising yourself with the documentation will greatly help you in creating your bot and using cogs.
"""


def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['?/', '?/ ']

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = [
'cogs.manager',
'cogs.owner',
'cogs.status',
'cogs.trigger',
'cogs.basic',
'cogs.stats',
'cogs.images',
'cogs.help',
'cogs.copypasta'
]

bot = commands.Bot(command_prefix=get_prefix, description='A Very Cancerous Discord Bot')

bot.scommands = 0
bot.ucommands = 0
bot.striggers = 0
bot.utriggers = 0

bot.startdate = datetime.datetime.now()

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    print('Loading extensions...')
    print('Searching for extensions...')
    for extension in initial_extensions:
        print('Found extension: ' + extension)
    for extension in initial_extensions:
        try:
            print('Loading extension \'' + extension + '\'...')
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension \'' + extension + '\'\nError: ' + str(e))
            traceback.print_exc()

@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print('logged in')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    await bot.change_presence(game=discord.Game(name='Status loop not running'))
    print('Successfully logged in and booted...!')

filename = "ifr.cfg"
if os.path.isfile(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    token = config.get("config", "token")
else:
    print('ERR_EXIT_CODE = "1"')
    exit(1)

bot.run(token, bot=True, reconnect=True)
