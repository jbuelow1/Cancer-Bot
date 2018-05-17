
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
import re
import ast
import threading

version = '3'
blankvar = ''
workingdir = 'C:/Users/jdbue/Documents/GitHub/ifukkie-rapist/'
headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
}

pingemojis = [
'<:squidwardping:441962933208219658>',
'<:pingwhat:441962933178728448>',
'<:pingturtle:441962933250031662>',
'<:pingthink:441962932784332811>',
'<:PingReee1:441962933099167745>',
'<:ping:441804270698758155>',
'<:hyperpinged:441962933187248148>',
'<:GWnoneAngryPing:441962933199831040>',
'<:FeelsTooPingedMan:441962933199568906>',
'<:FeelsPingedMan:441962932700446721>',
'<:drakeping:441962932247724033>',
'<a:PandaPingRee:441962933115682818>',
'<a:AniPing:441962933413740545>',
'<a:angeryping:441962932662829096>'
]

dancefont = {
'a': '<a:danceA:440893333150105601>',
'b': '<a:danceB:440893333443706890>',
'c': '<a:danceC:440893333301100564>',
'd': '<a:danceD:440893333460746240>',
'e': '<a:danceE:440893333204762625>',
'f': '<a:danceF:440893333502427136>',
'g': '<a:danceG:440893333439643679>',
'h': '<a:danceH:440893333355888668>',
'i': '<a:danceI:440893333586575380>',
'j': '<a:danceJ:440893333351694346>',
'k': '<a:danceK:440893333578186752>',
'l': '<a:danceL:440893333544501258>',
'm': '<a:danceM:440893333317877760>',
'n': '<a:danceN:440893333276065813>',
'o': '<a:danceO:440893333435318272>',
'p': '<a:danceP:440893333624324113>',
'q': '<a:danceQ:440893333288517652>',
'r': '<a:danceR:440893333594832896>',
's': '<a:danceS:440893333636775946>',
't': '<a:danceT:440893333523398667>',
'u': '<a:danceU:440893333569667073>',
'v': '<a:danceV:440893333422997506>',
'w': '<a:danceW:440893333473198082>',
'x': '<a:danceX:440893333737439232>',
'y': '<a:danceY:440893333737308180>',
'z': '<a:danceZ:440893333917925386>',
'0': '0',
'1': '1',
'2': '2',
'3': '3',
'4': '4',
'5': '5',
'6': '6',
'7': '7',
'8': '8',
'9': '9'
}

debug = True

bot = discord.Client()

global ifunny
global heck
global ping
global kys
global hewwo
global xd

ifunny = False
heck = False
ping = False
kys = False
hewwo = False
xd = False

def loglog(message):
    print(blankvar.join(('[LOG] [ ] [ ] ', message)))

def debuglog(message):
    if debug:
        print(blankvar.join(('[LOG] [D] [ ] ', message)))

def errorlog(message):
    print(blankvar.join(('[LOG] [ ] [E] ', message)))

