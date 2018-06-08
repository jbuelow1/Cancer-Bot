
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

#modules
import images

version = '3'
blankvar = ''
headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
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

debug = True

bot = discord.Client()

emBleach = discord.Embed(title=''.join((dancefont['k'],dancefont['y'],dancefont['s'])), colour=0x121296)
emBleach.set_image(url="https://i.imgur.com/Mto46BE.png")

emHeck = discord.Embed(title='No Swearing!', colour=0x121296)

emThink = discord.Embed(title=':thinking::thinking::thinking::thinking::thinking:', colour=0x121296)
emThink.set_image(url="https://i.imgur.com/wHMWq1B.gif")

emHelp0 = discord.Embed(description='I am under constant development, expect many changes! You can help by sumbitting any suggestions to my senpai by using my suggestion command. (`?/suggest <suggestion>`)\n\nThis bot\'s command prefix is: `?/`\n\u200b', colour=0x121296)
emHelp0.set_thumbnail(url='https://i.imgur.com/fnt3A4l.png')
emHelp0.set_author(name='Cancer Bot Help', icon_url='https://i.imgur.com/4fehjDz.png')
emHelp0.add_field(name='?/help', value='Displays this help text', inline=True)
emHelp0.add_field(name='?/jpeg', value='Adds jpeg compression to images', inline=True)
emHelp0.add_field(name='?/ping', value='Tests the bot\'s ping time', inline=True)
emHelp0.add_field(name='?/rape', value='Utterly fucks an image', inline=True)
#emHelp0.add_field(name='?/deepfry', value=':b:eep fried :b:emes anyone? :joy:')
emHelp0.add_field(name='?/whois <ID>', value='Looks up user info by ID', inline=True)
emHelp0.add_field(name='?/suggest <suggestion>', value='DMs my senpai any suggestions you have', inline=True)

#emHelp0.add_field(name='?/help advanced', value='Helpage for more advanced bot commands', inline=True)

emJpeg = discord.Embed(title='✅ JPEG Complete! ✅')
emRape = discord.Embed(title='✅ Image Fucked! ✅')


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
    #Execute a simple external command and get its output.
    args = shlex.split(cmd)
    return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0]

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

#END OF FUNCTIONS
#DEFINES:
loglog(blankvar.join(('Starting Cancer Bot v', version, '...')))


#ASYNCROUS EVENTS:
@bot.event
async def on_ready():
    loglog('Connected to Discord!')
    await bot.edit_profile(username="Cancer Bot")
    loglog(blankvar.join(('(User: "', str(bot.user), '", User ID: "', str(bot.user.id), '")')))
    await bot.change_presence(game=discord.Game(name='with kids | ?/help'))

