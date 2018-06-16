import asyncio

class Mparser:
    def __init__(self, bot):
        self.bot = bot

        def self.self.findWholeWorld(w):
            return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

    def commands(self, message):
        pass

    def triggers(self, message):
        if message.server.id == '264445053596991498':
            return

        if (self.findWholeWorld('heck')(message.content.lower()) or self.findWholeWorld('hek')(message.content.lower()) or self.findWholeWorld('hecking')(message.content.lower()) or self.findWholeWorld('heckin')(message.content.lower())):
            self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            emHeck.set_image(url=random.choice(hecks))
            self.bot.send_message(message.channel, embed=emHeck)

        if message.mention_everyone:
            self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            self.bot.send_message(message.channel, random.choice(pingemojis))

        if (self.findWholeWorld('die')(message.content.lower()) or self.findWholeWorld('kys')(message.content.lower()) or self.findWholeWorld('kms')(message.content.lower())): #CBP
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
            if (self.findWholeWorld('die')(message.content.lower()) or self.findWholeWorld('kys')(message.content.lower()) or self.findWholeWorld('kms')(message.content.lower())):
                self.bot.send_message(message.channel, 'no u')
                self.bot.send_message(message.channel, 'Ladies and gentlmen, I appear to have won this argument. You can stop fighting like little cucklets now.') #CBP
            else:
                self.bot.send_message(message.channel, 'H- Hewwo?!')

        if self.findWholeWorld('xd')(message.content.lower()):
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
