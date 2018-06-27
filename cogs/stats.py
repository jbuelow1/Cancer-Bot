from discord.ext import commands
import discord

class statsCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stats')
    async def stats(self, ctx):
        await ctx.trigger_typing()
        await ctx.message.delete()
        users = []
        for server in bot.servers:
            for user in server.members:
                if (not (user.id in users) and (not user.bot)):
                    users.append(user.id)
        diff = relativedelta(datetime.datetime.now(), startdate)
        uptime = str(diff.days) + ' days, ' + str(diff.hours) + ' hours, ' + str(diff.minutes) + ' minutes and ' + str(diff.seconds) + ' seconds'
        emStats = discord.Embed(description='Statistics on Cancer Bot version ' + version, color=0x00ff00)
        emStats.set_author(name='Cancer Bot Stats', icon_url='https://i.imgur.com/4fehjDz.png')
        emStats.add_field(name='Servers', value=str(len(bot.servers) - 2), inline=True)
        emStats.add_field(name='Users', value=str(len(users)), inline=True)
        emStats.add_field(name='Uptime', value=uptime, inline=False)
        emStats.add_field(name='Actions since restart', value=bot.rcommands + bot.rtriggers, inline=False)
        emStats.add_field(name='Commands', value=bot.rcommands, inline=True)
        emStats.add_field(name='Triggers', value=bot.rtriggers, inline=True)
        emStats.add_field(name='Actions since v9', value=bot.commands + bot.triggers, inline=False)
        emStats.add_field(name='Commands', value=bot.commands, inline=True)
        emStats.add_field(name='Triggers', value=bot.triggers, inline=True)
        emStats.set_footer(icon_url=message.author.avatar_url, text=str(message.author.display_name) + ' requested this command')
        await ctx.send(embed=emStats)

def setup(bot):
    bot.add_cog(statsCog(bot))
