from discord.ext import commands
import discord

import json
import io
import sys

class ownerCog:
    def __init__(self, bot):
        self.bot = bot

    async def on_guild_join(self, guild):
        owner = await self.bot.get_user_info('273940917596061698')
        guildDesc = '**Guild Joined**\n\nName: `' + guild.name + '`\nMember count: `' + str(guild.member_count) + '`\nID: `' + str(guild.id) + '`\nChannels: `' + str(len(guild.channels)) + '`\nCreated at: `' + str(guild.created_at) + '`\nisLarge: `' + str(guild.large) + '`\nOwner: `' + str(guild.owner) + '`\nOwner ID: `' + str(guild.owner.id) + '`'
        if (len(guild.features) > 0):
            guildDesc += '\n\n𝓢𝓹𝓮𝓬𝓲𝓪𝓵 𝓕𝓮𝓪𝓽𝓾𝓻𝓮𝓼: `' + str(guild.features) + '`'
        guildDesc += '\n========================='
        await owner.send(guildDesc)

    @commands.command(name='lsguilds', hidden=True)
    @commands.is_owner()
    async def lsguilds(self, ctx):
        guildList = ''
        for guild in self.bot.guilds:
            guildList = guildList + guild.name + '\n'
        emLsGuilds = discord.Embed(title='Cancer Bot\'s Guild List', description=guildList)
        await ctx.send(embed=emLsGuilds)

    #why in the actual fucking fuck did i decide to make this command? Like when the fuck will i even use this shit???? ITS SO FUCKING LONG!!!! WHY!!!! WHY THE FUCK DID I WASTE SOOO MUCH FUCKING TIME DOING THIS SHIT?!?!??!?! REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    @commands.command(name='lsreport', hidden=True)
    @commands.is_owner()
    async def lsreport(self, ctx):
        async with ctx.typing():
            try:
                d = json.dump(self.bot.__dict__)
            except:
                await ctx.send(':warning: The JSON dump failed! :warning:```' + sys.exc_info[0] + '```')
            else:
                f = io.StringIO(d)
                file = discord.File(d, filename='dump.json')
                await ctx.send(':white_check_mark: Done! :white_check_mark:', file=file)


    @commands.command(name='suggest', usage='<Text>', brief='Sends senpai your "wonderful" ideas')
    async def suggest(self, ctx, *, arg):
        owner = await self.bot.get_user_info('273940917596061698')
        await owner.send('HEWWO SENPAI I HAS FEEDBACK FROM `' + str(ctx.message.author) + '`:```' + arg.replace('```', '<REMOVED>') + '```')
        await ctx.send('Thanks for your feedback! Senpai has been notified!')

def setup(bot):
    bot.add_cog(ownerCog(bot))
