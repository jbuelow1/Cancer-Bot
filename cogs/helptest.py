from discord.ext import commands
import discord

class thelpCog:
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

    @commands.command(name='thelp', usage='', brief='Displays this helptext', hidden=True)
    @commands.cooldown(1, 60, commands.BucketType.channel)
    async def thelpMsg(self, ctx, *, page=''):
        await ctx.trigger_typing()
        await ctx.message.delete()

        print(str(page))

        if page == '':
            self.emHelp0 = discord.Embed(description='I am under constant development, expect many changes! You can help by sumbitting any suggestions to my senpai by using my suggestion command. (`?/suggest <suggestion>`)\n\nThis bot\'s command prefix is: `?/`\n\n`<argument>` is a required argument\n`[argument]` is an optional argument\n`{image}` is an optional image argument that is attached\n\u200b', color=0x00ff00)
            self.emHelp0.set_thumbnail(url='https://i.imgur.com/fnt3A4l.png')
            self.emHelp0.set_author(name='Cancer Bot Help', icon_url='https://i.imgur.com/4fehjDz.png')

            commands = list(self.bot.walk_commands())
            for command in commands:
                if command.enabled and (not command.hidden) and (not (command.category in self.bot.categories)):
                    try:
                        self.emHelp0.add_field(name='?/' + command.name + ' ' + command.usage, value=command.brief, inline=False)
                    except:
                        self.emHelp0.add_field(name='?/' + command.name, value='ERROR: Could not retrieve command info.', inline=False)

            self.emHelp0.set_footer(icon_url=ctx.message.author.avatar_url, text=str(ctx.message.author.display_name) + ' requested this command')
            await ctx.send(embed=self.emHelp0)

def setup(bot):
    bot.add_cog(thelpCog(bot))