def image_check(suspect,template):
    img_rgb = cv.imread(suspect)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread(template,0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    if str(loc) != ("(array([], dtype=int64), array([], dtype=int64))" or "(array([], dtype=int32), array([], dtype=int32))"):
        return True
    else:
        return False

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def processImage(infile):
    try:
        im = Image.open(infile)
    except IOError:
        print("Cant load", infile)
        sys.exit(1)
    i = 0
    mypalette = im.getpalette()
    try:
        while 1:
            im.putpalette(mypalette)
            new_im = Image.new("RGBA", im.size)
            new_im.paste(im)
            new_im.save('foo'+str(i)+'.png')
            i += 1
            im.seek(im.tell() + 1)
    except EOFError:
        pass # end of sequence

def chHeck(message):
    debuglog('Checking for trigger words...')
    debuglog('checing for "heck"...')
    if (('heck' in message.content.lower()) or ('hek' in message.content.lower())):
        debuglog(blankvar.join((str(message.author), ' just said h*ck!')))
        bot.send_file(message.channel, blankvar.join(('heck',str(random.randint(1,6)),'.jpg')))
        global heck
        heck = True
    else:
        global heck
        heck = False

def chPing(message):
    debuglog('checking for "@everyone"...')
    if '@everyone' in message.content:
        debuglog(blankvar.join((str(message.author), ' pinged! REEEE!!!')))
        bot.send_message(message.channel, random.choice(pingemojis))
        global ping
        ping = True
    else:
        global ping
        ping = False

def chKys(message):
    debuglog('checking for "die", "kys" and "kms"...')
    if (findWholeWord('die')(message.content.lower()) or findWholeWord('kys')(message.content.lower()) or findWholeWord('kms')(message.content.lower())):
        debuglog(blankvar.join((str(message.author), ' wants to die. helping...')))
        bot.send_file(message.channel, 'bleach.png', content=''.join((dancefont['k'],dancefont['y'],dancefont['s'])))
        global kys
        kys = True
    else:
        global kys
        kys = False

def chHewwo(message):
    debuglog('checking for my mentions...')
    if (blankvar.join(('<@', bot.user.id, '>')) in message.content) or (blankvar.join(('<!@', bot.user.id, '>')) in message.content):
        debuglog(blankvar.join((str(message.author),' said hi!')))
        bot.send_message(message.channel, 'H- Hewwo?!')
        global hewwo
        hewwo = True
    else:
        global hewwo
        hewwo = False

def chXd(message):
    debuglog('looking for XD...')
    if findWholeWord('xd')(message.content.lower()):
        debuglog(blankvar.join((str(message.author),' just XD\'d')))
        bot.send_message(message.channel, '<a:xd:442034831690301461>')
        global xd
        xd = True
    else:
        global xd
        xd = False

def chIfunny(message):
    if message.attachments != []:
        debuglog('Message has attachments. Scanning for cancer...')
        url = ast.literal_eval(str(message.attachments).split("[")[1].split("]")[0])
        r = requests.get(url['url'], stream=True)
        if r.status_code == 200:
            with open(blankvar.join(('tmp/', url['filename'])), 'wb') as f:
                for chunk in r:
                    f.write(chunk)

        ifukkie = image_check(blankvar.join(('tmp/', url['filename'])), 'ifukkie.png')
        if ifukkie or ('ifunny.co/' in message.content):
            bot.delete_message(message)
            bot.send_message(message.channel, blankvar.join(('<:shooter:441972276901052416> ',dancefont['d'],dancefont['e'],dancefont['l'],dancefont['e'],dancefont['t'],' ',dancefont['d'],dancefont['i'],dancefont['s'],' <:shooter:441972276901052416>')))
            global ifunny
            ifunny = True
            loglog('Message was cancerous and was deleted.')
        else:
            debuglog('False Alarm. Message was fine.')
        os.remove(blankvar.join(('tmp/', url['filename'])))
        global ifunny
        ifunny = False



#END OF FUNCTIONS
#DEFINES:
loglog(blankvar.join(('Starting iFukkie Rapist v', version, '...')))


#ASYNCROUS EVENTS:
@bot.event
async def on_ready():
    loglog('Connected to Discord!')
    loglog(blankvar.join(('(User: "', str(bot.user), '", User ID: "', str(bot.user.id), '")')))
    await bot.change_status(game=discord.Game(name='with little children'))

@bot.event
async def on_message(message):
    debuglog(blankvar.join(('New Message by ', str(message.author), ' with ID ', str(message.id), ' in channel ', str(message.channel.id), '.')))
    if message.author == bot.user:
        debuglog('Message is by me, exiting...')
        return
    else:
        tChIfunny = threading.Thread(target=chIfunny, args=(message,))
        tChHeck = threading.Thread(target=chHeck, args=(message,))
        tChPing = threading.Thread(target=chPing, args=(message,))
        tChKys = threading.Thread(target=chKys, args=(message,))
        tChHewwo = threading.Thread(target=chHewwo, args=(message,))
        tChXd = threading.Thread(target=chXd, args=(message,))

        tChIfunny.start()
        tChHeck.start()
        tChPing.start()
        tChKys.start()
        tChHewwo.start()
        tChXd.start()

        tChIfunny.join()
        tChHeck.join()
        tChPing.join()
        tChKys.join()
        tChHewwo.join()
        tChXd.join()


        if ifunny:
            bot.delete_message(message)
            bot.send_message(message.channel, blankvar.join(('<:shooter:441972276901052416> ',dancefont['d'],dancefont['e'],dancefont['l'],dancefont['e'],dancefont['t'],' ',dancefont['d'],dancefont['i'],dancefont['s'],' <:shooter:441972276901052416>')))

        if heck:
            bot.send_file(message.channel, blankvar.join(('heck',str(random.randint(1,6)),'.jpg')))

        if ping:
            bot.send_message(message.channel, random.choice(pingemojis))

        if kys:
            bot.send_file(message.channel, 'bleach.png', content=''.join((dancefont['k'],dancefont['y'],dancefont['s'])))

        if hewwo:
            bot.send_message(message.channel, 'H- Hewwo?!')

        if xd:
            bot.send_message(message.channel, '<a:xd:442034831690301461>')


        debuglog(blankvar.join(('Message #', message.id, ' has finished processing.')))


@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        debuglog('Someone deleted my post! REEEEEEEE Spamming...')
        await bot.send_message(message.channel, message.content)
        await bot.send_message(message.channel, message.content)
        await bot.send_message(message.channel, message.content)

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
