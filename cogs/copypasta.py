from discord.ext import commands
import discord

import os
import requests
import textwrap
import configparser
import ast

class copypastaCog:
    def __init__(self, bot):
        self.bot = bot
        filename = "ifr.cfg"
        if os.path.isfile(filename):
            config = configparser.ConfigParser()
            config.read(filename)
            self.dbltoken = config.get("config", "dbltoken")
        else:
            print('Could not find a config file for dbl. HOW THE FUCK AM I RUNNING????')

    async def has_voted(self, ctx):
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = self.dbltoken
        r = requests.get('https://discordbots.org/api/bots/439851454203691019/check?userId=' + str(ctx.author.id), headers=headers)
        if r.status_code == 200:
            rdict = ast.literal_eval(r.json())
            if rdict['voted'] == 1:
                return True
            if rdict['voted'] == 0:
                await ctx.send(':no_entry_sign: Woah there! Seems like you havent voted today! Try using this command again once you have voted. :no_entry_sign:\nVote for Cancer Bot at: https://discordbots.org/bot/439851454203691019/vote')
                return False

    @commands.command(category='copypasta', name='fit', usage='', brief='Gotta stay fit, kids')
    async def fitPasta(self, ctx):
        await ctx.send('**The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.**')

    @commands.command(category='copypasta', name='bee', usage='', brief='why? (spam warning)')
    @commands.cooldown(1, 300, commands.BucketType.channel)
    @commands.check(self.has_voted)
    async def beePasta(self, ctx):
        f = open('copypastas/bee.txt', mode='r')
        pasta = f.read()
        lines = textwrap.wrap(pasta, width=1990)
        for line in lines:
            await ctx.send('**' + line + '**')
            await ctx.trigger_typing()
        await ctx.send('That is all.')


def setup(bot):
    bot.add_cog(copypastaCog(bot))
