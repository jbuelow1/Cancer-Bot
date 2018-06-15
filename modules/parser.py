import asyncio

def commands(bot, message):
    pass

def triggers(bot, message):
    if message.server.id == '264445053596991498':
        return

    if (findWholeWord('heck')(message.content.lower()) or findWholeWord('hek')(message.content.lower()) or findWholeWord('hecking')(message.content.lower()) or findWholeWord('heckin')(message.content.lower())):
        await bot.send_typing(message.channel)
        bot.striggers += 1
        bot.utriggers += 1
        emHeck.set_image(url=random.choice(hecks))
        await bot.send_message(message.channel, embed=emHeck)

    if message.mention_everyone:
        await bot.send_typing(message.channel)
        bot.striggers += 1
        bot.utriggers += 1
        await bot.send_message(message.channel, random.choice(pingemojis))

    if (findWholeWord('die')(message.content.lower()) or findWholeWord('kys')(message.content.lower()) or findWholeWord('kms')(message.content.lower())): #CBP
        await bot.send_typing(message.channel)
        bot.striggers += 1
        bot.utriggers += 1
        if bot.user.mentioned_in(message):
            await bot.send_message(message.channel, 'no u')
            await bot.send_message(message.channel, 'Ladies and gentlmen, I appear to have won this argument. You can stop fighting like little cucklets now.') #CBP
        else:
            await bot.send_message(message.channel, embed=emBleach)

    elif bot.user.mentioned_in(message):
        await bot.send_typing(message.channel)
        bot.striggers += 1
        bot.utriggers += 1
        if (findWholeWord('die')(message.content.lower()) or findWholeWord('kys')(message.content.lower()) or findWholeWord('kms')(message.content.lower())):
            await bot.send_message(message.channel, 'no u')
            await bot.send_message(message.channel, 'Ladies and gentlmen, I appear to have won this argument. You can stop fighting like little cucklets now.') #CBP
        else:
            await bot.send_message(message.channel, 'H- Hewwo?!')

    if findWholeWord('xd')(message.content.lower()):
        await bot.send_typing(message.channel)
        bot.striggers += 1
        bot.utriggers += 1
        await bot.send_message(message.channel, '<a:xd:442034831690301461>')

    if '🤔' in message.content:
        await bot.send_typing(message.channel)
        bot.striggers += 1
        bot.utriggers += 1
        await bot.send_message(message.channel, embed=emThink)

    if 'no u' in message.content.lower():
        await bot.send_typing(message.channel)
        bot.striggers += 1
        bot.utriggers += 1
        await bot.send_message(message.channel, 'Ladies and gentlmen, <@' + message.author.id + '> appears to have won this argument. You can stop fighting like little cucklets now.') #CBP
