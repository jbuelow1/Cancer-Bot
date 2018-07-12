from discord.ext import commands
import discord

import asyncio
import pickle
import datetime
from dateutil.relativedelta import relativedelta
import time

class statsCog:
    def __init__(self, bot):
        self.bot = bot

        async def save_stats():
            while True:
                try:
                    with open('actions.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
                        self.bot.vcommands, self.bot.vtriggers = pickle.load(f)
                except:
                    self.bot.vcommands = 0
                    self.bot.vtriggers = 0

                with open('actions.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
                    pickle.dump([self.bot.ucommands + self.bot.vcommands, self.bot.utriggers + self.bot.vtriggers], f)

                self.bot.ucommands = 0
                self.bot.utriggers = 0
                await asyncio.sleep(60)

        self.bot.loop.create_task(save_stats())

    async def on_command(self, ctx):
        self.bot.scommands += 1
        self.bot.ucommands += 1

    @commands.command(name='stats', usage='', brief='Shows bot statistics')
    async def stats(self, ctx):
        await ctx.trigger_typing()
        await ctx.message.delete()
        users = []
        for server in self.bot.guilds:
            for user in server.members:
                if (not (user.id in users) and (not user.bot)):
                    users.append(user.id)

        diff = relativedelta(datetime.datetime.now(), self.bot.startdate)
        uptime = str(diff.days) + ' days, ' + str(diff.hours) + ' hours, ' + str(diff.minutes) + ' minutes and ' + str(diff.seconds) + ' seconds'
        emStats = discord.Embed(description='Statistics on Cancer Bot', color=0x00ff00)
        emStats.set_author(name='Cancer Bot Stats', icon_url='https://i.imgur.com/4fehjDz.png')
        emStats.add_field(name='Servers', value=str(len(self.bot.guilds) - 2), inline=True)
        emStats.add_field(name='Users', value=str(len(users)), inline=True)
        emStats.add_field(name='Uptime', value=uptime, inline=False)
        emStats.add_field(name='Actions since restart', value=self.bot.scommands + self.bot.striggers, inline=False)
        emStats.add_field(name='Commands', value=self.bot.scommands, inline=True)
        emStats.add_field(name='Triggers', value=self.bot.striggers, inline=True)
        emStats.add_field(name='Actions since the dawn of time', value=self.bot.vcommands + self.bot.vtriggers + self.bot.ucommands + self.bot.utriggers, inline=False)
        emStats.add_field(name='Commands', value=self.bot.vcommands + self.bot.ucommands, inline=True)
        emStats.add_field(name='Triggers', value=self.bot.vtriggers + self.bot.utriggers, inline=True)
        emStats.set_footer(icon_url=ctx.message.author.avatar_url, text=str(ctx.message.author.display_name) + ' requested this command')
        await ctx.send(embed=emStats)

def setup(bot):
    bot.add_cog(statsCog(bot))
