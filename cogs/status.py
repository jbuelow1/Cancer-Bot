from discord.ext import commands
import discord

import random
import asyncio
import time
import pickle
import os
import configparser
import requests

class statusCog:
    def __init__(self, bot):
        self.bot = bot

        async def status_change():
            while True:
                with open('status.pkl', 'rb') as f:
                    stati, helpStati = pickle.load(f)
                try:
                    await self.bot.change_presence(game=discord.Game(name=random.choice(stati)))
                except:
                    print('[WARN] Setting status message failed! Either this server is offline, or the API is down.')
                await asyncio.sleep(20)
                try:
                    await self.bot.change_presence(game=discord.Game(name=random.choice(helpStati) + ' in ' + str(len(self.bot.guilds)) + ' servers'))
                except:
                    print('[WARN] Setting status message failed! Either this server is offline, or the API is down.')
                await asyncio.sleep(10)

        self.bot.loop.create_task(status_change())

    async def has_voted(ctx):
        filename = "ifr.cfg"
        if os.path.isfile(filename):
            config = configparser.ConfigParser()
            config.read(filename)
            dbltoken = config.get("config", "dbltoken")
        else:
            print('Could not find a config file for dbl. HOW THE FUCK AM I RUNNING????')
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = dbltoken
        r = requests.get('https://discordbots.org/api/bots/439851454203691019/check?userId=' + str(ctx.author.id), headers=headers)
        if r.status_code == 200:
            rdict = r.json()
            if rdict['voted'] == 1:
                return True
            if rdict['voted'] == 0:
                await ctx.send(':no_entry_sign: Woah there! Seems like you havent voted today! Try using this command again once you have voted. :no_entry_sign:\nVote for Cancer Bot at: https://discordbots.org/bot/439851454203691019/vote')
                return False

    @commands.group(name='addstatus', hidden=True, invoke_without_command=True)
    async def addstatus(self, ctx):
        await ctx.send(':warning: Use `?/addstatus status <status>` or `?/addstatus help <status>`. :warning:')

    @addstatus.command(name='status', hidden=True)
    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.check(has_voted)
    async def addstatusstatus(self, ctx, *, arg):
        with open('status.pkl', 'rb') as f:
            stati, helpStati = pickle.load(f)
        stati.append(arg)
        with open('status.pkl', 'wb') as f:
            pickle.dump([stati, helpStati], f)

    @addstatus.command(name='help', hidden=True)
    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.check(has_voted)
    async def addhelpstatus(self, ctx, *, arg):
        with open('status.pkl', 'rb') as f:
            stati, helpStati = pickle.load(f)
        helpStati.append(arg)
        with open('status.pkl', 'wb') as f:
            pickle.dump([stati, helpStati], f)

def setup(bot):
    bot.add_cog(statusCog(bot))
