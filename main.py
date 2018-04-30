import discord
from discord.ext import commands
from six.moves import configparser
import os

version = '1'
blankvar = ''

def loglog(message):
    print(blankvar.join(('[LOG]', message)))

def debuglog(message):
    print(blankvar.join(('[LOG]', '[DEBUG]', message)))

def errorlog(message):
    print(blankvar.join(('[LOG]', '[ERROR]', message)))

bot = commands.Bot(command_prefix='ifr.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    print('[DEBUG] New Message.')
    if message.author == bot.user:
        debuglog('Message is by me, exiting...')
        return
    if message.attachments != []:
        debuglog('Message has attachments.')

        return
    else:
        debuglog('Message does not have attachments, exiting...')
        return

loglog(blankvar.join(('Starting iFukkie Rapist v.', version, '...')))

filename = "C:\\Users\\jdbue\\Documents\\GitHub\\ifukkie-rapist\\ifr.cfg"
if os.path.isfile(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    token = config.get("config", "token")
else:
    errorlog('Could not find a config file!')
    exit(1)

bot.run(token)
