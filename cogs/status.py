from discord.ext import commands
import discord

import random
import asyncio

class statusCog:
    def __init__(self, bot):
        self.bot = bot

    async def status_change(self):
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

        while True:
            await self.bot.change_presence(game=discord.Game(name=random.choice(stati)))
            await asyncio.sleep(20)
            #await self.bot.change_presence(game=discord.Game(name=random.choice(helpStati) + ' in ' + str(len(bot.servers) - 2) + ' servers'))
            await asyncio.sleep(10)

def setup(bot):
    bot.add_cog(statusCog(bot))
    bot.loop.create_task(statusCog.status_change())
