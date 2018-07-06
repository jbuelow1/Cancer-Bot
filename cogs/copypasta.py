from discord.ext import commands
import discord

import requests
import textwrap

class copypastaCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='fit', usage='', brief='Gotta stay fit, kids')
    async def fitPasta(self, ctx):
        await ctx.send('**The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.**')

    @commands.command(name='bee', usage='', brief='why? (spam warning)')
    @commands.cooldown(1, 300, commands.BucketType.channel)
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
