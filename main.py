import discord
from discord.ext import commands

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
        print(Image)
        return
    else:
        print('[DEBUG] Message does not have attachments, exiting...')
        return


bot.run('NDM5ODUxNDU0MjAzNjkxMDE5.DcZQxA.bCCmSP2Q6WkJWFAfFZoGFdXyQ7g')