@bot.event
async def on_message(message):
    debuglog(blankvar.join(('New Message by ', str(message.author), ' (', str(message.author.id), ') with message ID ', str(message.id), ' in channel ', str(message.channel.id), '.')))
    if message.author == bot.user:
        debuglog('Message is by me, exiting...')
        return
    else:
        #tChIfunny = threading.Thread(target=chIfunny, args=(message,))
        tJpeg = threading.Thread(target=images.jpeg, args=(message,))


        if (findWholeWord('heck')(message.content.lower()) or findWholeWord('hek')(message.content.lower()) or findWholeWord('hecking')(message.content.lower()) or findWholeWord('heckin')(message.content.lower())):
            await bot.send_typing(message.channel)
            emHeck.set_image(url=random.choice(hecks))
            await bot.send_message(message.channel, embed=emHeck)

        if '@everyone' in message.content:
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, random.choice(pingemojis))

        if (findWholeWord('die')(message.content.lower()) or findWholeWord('kys')(message.content.lower()) or findWholeWord('kms')(message.content.lower())):
            await bot.send_typing(message.channel)
            if (blankvar.join(('<@', bot.user.id, '>')) in message.content) or (blankvar.join(('<!@', bot.user.id, '>')) in message.content):
                await bot.send_message(message.channel, 'no u')
                await bot.send_message(message.channel, 'Ladies and gentlmen, I appear to have won this argument. You can stop fighting like little cucklets now.')
            else:
                await bot.send_message(message.channel, embed=emBleach)
        elif (blankvar.join(('<@', bot.user.id, '>')) in message.content) or (blankvar.join(('<!@', bot.user.id, '>')) in message.content):
            await bot.send_typing(message.channel)
            if (findWholeWord('die')(message.content.lower()) or findWholeWord('kys')(message.content.lower()) or findWholeWord('kms')(message.content.lower())):
                await bot.send_message(message.channel, 'no u')
                await bot.send_message(message.channel, 'Ladies and gentlmen, I appear to have won this argument. You can stop fighting like little cucklets now.')
            else:
                await bot.send_message(message.channel, 'H- Hewwo?!')

        if findWholeWord('xd')(message.content.lower()):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, '<a:xd:442034831690301461>')

        if '🤔' in message.content:
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, embed=emThink)

        if message.content.lower().startswith('?/help'):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, embed=emHelp0)

        if message.content.lower().startswith('?/ping'):
            t1 = time.perf_counter()
            await bot.send_typing(message.channel)
            t2 = time.perf_counter()
            typingPing = str(round((t2-t1)*1000, 1)) + ' ms'
            try:
                dnsPing = get_simple_cmd_output('fping -C 1 -q 8.8.8.8').split(' ')[2]
                googlePing = get_simple_cmd_output('fping -C 1 -q google.com').split(' ')[2]
                lanPing = get_simple_cmd_output('fping -C 1 -q 192.168.1.1').split(' ')[2]
            except:
                print(get_simple_cmd_output('fping -C 1 -q 192.168.1.1').split(' ')[2])
            emPing = discord.Embed(title=':ping_pong: Pong! :ping_pong:')
            emPing.add_field(name='Typing ping', value=typingPing, inline=True)
            emPing.add_field(name='DNS ping', value=dnsPing, inline=True)
            emPing.add_field(name='Google ping', value=googlePing, inline=True)
            emPing.add_field(name='LAN ping', value=lanPing, inline=True)
            await bot.send_message(message.channel, embed=emPing)

        if 'no u' in message.content.lower():
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, 'Ladies and gentlmen, <@' + message.author.id + '> appears to have won this argument. You can stop fighting like little cucklets now.')

        if message.content.lower().startswith('?/jpeg'):
            await bot.send_typing(message.channel)
            fail, exit, url = images.jpeg(message)
            await bot.delete_message(message)
            if fail:
                if exit == 1:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu You made a fucky wucky!! A wittle fucko boingo! You better be working **VEWY HAWD** to fix this! Please supply a `.png`, `.jpg`, `.jpeg` or `.bmp` file!\nError code: `YOURE_AUTISTIC`\n*Request by: `' + str(message.author) + '`*')
                elif exit == 2:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `DOWNLOAD_FAILED`\n*Request by: `' + str(message.author) + '`*')
                elif exit == 3:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `FILE_OPEN_FAILURE`\n*Request by: `' + str(message.author) + '`*')
                elif exit == 4:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `PROCESSING_FAILED`\n*Request by: `' + str(message.author) + '`*')
                else:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `OOPSIE_WOOPSIE`\n*Request by: `' + str(message.author) + '`*')
            else:
                emJpeg.set_footer(icon_url=message.author.avatar_url, text=str(message.author) + ' requested this command')
                emJpeg.set_image(url=url)
                await bot.send_message(message.channel, embed=emJpeg)

        if message.content.lower().startswith('?/rape'):
            await bot.send_typing(message.channel)
            fail, exit, url = images.rape(message)
            await bot.delete_message(message)
            if fail:
                if exit == 1:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu You made a fucky wucky!! A wittle fucko boingo! You better be working **VEWY HAWD** to fix this! Please supply a `.png`, `.jpg`, `.jpeg` or `.bmp` file!\nError code: `YOURE_AUTISTIC`\n*Request by: `' + str(message.author) + '`*')
                elif exit == 2:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `DOWNLOAD_FAILED`\n*Request by: `' + str(message.author) + '`*')
                elif exit == 3:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `FILE_OPEN_FAILURE`\n*Request by: `' + str(message.author) + '`*')
                elif exit == 4:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `PROCESSING_FAILED`\n*Request by: `' + str(message.author) + '`*')
                else:
                    await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `OOPSIE_WOOPSIE`\n*Request by: `' + str(message.author) + '`*')
            else:
                emRape.set_footer(icon_url=message.author.avatar_url, text=str(message.author) + ' requested this command')
                emRape.set_image(url=url)
                await bot.send_message(message.channel, embed=emRape)

        if message.content.lower().startswith('?/deepfry'):
            await bot.send_typing(message.channel)
            await bot.send_message(message.channel, ':warning: **OOPSIE WOOPSIE!!** Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working **VEWY HAWD** to fix this!\nError code: `FEATURE_NOT_IMPLEMENTED`\n*Request by: `' + str(message.author) + '`*')

        if message.content.lower().startswith('?/whois'):
            pass

        if message.content.lower().startswith('?/suggest'):
            pass

        #bot owner commands
        if message.content.lower().startswith('?/;jpegas'):
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                fail, exit, url = images.jpeg(message)
                await bot.delete_message(message)
                if not fail:
                    target = await bot.get_user_info(message.content.split(' ')[1])
                    emJpeg.set_footer(icon_url=target.avatar_url, text=str(target) + ' requested this command')
                    emJpeg.set_image(url=url)
                    await bot.send_message(message.channel, embed=emJpeg)

        if message.content.lower().startswith('?/;rapeas'):
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                fail, exit, url = images.rape(message)
                await bot.delete_message(message)
                if not fail:
                    target = await bot.get_user_info(message.content.split(' ')[1])
                    emRape.set_footer(icon_url=target.avatar_url, text=str(target) + ' requested this command')
                    emRape.set_image(url=url)
                    await bot.send_message(message.channel, embed=emRape)

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
                    await bot.send_message(message.channel, embed=emDeepfry)'''

        if message.content.lower().startswith('?/;delete'):
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

        if message.content.lower().startswith('?/;say'):
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                try:
                    await bot.delete_message(message)
                except:
                    pass
                await bot.send_message(message.channel, message.content.split(' ', 1)[1])

        if message.content.lower().startswith('?/;asay'):
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                try:
                    await bot.delete_message(message)
                except:
                    pass
                channel = await bot.get_channel(message.content.split(' ', 2)[1])
                await bot.send_message(channel, message.content.split(' ', 2)[2])

        if message.content.lower().startswith('?/;kick'):
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
                    await bot.send_message(message.author, ':warning: I have insufficient permissions to do that action in that server, daddy.')

        if message.content.lower().startswith('?/;ban'):
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
                    await bot.send_message(message.author, ':warning: I have insufficient permissions to do that action in that server, daddy.')

        if message.content.lower().startswith('?/;unban'):
            debuglog('Owner command triggered.')
            if str(message.author.id) == '273940917596061698':
                loglog('Bot owner has issued a owner command.')
                try:
                    await bot.delete_message(message)
                except:
                    pass
                if len(message.content.split(' ')) >= 3:
                    server = bot.get_server(message.content.split(' ')[1])
                    user = server.get_user(message.content.split(' ')[2])
                else:
                    server = message.server
                    user = server.get_user(message.content.split(' ')[1])
                try:
                    await bot.unban(server, user)
                except:
                    await bot.send_message(message.author, ':warning: I have insufficient permissions to do that action in that server, daddy.')

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
