import re
import discord
import random

class Mparser:
    def __init__(self, bot):
        self.bot = bot
        self.hecks = [
        'https://i.imgur.com/ynS00JL.jpg',
        'https://i.imgur.com/YaFUVwE.jpg',
        'https://i.imgur.com/S6sqpoq.png',
        'https://i.imgur.com/zTxzouf.jpg',
        'https://i.imgur.com/z4u0Juo.png',
        'https://i.imgur.com/z4u0Juo.png',
        'https://i.imgur.com/vcTg4tO.jpg',
        ]

        self.pingemojis = [
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

        self.dancefont = {
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

    def findWholeWorld(self, w):
        return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

    def wordInString(self, word, string_value):
        return True if re.search(r'\b' + word + r'\b', string_value) else False

    def commands(self, message):
        pass

    def triggers(self, message):
        hecks = [
        'https://i.imgur.com/ynS00JL.jpg',
        'https://i.imgur.com/YaFUVwE.jpg',
        'https://i.imgur.com/S6sqpoq.png',
        'https://i.imgur.com/zTxzouf.jpg',
        'https://i.imgur.com/z4u0Juo.png',
        'https://i.imgur.com/z4u0Juo.png',
        'https://i.imgur.com/vcTg4tO.jpg',
        ]

        
        print("starting trigger parser...")
        emBleach = discord.Embed(title=''.join((self.dancefont['k'],self.dancefont['y'],self.dancefont['s'])), color=0x00ff00) #CBP
        emBleach.set_image(url="https://i.imgur.com/Mto46BE.png")

        emHeck = discord.Embed(title='No Swearing!', color=0x00ff00)

        emThink = discord.Embed(title=':thinking::thinking::thinking::thinking::thinking:', color=0x00ff00)
        emThink.set_image(url="https://i.imgur.com/wHMWq1B.gif")

        if message.server.id == '264445053596991498':
            return

        if (self.wordInString('heck', message.content.lower()) or self.wordInString('hek', message.content.lower()) or self.wordInString('hecking', message.content.lower()) or self.wordInString('heckin', message.content.lower())):
            print("heck found.")

            self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            emHeck.set_image(url=random.choice(hecks))
            self.bot.send_message(message.channel, embed=emHeck)
            print("done prosessing trigger.")

        if message.mention_everyone:
            self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            self.bot.send_message(message.channel, random.choice(pingemojis))

        if (self.wordInString('die', message.content.lower()) or self.wordInString('kys', message.content.lower()) or self.wordInString('kms', message.content.lower())): #CBP
            self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            if self.bot.user.mentioned_in(message):
                self.bot.send_message(message.channel, 'no u')
                self.bot.send_message(message.channel, 'Ladies and gentlmen, I appear to have won this argument. You can stop fighting like little cucklets now.') #CBP
            else:
                self.bot.send_message(message.channel, embed=emBleach)

        elif self.bot.user.mentioned_in(message):
            self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            if (self.wordInString('die', message.content.lower()) or self.wordInString('kys', message.content.lower()) or self.wordInString('kms', message.content.lower())):
                self.bot.send_message(message.channel, 'no u')
                self.bot.send_message(message.channel, 'Ladies and gentlmen, I appear to have won this argument. You can stop fighting like little cucklets now.') #CBP
            else:
                self.bot.send_message(message.channel, 'H- Hewwo?!')

        if self.wordInString('xd', message.content.lower()):
            self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            self.bot.send_message(message.channel, '<a:xd:442034831690301461>')

        if '🤔' in message.content:
            self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            self.bot.send_message(message.channel, embed=emThink)

        if 'no u' in message.content.lower():
            self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            self.bot.send_message(message.channel, 'Ladies and gentlmen, <@' + message.author.id + '> appears to have won this argument. You can stop fighting like little cucklets now.') #CBP
