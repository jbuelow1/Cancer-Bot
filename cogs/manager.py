from discord.ext import commands

import py_compile
import shutil

class managerCog:

    def __init__(self, bot):
        self.bot = bot
        self.loadedmods = [
        'cogs.manager',
        'cogs.owner',
        'cogs.status',
        'cogs.trigger',
        'cogs.basic',
        'cogs.stats',
        'cogs.images',
        'cogs.help',
        'cogs.copypasta'
        ]

    async def is_dev(ctx):
        devs = [
        273940917596061698
        ]
        return ctx.author.id in devs

    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send('**ERROR:** `' + str(e) + '`')
        else:
            await ctx.send('**SUCCESS:** `Loaded module named \'' + cog + '\'`')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def cog_unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send('**ERROR:** `' + str(e) + '`')
        else:
            await ctx.send('**SUCCESS:** `Unloaded module named \'' + cog + '\'`')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
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

    @commands.group(name='modman', hidden=True, invoke_without_command=True)
    @commands.check(is_dev)
    async def modman(self, ctx):
        await ctx.send('modman requires an action.')

    @modman.command(name='load', hidden=True)
    @commands.check(is_dev)
    async def modmanLoad(self, ctx, *, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send('**ERROR:** `' + str(e) + '`')
        else:
            await ctx.send('**SUCCESS:** `Loaded module named \'' + cog + '\'`')

    @modman.command(name='unload', hidden=True)
    @commands.check(is_dev)
    async def modmanUnload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send('**ERROR:** `' + str(e) + '`')
        else:
            await ctx.send('**SUCCESS:** `Unloaded module named \'' + cog + '\'`')

    @modman.command(name='reload', hidden=True)
    @commands.check(is_dev)
    async def modmanReload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send('**ERROR:** `' + str(e) + '`')
        else:
            await ctx.send('**SUCCESS:** `Unloaded module named \'' + cog + '\'`\n**SUCCESS:** `Loaded module named \'' + cog + '\'`')

    @modman.command(name='clear', hidden=True)
    @commands.check(is_dev)
    async def modmanClear(self, ctx):
        try:
            shutil.rmtree('cogs/__pycache__')
        except Exception as e:
            await ctx.send('**ERROR:** `' + str(e) + '`')
        else:
            await ctx.send('**SUCCESS:** `Cache folder has been cleared.`')

    @modman.group(name='list', hidden=True, invoke_without_command=True)
    @commands.check(is_dev)
    async def modmanList(self, ctx):
        await ctx.send('You must specify ~~`all`~~, `avaliable` or ~~`loaded`~~.')

    @modmanList.command(name='avaliable', hidden=True)
    @commands.check(is_dev)
    async def modmanListAvaliable(self, ctx):
        mods = ''
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                mods += file.replace(file.split('.')[-1], '').replace('/','.') + '\n'
        await ctx.send('Module listing complete:\n```' + mods + '```')

def setup(bot):
    bot.add_cog(managerCog(bot))
