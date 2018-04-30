import discord
from discord.ext import commands
import ConfigParser

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
        print('[DEBUG] Message is by me, exiting...')
        return
    if message.attachments != []:
        print('[DEBUG] Message has attachments.')

        return
    else:
        print('[DEBUG] Message does not have attachments, exiting...')
        return

config = ConfigParser.ConfigParser()
config.read("config.cfg")
token = config.get("basic", "token")

bot.run(token)
