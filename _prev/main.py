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
import time
from io import StringIO
import shlex
from subprocess import Popen, PIPE, STDOUT
import math
import asyncio
import datetime
from dateutil.relativedelta import relativedelta
from pathlib import Path
import pickle
import importlib

#modules
import Mparser
import modules.images

version = '9'
if str(Path(".").resolve()).split('/')[-1] == 'testing':
    version = version + ' [BETA]'
blankvar = ''
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
}

hecks = [
'https://i.imgur.com/ynS00JL.jpg',
'https://i.imgur.com/YaFUVwE.jpg',
'https://i.imgur.com/S6sqpoq.png',
'https://i.imgur.com/zTxzouf.jpg',
'https://i.imgur.com/z4u0Juo.png',
'https://i.imgur.com/z4u0Juo.png',
'https://i.imgur.com/vcTg4tO.jpg',
]

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

stati = [
'with little children', #CBP
'with ur mum XD', #CBP
'( ͡° ͜ʖ ͡°)',
'with big, big balls', #CBP
'FORTNITE XD XD',
'yeeting babies', #CBP
'deepfrying the memes',
'bepis simulator',
'with myself', #CBP
'with my peepee', #CBP
'with mommy\'s peepee', #CBP
'midget basketball', #CBP
'with my rocket', #CBP
'with the anthros', #CBP
'peek a boo ( ͡° ͜ʖ ͡°)', #CBP
'on e621', #CBP
'lewding lolis', #CBP
'dead',
'alone',
'Discord',
'with high voltage',
'on a shitty server', #CBP
'in the street', #CBP
'with lives of the innocent', #CBP
'rm -rf /',
'with 14 werewolves', #CBP
'in a back alley' #CBP
]

helpStati = [
'type ?/help',
'try ?/help',
'use ?/help',
'say ?/help',
'?/help'
]

debug = True

bot = discord.Client()
parser = Mparser.parser(bot)

emBleach = discord.Embed(title=''.join((dancefont['k'],dancefont['y'],dancefont['s'])), color=0x00ff00) #CBP
emBleach.set_image(url="https://i.imgur.com/Mto46BE.png")

emHeck = discord.Embed(title='No Swearing!', color=0x00ff00)

emThink = discord.Embed(title=':thinking::thinking::thinking::thinking::thinking:', color=0x00ff00)
emThink.set_image(url="https://i.imgur.com/wHMWq1B.gif")

emHelp0 = discord.Embed(description='I am under constant development, expect many changes! You can help by sumbitting any suggestions to my senpai by using my suggestion command. (`?/suggest <suggestion>`)\n\nThis bot\'s command prefix is: `?/`\n\n`<argument>` is a required argument\n`[argument]` is an optional argument\n`{image}` is an optional image argument that is attached\n\u200b', color=0x00ff00)
emHelp0.set_thumbnail(url='https://i.imgur.com/fnt3A4l.png')
emHelp0.set_author(name='Cancer Bot Help', icon_url='https://i.imgur.com/4fehjDz.png')
emHelp0.add_field(name='?/help', value='Displays this help text', inline=True)
emHelp0.add_field(name='?/ping', value='Tests the bot\'s ping time', inline=True)
emHelp0.add_field(name='?/stats', value='Shows bot stats', inline=True)
emHelp0.add_field(name='?/suggest <suggestion>', value='DMs my senpai any suggestions you have', inline=True)

emHelp0.add_field(name='?/whois [user]', value='Looks up user info', inline=True)

emHelp0.add_field(name='?/jpeg [{image} | [user]]', value='Adds jpeg compression to images', inline=True)
emHelp0.add_field(name='?/destroy [{image} | [user]]', value='Destroys an image', inline=True)
#emHelp0.add_field(name='?/deepfry <{image}>', value=':b:eep fried :b:emes anyone? :joy:')

#emHelp0.add_field(name='?/help advanced', value='Helpage for more advanced bot commands', inline=True)

emJpeg = discord.Embed(title='✅ JPEG Complete! ✅', color=0x00ff00)
emRape = discord.Embed(title='✅ Image Destroyed! ✅', color=0x00ff00)


def loglog(message):
    ts = time.gmtime()
    print(blankvar.join(('[', time.strftime("%Y-%m-%d %H:%M:%S", ts), '] ', '[LOG] [ ] [ ] ', message)))

