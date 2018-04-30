import discord
from six.moves import configparser
import os
from time import sleep
import cv2 as cv
import numpy as np

version = '1'
blankvar = ''

def loglog(message):
    print(blankvar.join(('[LOG] [ ] [ ] ', message)))

def debuglog(message):
    print(blankvar.join(('[LOG] [D] [ ] ', message)))

def errorlog(message):
    print(blankvar.join(('[LOG] [ ] [E] ', message)))

def ifukkie_check():
    img_rgb = cv.imread('test.jpg')
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread('sample.jpg',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    if str(loc) != "(array([], dtype=int32), array([], dtype=int32))":
        return True
    else:
        return False

print("")
loglog(blankvar.join(('Starting iFukkie Rapist v', version, '...')))

bot = discord.Client()

@bot.event
async def on_ready():
    loglog('Connected to Discord!')
    loglog(blankvar.join(('(User: "', str(bot.user), '", User ID: "', str(bot.user.id), '")')))
    print("")

@bot.event
async def on_message(message):
    debuglog(blankvar.join(('New Message by ', str(message.author), ' with ID ', str(message.id), ' in channel ', str(message.channel.id), '.')))
    if message.author == bot.user:
        debuglog('Message is by me, exiting...')
        return
    if message.attachments != []:
        debuglog('Message has attachments.')
        if (int(message.author.id) == 95274427171733504) and (int(message.channel.id) == 426605575669940234):
            loglog('Message is from a cunt. Delet dis! ( ͠° ͟ʖ ͠°)')
            sleep(2)
            await bot.delete_message(message)
            await bot.send_message(message.channel, '<:nope:432913100144902146>')
            loglog(blankvar.join(('Message was deleted with id ', message.id, ' from channel ', message.channel.id)))
        return
    else:
        debuglog('Message does not have attachments, exiting...')
        return

loglog('Attempting to login to discord...')

filename = "C:\\Users\\jdbue\\Documents\\GitHub\\ifukkie-rapist\\ifr.cfg"
if os.path.isfile(filename):
    debuglog(blankvar.join(('Found config file: "', filename, '".')))
    config = configparser.ConfigParser()
    config.read(filename)
    debuglog('Checking for "token" variable...')
    token = config.get("config", "token")
else:
    errorlog('Could not find a config file!')
    print('ERR_EXIT_CODE = "1"')
    exit(1)

loglog('Logging in...')

bot.run(token)
