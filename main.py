
import discord
from six.moves import configparser
import os
from time import sleep
import cv2 as cv
import numpy as np
import json
import urllib.request
import requests
import shutil

version = '1'
blankvar = ''
workingdir = 'C:/Users/jdbue/Documents/GitHub/ifukkie-rapist/'
headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
}

def loglog(message):
    print(blankvar.join(('[LOG] [ ] [ ] ', message)))

def debuglog(message):
    print(blankvar.join(('[LOG] [D] [ ] ', message)))

def errorlog(message):
    print(blankvar.join(('[LOG] [ ] [E] ', message)))

def ifukkie_check(suspect):
    img_rgb = cv.imread(suspect)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread('sample.jpg',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.4
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
        debuglog('Message has attachments. Scanning for cancer...')
        attach = str(message.attachments)
        url = attach.split("'")
        path = url[5].split("/")

        r = requests.get(url[5], stream=True)
        if r.status_code == 200:
            with open(path[6], 'wb') as f:
                for chunk in r:
                    f.write(chunk)

        cancerous = ifukkie_check(path[6])
        if cancerous:
            await bot.delete_message(message)
            await bot.send_message(message.channel, '<:nope:432913100144902146>')
            loglog('Message was cancerous and was deleted.')
        else:
            debuglog('False Alarm. Message was fine.')
        os.remove(path[6])
        return
    else:
        debuglog('Message does not have attachments, exiting...')
        return

loglog('Attempting to login to Discord...')

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
