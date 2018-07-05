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

    #@commands.command(name='bee', usage='', brief='Buzz buzz, motherfucker', hidden=True)
    @commands.cooldown(1, 60, commands.BucketType.channel)
    async def beePasta(self, ctx):
        request_result = requests.get('https://gist.githubusercontent.com/The5heepDev/a15539b297a7862af4f12ce07fee6bb7/raw/7164813a9b8d0a3b2dcffd5b80005f1967887475/entire_bee_movie_script')
        pasta = request_result.content
        lines = textwrap.wrap(pasta, width=2000)
        for line in lines:
            await ctx.send(line)

def setup(bot):
    bot.add_cog(copypastaCog(bot))
