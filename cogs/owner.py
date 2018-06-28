from discord.ext import commands
import discord

class ownerCog:
    def __init__(self, bot):
        self.bot = bot

    async def on_server_join(self, server):
        owner = await bot.get_user_info('273940917596061698')
        await owner.send('**HEWWO SENPAI I HAS JOINED A NEW SERVER CALLED** ' + server.name + ' **WITH** ' + str(len(server.members)) + ' **MEMBERS!**')

    @commands.command(name='suggest')
    async def suggest(self, ctx, *, arg):
        owner = await bot.get_user_info('273940917596061698')
        await owner.send('HEWWO SENPAI I HAS FEEDBACK FROM `' + str(ctx.message.author) + '`:```' + arg.replace('```', '<REMOVED>') + '```')
        await ctx.send('Thanks for your feedback! Senpai has been notified!')

def setup(bot):
    bot.add_cog(ownerCog(bot))
