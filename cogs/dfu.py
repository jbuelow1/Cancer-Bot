from discord.ext import commands

import py_compile

class dfuCog:

    def __init__(self, bot, callback):
        self.bot = bot

    @commands.group(name='dfu')

    # Hidden means it won't show up on the default help.
    @dfu.command(name='load', hidden=True)
    @dfu.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send('**ERROR:** `' + str(e) + '`')
        else:
            await ctx.send('**SUCCESS:** `Loaded module named \'' + cog + '\'`')

    @dfu.command(name='unload', hidden=True)
    @dfu.is_owner()
    async def cog_unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send('**ERROR:** `' + str(e) + '`')
        else:
            await ctx.send('**SUCCESS:** `Unloaded module named \'' + cog + '\'`')

    @dfu.command(name='reload', hidden=True)
    @dfu.is_owner()
    async def cog_reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            py_compile.compile(cog.replace('.', '/') + '.py')
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send('**ERROR:** `' + str(e) + '`')
        else:
            await ctx.send('**SUCCESS:** `Unloaded module named \'' + cog + '\'`\n**SUCCESS:** `Loaded module named \'' + cog + '\'`')


def setup(bot):
    bot.add_cog(dfuCog(bot))