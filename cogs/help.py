from discord.ext import commands
import discord

class helpCog:
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

    @commands.command(name='help', usage='', brief='Displays this helptext')
    @commands.cooldown(1, 60, commands.BucketType.channel)
    async def helpMsg(self, ctx):
        await ctx.trigger_typing()
        await ctx.message.delete()

        self.emHelp0 = discord.Embed(description='I am under constant development, expect many changes! You can help by sumbitting any suggestions to my senpai by using my suggestion command. (`?/suggest <suggestion>`)\n\nThis bot\'s command prefix is: `?/`\n\n`<argument>` is a required argument\n`[argument]` is an optional argument\n`{image}` is an optional image argument that is attached\n\u200b', color=0x00ff00)
        self.emHelp0.set_thumbnail(url='https://i.imgur.com/fnt3A4l.png')
        self.emHelp0.set_author(name='Cancer Bot Help', icon_url='https://i.imgur.com/4fehjDz.png')

        commands = list(self.bot.walk_commands())
        for command in commands:
            if command.enabled and (not command.hidden):
                try:
                    self.emHelp0.add_field(name='?/' + command.name + ' ' + command.usage, value=command.brief, inline=False)
                except:
                    self.emHelp0.add_field(name='?/' + command.name, value='ERROR: Could not retrieve command info.', inline=False)

        self.emHelp0.set_footer(icon_url=ctx.message.author.avatar_url, text=str(ctx.message.author.display_name) + ' requested this command')
        await ctx.send(embed=self.emHelp0)

    @commands.command(name='helptest', usage='', brief='Displays this helptext', hidden=True)
    @commands.cooldown(1, 60, commands.BucketType.channel)
    async def helpMsg(self, ctx):
        await ctx.trigger_typing()
        await ctx.message.delete()

        self.emHelp0 = discord.Embed(description='I am under constant development, expect many changes! You can help by sumbitting any suggestions to my senpai by using my suggestion command. (`?/suggest <suggestion>`)\n\nThis bot\'s command prefix is: `?/`\n\n`<argument>` is a required argument\n`[argument]` is an optional argument\n\u200b', color=0x00ff00)
        self.emHelp0.set_thumbnail(url='https://i.imgur.com/fnt3A4l.png')
        self.emHelp0.set_author(name='Cancer Bot Help', icon_url='https://i.imgur.com/4fehjDz.png')

        cogs = []
        commands = list(self.bot.walk_commands())
        for command in commands:
            if not command.cog_name in cogs:
                cogs.append(command.cog_name)

        cogs.sort()

        for cog in cogs:
            commandsInCog = []
            for command in commands:
                if command.cog_name == cog:
                    if command.enabled and (not command.hidden):
                        commandsInCog.append(command)
            if len(commandsInCog) > 0:
                commandsInCog.sort(key=lambda command: command.name)
                text = ''
                for command in commandsInCog:
                    try:
                        text += '**?/' + command.name + ' ' + command.usage + '** --- *' + command.brief + '*\n'
                    except:
                        text += '**?/' + command.name + '** --- *Command information unnavaliable*\n'
                self.emHelp0.add_field(name=cog.split('Cog')[0], value=text)

        '''for command in commands:
            if command.enabled and (not command.hidden):
                try:
                    self.emHelp0.add_field(name='?/' + command.name + ' ' + command.usage, value=command.brief, inline=False)
                except:
                    self.emHelp0.add_field(name='?/' + command.name, value='ERROR: Could not retrieve command info.', inline=False)'''

        self.emHelp0.set_footer(icon_url=ctx.message.author.avatar_url, text=str(ctx.message.author.display_name) + ' requested this command')
        await ctx.send(embed=self.emHelp0)

def setup(bot):
    bot.add_cog(helpCog(bot))
