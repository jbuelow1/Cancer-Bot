import asyncio

class Mparser:
    def __init__(self, bot):
        self.bot = bot

    def commands(bot, message):
        pass

    def triggers(message):
        if message.server.id == '264445053596991498':
            return

        if (findWholeWord('heck')(message.content.lower()) or findWholeWord('hek')(message.content.lower()) or findWholeWord('hecking')(message.content.lower()) or findWholeWord('heckin')(message.content.lower())):
            await self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            emHeck.set_image(url=random.choice(hecks))
            await self.bot.send_message(message.channel, embed=emHeck)

        if message.mention_everyone:
            await self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            await self.bot.send_message(message.channel, random.choice(pingemojis))

        if (findWholeWord('die')(message.content.lower()) or findWholeWord('kys')(message.content.lower()) or findWholeWord('kms')(message.content.lower())): #CBP
            await self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            if self.bot.user.mentioned_in(message):
                await self.bot.send_message(message.channel, 'no u')
                await self.bot.send_message(message.channel, 'Ladies and gentlmen, I appear to have won this argument. You can stop fighting like little cucklets now.') #CBP
            else:
                await self.bot.send_message(message.channel, embed=emBleach)

        elif self.bot.user.mentioned_in(message):
            await self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            if (findWholeWord('die')(message.content.lower()) or findWholeWord('kys')(message.content.lower()) or findWholeWord('kms')(message.content.lower())):
                await self.bot.send_message(message.channel, 'no u')
                await self.bot.send_message(message.channel, 'Ladies and gentlmen, I appear to have won this argument. You can stop fighting like little cucklets now.') #CBP
            else:
                await self.bot.send_message(message.channel, 'H- Hewwo?!')

        if findWholeWord('xd')(message.content.lower()):
            await self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            await self.bot.send_message(message.channel, '<a:xd:442034831690301461>')

        if '🤔' in message.content:
            await self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            await self.bot.send_message(message.channel, embed=emThink)

        if 'no u' in message.content.lower():
            await self.bot.send_typing(message.channel)
            self.bot.striggers += 1
            self.bot.utriggers += 1
            await self.bot.send_message(message.channel, 'Ladies and gentlmen, <@' + message.author.id + '> appears to have won this argument. You can stop fighting like little cucklets now.') #CBP
