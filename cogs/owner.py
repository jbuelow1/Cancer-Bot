from discord.ext import commands
import discord

import json
import io
import traceback
import random
import asyncio

class ownerCog:
    def __init__(self, bot):
        self.bot = bot

    async def on_guild_join(self, guild):
        owner = await self.bot.get_user_info('273940917596061698')
        guildDesc = 'Name:          `' + guild.name + '`\nMembers:   `' + str(guild.member_count) + '`\nID:                 `' + str(guild.id) + '`\nChannels:   `' + str(len(guild.channels)) + '`\nCreated at: `' + str(guild.created_at) + '`\nisLarge:       `' + str(guild.large) + '`\nOwner:         `' + str(guild.owner) + '`\nOwner ID:    `' + str(guild.owner.id) + '`'
        if (len(guild.features) > 0):
            guildDesc += '\n\n𝓢𝓹𝓮𝓬𝓲𝓪𝓵 𝓕𝓮𝓪𝓽𝓾𝓻𝓮𝓼: `' + str(guild.features) + '`'
        em = discord.Embed(title='Guild Join', description=guildDesc, color=0x00ff00)
        em.set_image(url=guild.icon_url)
        em.set_thumbnail(url=guild.owner.avatar_url)
        await owner.send(embed=em)

    async def on_guild_remove(self, guild):
        owner = await self.bot.get_user_info('273940917596061698')
        guildDesc = 'Name:          `' + guild.name + '`\nMembers:   `' + str(guild.member_count) + '`\nID:                 `' + str(guild.id) + '`\nChannels:   `' + str(len(guild.channels)) + '`\nCreated at: `' + str(guild.created_at) + '`\nisLarge:       `' + str(guild.large) + '`\nOwner:         `' + str(guild.owner) + '`\nOwner ID:    `' + str(guild.owner.id) + '`'
        if (len(guild.features) > 0):
            guildDesc += '\n\n𝓢𝓹𝓮𝓬𝓲𝓪𝓵 𝓕𝓮𝓪𝓽𝓾𝓻𝓮𝓼: `' + str(guild.features) + '`'
        em = discord.Embed(title='Guild Leave', description=guildDesc, color=0xff0000)
        em.set_image(url=guild.icon_url)
        em.set_thumbnail(url=guild.owner.avatar_url)
        await owner.send(embed=em)

    @commands.command(name='lsguilds', hidden=True)
    @commands.is_owner()
    async def lsguilds(self, ctx):
        guildList = ''
        for guild in self.bot.guilds:
            if (len(guildList) + len(guild.name) + 25) < 2048:
                guildList = guildList + '`' + str(guild.id) + '` | ' + guild.name + '\n'
            else:
                emLsGuilds = discord.Embed(title='Cancer Bot\'s Guild List', description=guildList, color=0xffff00)
                await ctx.send(embed=emLsGuilds)
                guildList = '`' + str(guild.id) + '` | ' + guild.name + '\n'
        emLsGuilds = discord.Embed(title='Cancer Bot\'s Guild List', description=guildList, color=0xffff00)
        await ctx.send(embed=emLsGuilds)

    #why in the actual fucking fuck did i decide to make this command? Like when the fuck will i even use this shit???? ITS SO FUCKING LONG!!!! WHY!!!! WHY THE FUCK DID I WASTE SOOO MUCH FUCKING TIME DOING THIS SHIT?!?!??!?! REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    @commands.command(name='lsreport', hidden=True)
    @commands.is_owner()
    async def lsreport(self, ctx):
        async with ctx.typing():
            try:
                d = json.dumps(self.bot.__dict__)
            except:
                traceback.print_exc()
                await ctx.send(':warning: The JSON dump failed! :warning:')
            else:
                f = io.StringIO(d)
                file = discord.File(d, filename='dump.json')
                await ctx.send(':white_check_mark: Done! :white_check_mark:', file=file)


    @commands.command(name='suggest', usage='<Text>', brief='Sends senpai your "wonderful" ideas')
    @commands.cooldown(3, 86400, commands.BucketType.user)
    async def suggest(self, ctx, *, arg):
        owner = await self.bot.get_user_info('273940917596061698')
        if ctx.guild:
            guildDesc = 'Name:          `' + ctx.guild.name + '`\nMembers:   `' + str(ctx.guild.member_count) + '`\nID:                 `' + str(ctx.guild.id) + '`\nChannels:   `' + str(len(ctx.guild.channels)) + '`\nCreated at: `' + str(ctx.guild.created_at) + '`\nisLarge:       `' + str(ctx.guild.large) + '`\nOwner:         `' + str(ctx.guild.owner) + '`\nOwner ID:    `' + str(ctx.guild.owner.id) + '`'
            if (len(ctx.guild.features) > 0):
                guildDesc += '\n\n𝓢𝓹𝓮𝓬𝓲𝓪𝓵 𝓕𝓮𝓪𝓽𝓾𝓻𝓮𝓼: `' + str(ctx.guild.features) + '`'
            guildDesc += '\n\nAuthor: `' + str(ctx.author) + '`\nFeedback:\n```' + arg.replace('```', '<REMOVED>') + '```'
        else:
            guildDesc = 'Author: `' + str(ctx.author) + '`\nFeedback:\n```' + arg.replace('```', '<REMOVED>') + '```'
        em = discord.Embed(title='Feedback', description=guildDesc, color=0x00ff00)
        em.set_image(url=ctx.author.avatar_url)
        em.set_thumbnail(url=ctx.guild.icon_url)
        await owner.send(embed=em)
        await ctx.send('Thanks for your feedback! Senpai has been notified!')

    @commands.command(name='leave', hidden=True)
    @commands.is_owner()
    async def guildLeave(self, ctx, *, guildID: int):
        guild = self.bot.get_guild(guildID)
        guildDesc = 'Name:          `' + guild.name + '`\nMembers:   `' + str(guild.member_count) + '`\nID:                 `' + str(guild.id) + '`\nChannels:   `' + str(len(guild.channels)) + '`\nCreated at: `' + str(guild.created_at) + '`\nisLarge:       `' + str(guild.large) + '`\nOwner:         `' + str(guild.owner) + '`\nOwner ID:    `' + str(guild.owner.id) + '`'
        if (len(guild.features) > 0):
            guildDesc += '\n\n𝓢𝓹𝓮𝓬𝓲𝓪𝓵 𝓕𝓮𝓪𝓽𝓾𝓻𝓮𝓼: `' + str(guild.features) + '`'
        clocks = ['🕐','🕑','🕒','🕓','🕔','🕕','🕖','🕗','🕘','🕙','🕚','🕛','🕜','🕝','🕞','🕟','🕠','🕡','🕢','🕣','🕤','🕥','🕦','🕧']
        clock = random.choice(clocks)
        guildDesc += '\n\n**__To confirm leaving of this guild, React with ' + clock + '.__**'
        em = discord.Embed(title='Guild Leave Confirmation', description=guildDesc, color=0x00ff00)
        em.set_image(url=guild.icon_url)
        em.set_thumbnail(url=guild.owner.avatar_url)
        await ctx.send(embed=em)
        def check(reaction, user):
            return ctx.author.id == 273940917596061698 and str(reaction.emoji) == clock
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Timeout.')
        else:
            await guild.channels[0].send('Senpai has requested that I leave this guild. Probably because you fuckers are too autistic. Bye, bitches!')
            await guild.leave()

def setup(bot):
    bot.add_cog(ownerCog(bot))