def debuglog(message):
    if debug:
        ts = time.gmtime()
        print(blankvar.join(('[', time.strftime("%Y-%m-%d %H:%M:%S", ts), '] ', '[LOG] [D] [ ] ', message)))

def errorlog(message):
    ts = time.gmtime()
    print(blankvar.join(('[', time.strftime("%Y-%m-%d %H:%M:%S", ts), '] ', '[LOG] [ ] [E] ', message)))

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

def get_simple_cmd_output(cmd, stderr=STDOUT):
    """
    Execute a simple external command and get its output.
    """
    args = shlex.split(cmd)
    return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0]


def get_ping_time(host):
    host = host.split(':')[0]
    cmd = "fping {host} -C 1 -q".format(host=host)
    # result = str(get_simple_cmd_output(cmd)).replace('\\','').split(':')[-1].split() if x != '-']
    result = str(get_simple_cmd_output(cmd)).replace('\\', '').split(':')[-1].replace("n'", '').replace("-",
                                                                                                        '').replace(
        "b''", '').split()
    res = [float(x) for x in result]
    if len(res) > 0:
        return sum(res) / len(res)
    else:
        return 999999

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

async def save_stats():
    while True:
        with open('actions.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
            bot.commands, bot.triggers = pickle.load(f)

        with open('actions.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
            pickle.dump([bot.ucommands + bot.commands, bot.utriggers + bot.triggers], f)

        bot.ucommands = 0
        bot.utriggers = 0
        await asyncio.sleep(60)

async def status_change():
    while True:
        await bot.change_presence(game=discord.Game(name=random.choice(stati)))
        await asyncio.sleep(20)
        await bot.change_presence(game=discord.Game(name=random.choice(helpStati) + ' in ' + str(len(bot.servers) - 2) + ' servers'))
        await asyncio.sleep(10)

#END OF FUNCTIONS
#DEFINES:
loglog(blankvar.join(('Starting Cancer Bot v', version, '...')))
startdate = datetime.datetime.now()
bot.ucommands = 0
bot.utriggers = 0
bot.scommands = 0
bot.striggers = 0

try:
    with open('actions.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
        bot.acommands, bot.atriggers = pickle.load(f)
except:
    with open('actions.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump([0, 0], f)

#ASYNCROUS EVENTS:
@bot.event
async def on_ready():
    loglog('Connected to Discord!')
    await bot.edit_profile(username="Cancer Bot")
    loglog(blankvar.join(('(User: "', str(bot.user), '", User ID: "', str(bot.user.id), '")')))

    bot.loop.create_task(status_change())

@bot.event
async def on_server_join(server):
    owner = await bot.get_user_info('273940917596061698')
    await bot.send_message(owner, '**HEWWO SENPAI I HAS JOINED A NEW SERVER CALLED** ' + server.name + ' **WITH** ' + str(len(server.members)) + ' **MEMBERS!**')

@bot.event
async def on_message(message):
    debuglog(blankvar.join(('New Message by ', str(message.author), ' (', str(message.author.id), ') with message ID ', str(message.id), ' in channel ', str(message.channel.id), '.')))
    if message.author.bot:
        debuglog('Message is by me or another bot, exiting...')
        return
    else:
        if message.content.startswith('?/;reload'):
            importlib.reload(Mparser)
            importlib.reload(modules.images)
        elif message.content.startswith('?/'):
            await parser.commands(message)
        else:
            await parser.triggers(message)



        if message.content.lower().startswith('?/help'):
            bot.scommands += 1
            bot.ucommands += 1
            await bot.send_typing(message.channel)
            await bot.delete_message(message)
            emHelp0.set_footer(icon_url=message.author.avatar_url, text=str(message.author.display_name) + ' requested this command')
            await bot.send_message(message.channel, embed=emHelp0)
            save_stats()

        if message.content.lower().startswith('?/ping'):
            bot.scommands += 1
            bot.ucommands += 1
            t1 = time.perf_counter()
            await bot.send_typing(message.channel)
            t2 = time.perf_counter()
            await bot.delete_message(message)
            typingPing = str(math.floor((t2-t1)*1000)) + ' ms'
            dnsPing = str(math.floor(get_ping_time('8.8.8.8'))) + ' ms'
            googlePing = str(math.floor(get_ping_time('google.com'))) + ' ms'
            lanPing = str(math.floor(get_ping_time('192.168.1.1'))) + ' ms'
            emPing = discord.Embed(title=':ping_pong: Pong! :ping_pong:', description='Ping statistics for this bot', color=0x00ff00)
            emPing.add_field(name='Typing ping', value=typingPing, inline=False)
            emPing.add_field(name='DNS (8.8.8.8) ping', value=dnsPing, inline=False)
            emPing.add_field(name='Google (google.com) ping', value=googlePing, inline=False)
            emPing.add_field(name='LAN (192.168.1.1) ping', value=lanPing, inline=False)
            emPing.set_thumbnail(url='https://i.imgur.com/q60RAcT.jpg')
            emPing.set_footer(icon_url=message.author.avatar_url, text=str(message.author.display_name) + ' requested this command')
            await bot.send_message(message.channel, embed=emPing)
            save_stats()



        if message.content.lower().startswith('?/jpeg'):
            bot.scommands += 1
            bot.ucommands += 1
            await bot.send_typing(message.channel)
            fail, exit, url = images.jpeg(message)
            await bot.delete_message(message)
            if fail:
                if exit == 1:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu You made a fucky wucky!! A wittle fucko boingo! You better be working **VEWY HAWD** to fix this! Please supply a `.png`, `.jpg`, `.jpeg` or `.bmp` file!\nError code: `NO_FILE`\n*Request by: `' + str(message.author) + '`*') #CBP
                elif exit == 2:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `DOWNLOAD_FAILED`\n*Request by: `' + str(message.author) + '`*') #CBP
                elif exit == 3:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `FILE_OPEN_FAILURE`\n*Request by: `' + str(message.author) + '`*') #CBP
                elif exit == 4:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `PROCESSING_FAILED`\n*Request by: `' + str(message.author) + '`*') #CBP
                else:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `OOPSIE_WOOPSIE`\n*Request by: `' + str(message.author) + '`*') #CBP
            else:
                emJpeg.set_footer(icon_url=message.author.avatar_url, text=str(message.author.display_name) + ' requested this command')
                emJpeg.set_image(url=url)
                await bot.send_message(message.channel, embed=emJpeg)
            save_stats()

        if message.content.lower().startswith('?/destroy') or message.content.lower().startswith('?/rape'):
            bot.scommands += 1
            bot.ucommands += 1
            await bot.send_typing(message.channel)
            fail, exit, url = images.rape(message)
            await bot.delete_message(message)
            if fail:
                if exit == 1:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu You made a fucky wucky!! A wittle fucko boingo! You better be working **VEWY HAWD** to fix this! Please supply a `.png`, `.jpg`, `.jpeg` or `.bmp` file!\nError code: `NO_FILE`\n*Request by: `' + str(message.author) + '`*') #CBP
                elif exit == 2:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `DOWNLOAD_FAILED`\n*Request by: `' + str(message.author) + '`*') #CBP
                elif exit == 3:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `FILE_OPEN_FAILURE`\n*Request by: `' + str(message.author) + '`*') #CBP
                elif exit == 4:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `PROCESSING_FAILED`\n*Request by: `' + str(message.author) + '`*') #CBP
                else:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `OOPSIE_WOOPSIE`\n*Request by: `' + str(message.author) + '`*') #CBP
            else:
                emRape.set_footer(icon_url=message.author.avatar_url, text=str(message.author.display_name) + ' requested this command')
                emRape.set_image(url=url)
                await bot.send_message(message.channel, embed=emRape)
            save_stats()

        if message.content.lower().startswith('?/deepfry'):
            bot.scommands += 1
            bot.ucommands += 1
            await bot.send_typing(message.channel)
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `FEATURE_NOT_IMPLEMENTED`\n*Request by: `' + str(message.author) + '`*') #CBP
            save_stats()

        if message.content.lower().startswith('?/whois'):
            bot.scommands += 1
            bot.ucommands += 1
            await bot.send_typing(message.channel)
            await bot.delete_message(message)
            if len(message.mentions) > 0:
                if len(message.mentions) > 3:
                    await bot.send_message(message.channel, message.author.mention + ', you supplied more than 3 users to lookup. Because of this, the userinfo is being sent to your DMs.')
                    for user in message.mentions:
                        emWhois = discord.Embed(title='User Info', color=0x00ff00)
                        emWhois.add_field(name='Nickname', value=user.display_name, inline=True)
                        emWhois.add_field(name='Global Name', value=user.name, inline=True)
                        emWhois.add_field(name='Discriminator', value=user.discriminator, inline=True)
                        emWhois.add_field(name='ID', value=user.id, inline=True)
                        emWhois.set_footer(icon_url=message.author.avatar_url, text=str(message.author.display_name) + ' requested this command')
                        emWhois.set_image(url=user.avatar_url)
                        await bot.send_message(message.author, embed=emWhois)
                else:
                    for user in message.mentions:
                        emWhois = discord.Embed(title='User Info', color=0x00ff00)
                        emWhois.add_field(name='Nickname', value=user.display_name, inline=True)
                        emWhois.add_field(name='Global Name', value=user.name, inline=True)
                        emWhois.add_field(name='Discriminator', value=user.discriminator, inline=True)
                        emWhois.add_field(name='ID', value=user.id, inline=True)
                        emWhois.set_footer(icon_url=message.author.avatar_url, text=str(message.author.display_name) + ' requested this command')
                        emWhois.set_image(url=user.avatar_url)
                        await bot.send_message(message.channel, embed=emWhois)
            else:
                emWhois = discord.Embed(title='User Info', color=0x00ff00)
                emWhois.add_field(name='Nickname', value=message.author.display_name, inline=True)
                emWhois.add_field(name='Global Name', value=message.author.name, inline=True)
                emWhois.add_field(name='Discriminator', value=message.author.discriminator, inline=True)
                emWhois.add_field(name='ID', value=message.author.id, inline=True)
                emWhois.set_footer(icon_url=message.author.avatar_url, text=str(message.author.display_name) + ' requested this command')
                emWhois.set_image(url=message.author.avatar_url)
                await bot.send_message(message.channel, embed=emWhois)
            save_stats()

        if message.content.lower().startswith('?/suggest'):
            bot.scommands += 1
            bot.ucommands += 1
            await bot.send_typing(message.channel)
            owner = await bot.get_user_info('273940917596061698')
            await bot.send_message(owner, 'HEWWO SENPAI I HAS FEEDBACK FROM `' + str(message.author) + '`:```' + message.content.split(' ', 1)[1].replace('```', '<REMOVED>') + '```')
            await bot.send_message(message.channel, 'Thanks for your feedback! Senpai has been notified!')
            save_stats()

        if message.content.lower().startswith('?/stats'):
            bot.scommands += 1
            bot.ucommands += 1
            await bot.send_typing(message.channel)
            await bot.delete_message(message)
            save_stats()
            users = []
            for server in bot.servers:
                for user in server.members:
                    if (not (user.id in users) and (not user.bot)):
                        users.append(user.id)
            with open('actions.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
                bot.commands, bot.triggers = pickle.load(f)
            diff = relativedelta(datetime.datetime.now(), startdate)
            uptime = str(diff.days) + ' days, ' + str(diff.hours) + ' hours, ' + str(diff.minutes) + ' minutes and ' + str(diff.seconds) + ' seconds'
            emStats = discord.Embed(description='Statistics on Cancer Bot version ' + version, color=0x00ff00)
            emStats.set_author(name='Cancer Bot Stats', icon_url='https://i.imgur.com/4fehjDz.png')
            emStats.add_field(name='Servers', value=str(len(bot.servers) - 2), inline=True)
            emStats.add_field(name='Users', value=str(len(users)), inline=True)
            emStats.add_field(name='Uptime', value=uptime, inline=False)
            emStats.add_field(name='Actions since restart', value=bot.rcommands + bot.rtriggers, inline=False)
            emStats.add_field(name='Commands', value=bot.rcommands, inline=True)
            emStats.add_field(name='Triggers', value=bot.rtriggers, inline=True)
            emStats.add_field(name='Actions since v9', value=bot.commands + bot.triggers, inline=False)
            emStats.add_field(name='Commands', value=bot.commands, inline=True)
            emStats.add_field(name='Triggers', value=bot.triggers, inline=True)
            emStats.set_footer(icon_url=message.author.avatar_url, text=str(message.author.display_name) + ' requested this command')
            await bot.send_message(message.channel, embed=emStats)
        #bot owner commands
        if message.content.lower().startswith('?/;jpegas'):
            bot.scommands += 1
            bot.ucommands += 1
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                fail, exit, url = images.jpeg(message)
                await bot.delete_message(message)
                if not fail:
                    target = await bot.get_user_info(message.content.split(' ')[1])
                    emJpeg.set_footer(icon_url=target.avatar_url, text=str(target.display_name) + ' requested this command')
                    emJpeg.set_image(url=url)
                    await bot.send_message(message.channel, embed=emJpeg)
                save_stats()

        if message.content.lower().startswith('?/;rapeas'): #CBP
            bot.scommands += 1
            bot.ucommands += 1
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                fail, exit, url = images.rape(message)
                await bot.delete_message(message)
                if not fail:
                    target = await bot.get_user_info(message.content.split(' ')[1])
                    emRape.set_footer(icon_url=target.avatar_url, text=str(target.display_name) + ' requested this command')
                    emRape.set_image(url=url)
                    await bot.send_message(message.channel, embed=emRape)
                save_stats()

        '''if message.content.lower().startswith('?/;deepfryas'):
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                fail, exit, url = images.deepfry(message)
                await bot.delete_message(message)
                if not fail:
                    target = await bot.get_user_info(message.content.split(' ')[1])
                    emDeepfry.set_footer(icon_url=target.avatar_url, text=str(target) + ' requested this command')
                    emDeepfry.set_image(url=url)
                    await bot.send_message(message.channel, embed=emDeepfry)
                save_stats()'''

        if message.content.lower().startswith('?/;delete'):
            bot.scommands += 1
            bot.ucommands += 1
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                try:
                    await bot.delete_message(message)
                except:
                    pass
                if len(message.content.split(' ')) >= 3:
                    channel = await bot.get_channel(message.content.split(' ', 2)[1])
                    target = await bot.get_message(channel, message.content.split(' ')[2])
                else:
                    target = await bot.get_message(message.channel, message.content.split(' ')[1])
                await bot.delete_message(target)
                save_stats()

        if message.content.lower().startswith('?/;say'):
            bot.scommands += 1
            bot.ucommands += 1
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                try:
                    await bot.delete_message(message)
                except:
                    pass
                await bot.send_message(message.channel, message.content.split(' ', 1)[1])
                save_stats()

        if message.content.lower().startswith('?/;asay'):
            bot.scommands += 1
            bot.ucommands += 1
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                try:
                    await bot.delete_message(message)
                except:
                    pass
                channel = bot.get_channel(message.content.split(' ', 2)[1])
                await bot.send_message(channel, message.content.split(' ', 2)[2])
                save_stats()

        if message.content.lower().startswith('?/;kick'):
            bot.scommands += 1
            bot.ucommands += 1
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                try:
                    await bot.delete_message(message)
                except:
                    pass
                if len(message.content.split(' ')) >= 3:
                    server = bot.get_server(message.content.split(' ')[1])
                    member = server.get_member(message.content.split(' ')[2])
                else:
                    server = message.server
                    member = server.get_member(message.content.split(' ')[1])
                try:
                    await bot.kick(member)
                except:
                    await bot.send_message(message.author, ':warning: I have insufficient permissions to do that action in that server, senpai.')
                save_stats()

        if message.content.lower().startswith('?/;ban'):
            bot.scommands += 1
            bot.ucommands += 1
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                try:
                    await bot.delete_message(message)
                except:
                    pass
                if len(message.content.split(' ')) >= 3:
                    server = bot.get_server(message.content.split(' ')[1])
                    member = server.get_member(message.content.split(' ')[2])
                else:
                    server = message.server
                    member = server.get_member(message.content.split(' ')[1])
                try:
                    await bot.ban(member)
                except:
                    await bot.send_message(message.author, ':warning: I have insufficient permissions to do that action in that server, senpai.')
                save_stats()

        if message.content.lower().startswith('?/;unban'):
            bot.scommands += 1
            bot.ucommands += 1
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                try:
                    await bot.delete_message(message)
                except:
                    pass
                if len(message.content.split(' ')) >= 3:
                    server = bot.get_server(message.content.split(' ')[1])
                    user = bot.get_user(message.content.split(' ')[2])
                else:
                    server = message.server
                    user = bot.get_user(message.content.split(' ')[1])
                try:
                    await bot.unban(server, user)
                except:
                    await bot.send_message(message.author, ':warning: I have insufficient permissions to do that action in that server, senpai.')
                save_stats()

        #tChIfunny.join()
        #if ifunny:
    #        await bot.delete_message(message)
#            await bot.send_message(message.channel, blankvar.join(('<:shooter:441972276901052416> ',dancefont['d'],dancefont['e'],dancefont['l'],dancefont['e'],dancefont['t'],' ',dancefont['d'],dancefont['i'],dancefont['s'],' <:shooter:441972276901052416>')))


        debuglog(blankvar.join(('Message #', message.id, ' has finished processing.')))



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
