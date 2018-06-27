from discord.ext import commands
import discord

class helpCog:
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

        self.emHelp0 = discord.Embed(description='I am under constant development, expect many changes! You can help by sumbitting any suggestions to my senpai by using my suggestion command. (`?/suggest <suggestion>`)\n\nThis bot\'s command prefix is: `?/`\n\n`<argument>` is a required argument\n`[argument]` is an optional argument\n`{image}` is an optional image argument that is attached\n\u200b', color=0x00ff00)
        self.emHelp0.set_thumbnail(url='https://i.imgur.com/fnt3A4l.png')
        self.emHelp0.set_author(name='Cancer Bot Help', icon_url='https://i.imgur.com/4fehjDz.png')
        self.emHelp0.add_field(name='?/help', value='Displays this help text', inline=True)
        self.emHelp0.add_field(name='?/ping', value='Tests the bot\'s ping time', inline=True)
        self.emHelp0.add_field(name='?/stats', value='Shows bot stats', inline=True)
        self.emHelp0.add_field(name='?/suggest <suggestion>', value='DMs my senpai any suggestions you have', inline=True)

    @commands.command(name='help')
    async def helpMsg(self, ctx):
        await ctx.trigger_typing()
        await ctx.message.delete()
        self.emHelp0.set_footer(icon_url=ctx.message.author.avatar_url, text=str(ctx.message.author.display_name) + ' requested this command')
        await ctx.send(embed=self.emHelp0)

def setup(bot):
    bot.add_cog(helpCog(bot))
