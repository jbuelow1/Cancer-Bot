from discord.ext import commands
import discord

class ownerCog:
    def __init__(self, bot):
        self.bot = bot

    async def on_guild_join(self, guild):
        owner = await self.bot.get_user_info('273940917596061698')
        await owner.send('**HEWWO SENPAI I HAS JOINED A NEW GUILD CALLED** ' + guild.name + ' **WITH** ' + str(len(guild.members)) + ' **MEMBERS!**')

    @commands.command(name='suggest')
    async def suggest(self, ctx, *, arg):
        owner = await self.bot.get_user_info('273940917596061698')
        await owner.send('HEWWO SENPAI I HAS FEEDBACK FROM `' + str(ctx.message.author) + '`:```' + arg.replace('```', '<REMOVED>') + '```')
        await ctx.send('Thanks for your feedback! Senpai has been notified!')

def setup(bot):
    bot.add_cog(ownerCog(bot))
