
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
import random

version = '1'
blankvar = ''
workingdir = 'C:/Users/jdbue/Documents/GitHub/ifukkie-rapist/'
headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
}

silent = False
debug = True

def loglog(message):
    print(blankvar.join(('[LOG] [ ] [ ] ', message)))

def debuglog(message):
    if debug:
        print(blankvar.join(('[LOG] [D] [ ] ', message)))

def errorlog(message):
    print(blankvar.join(('[LOG] [ ] [E] ', message)))

def ifukkie_check(suspect):
    img_rgb = cv.imread(suspect)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread('ifukkie.png',0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    if str(loc) != "(array([], dtype=int32), array([], dtype=int32))":
        return True
    else:
        return False

loglog(blankvar.join(('Starting iFukkie Rapist v', version, '...')))

bot = discord.Client()

@bot.event
async def on_ready():
    loglog('Connected to Discord!')
    loglog(blankvar.join(('(User: "', str(bot.user), '", User ID: "', str(bot.user.id), '")')))
    await bot.change_status(game=discord.Game(name='with my cock in ifunny\'s ass'))

@bot.event
async def on_message(message):
    debuglog(blankvar.join(('New Message by ', str(message.author), ' with ID ', str(message.id), ' in channel ', str(message.channel.id), '.')))
    if message.author == bot.user:
        debuglog('Message is by me, exiting...')
        return

    if (('heck' in message.content) or ('Heck' in message.content) or ('HECK' in message.content) or ('hek' in message.content) or ('Hek' in message.content) or ('HEK' in message.content)):
        debuglog(blankvar.join((str(message.author), ' just said h*ck!')))
        await bot.send_file(message.channel, blankvar.join(('heck',str(random.randint(1,4)),'.jpg')))

    if '@everyone' in message.content:
        debuglog(blankvar.join((str(message.author), ' pinged! REEEE!!!')))
        await bot.send_file(message.channel, 'ping.png')

    if message.attachments != []:
        debuglog('Message has attachments. Scanning for cancer...')
        attach = str(message.attachments)
        url = attach.split("'")
        path = url[5].split("/")

        print(str(url))
        print(url[6])
        r = requests.get(, stream=True)
        if r.status_code == 200:
            with open(path[6], 'wb') as f:
                for chunk in r:
                    f.write(chunk)

        ifukkie = ifukkie_check(path[6])
        #ilolifukker =ilolifukker_checker(path[6])
        #memecuck = memecuck_check(path[6])
        #instashit = instashit_check(path[6])
        cancerous = ifukkie
        if cancerous:
            await bot.delete_message(message)
            await bot.send_message(message.channel, '<:nope:432913100144902146> <a:danceD:440893333460746240><a:danceE:440893333204762625><a:danceL:440893333544501258><a:danceE:440893333204762625><a:danceT:440893333523398667> <a:danceD:440893333460746240><a:danceI:440893333586575380><a:danceS:440893333636775946> <:nope:432913100144902146>')
            loglog('Message was cancerous and was deleted.')
        else:
            debuglog('False Alarm. Message was fine.')
        os.remove(path[6])
        return
    else:
        debuglog('Message does not have attachments.')
        if 'ifunny.co/' in message.content:
            await bot.delete_message(message)
            await bot.send_message(message.channel, '<:nope:432913100144902146> <a:danceD:440893333460746240><a:danceE:440893333204762625><a:danceL:440893333544501258><a:danceE:440893333204762625><a:danceT:440893333523398667> <a:danceD:440893333460746240><a:danceI:440893333586575380><a:danceS:440893333636775946> <:nope:432913100144902146>')
            loglog('Message was cancerous and was deleted.')
        return

loglog('Attempting to login to Discord...')

filename = "ifr.cfg"
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
