from discord.ext import commands
import discord

import random
import asyncio
import time
import pickle

class statusCog:
    def __init__(self, bot):
        self.bot = bot

        async def status_change():
            while True:
                try:
                    with open('status.pkl', 'rb') as f:
                        stati, helpStati = pickle.load(f)
                    await self.bot.change_presence(game=discord.Game(name=random.choice(stati)))
                    await asyncio.sleep(20)
                    await self.bot.change_presence(game=discord.Game(name=random.choice(helpStati) + ' in ' + str(len(self.bot.guilds)) + ' servers'))
                    await asyncio.sleep(10)
                except:
                    print('[WARN] Setting status message failed! Either this server is offline, or the API is down.')

        self.bot.loop.create_task(status_change())

    @commands.group(name='addstatus', hidden=True)
    async def addstatus(self, ctx, *, arg):
        await ctx.send(':warning: Use `?/addstatus status <status>` or `?/addstatus help <status>`. :warning:')

    @addstatus.command(name='status', hidden=True)
    async def addstatusstatus(self, ctx, *, arg):
        with open('status.pkl', 'rb') as f:
            stati, helpStati = pickle.load(f)
        stati.append(arg)
        with open('status.pkl', 'wb') as f:
            pickle.dump([stati, helpStati], f)

    @addstatus.command(name='help', hidden=True)
    async def addhelpstatus(self, ctx, *, arg):
        with open('status.pkl', 'rb') as f:
            stati, helpStati = pickle.load(f)
        helpStati.append(arg)
        with open('status.pkl', 'wb') as f:
            pickle.dump([stati, helpStati], f)

def setup(bot):
    bot.add_cog(statusCog(bot))
