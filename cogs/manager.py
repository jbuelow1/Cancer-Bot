from discord.ext import commands
import discord

import py_compile
import shutil
import os
import shlex
from subprocess import Popen, PIPE, STDOUT

class managerCog:

    def __init__(self, bot):
        self.bot = bot
        self.loadedmods = [
        'cogs.manager',
        'cogs.errors',
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

    '''# Hidden means it won't show up on the default help.
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
            await ctx.send('**SUCCESS:** `Unloaded module named \'' + cog + '\'`\n**SUCCESS:** `Loaded module named \'' + cog + '\'`')'''

    @commands.group(name='modman', hidden=True, invoke_without_command=True)
    @commands.check(is_dev)
    async def modman(self, ctx):
        e = discord.Embed(title='No action specified', description='You can use:\n`load`\n`unload`\n`reload`\n`clear`\n`list`\n`pull`', color=0xff0000)
        e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=e)

    @modman.command(name='load', hidden=True)
    @commands.check(is_dev)
    async def modmanLoad(self, ctx, *, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            e = discord.Embed(title='Could not load module', description='Python error while loading module ' + cog + ':\n```' + str(e) + '```', color=0xff0000)
            e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=e)
        else:
            if not cog in self.loadedmods:
                self.loadedmods.append(cog)
            e = discord.Embed(title='Module Loaded', color=0x00ff00)
            e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
            e.add_field(name='Module', value=cog)
            await ctx.send(embed=e)

    @modman.command(name='unload', hidden=True)
    @commands.check(is_dev)
    async def modmanUnload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            e = discord.Embed(title='Could not unload module', description='Python error while unloading module ' + cog + ':\n```' + str(e) + '```', color=0xff0000)
            e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=e)
        else:
            if cog in self.loadedmods:
                self.loadedmods.remove(cog)
            e = discord.Embed(title='Module Unloaded', color=0x00ff00)
            e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
            e.add_field(name='Module', value=cog)
            await ctx.send(embed=e)

    @modman.command(name='reload', hidden=True)
    @commands.check(is_dev)
    async def modmanReload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            e = discord.Embed(title='Could not reload module', description='Python error while reloading module ' + cog + ':\n```' + str(e) + '```', color=0xff0000)
            e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=e)
        else:
            if not cog in self.loadedmods:
                self.loadedmods.append(cog)
            e = discord.Embed(title='Module Reloaded', color=0x00ff00)
            e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
            e.add_field(name='Module', value=cog)
            await ctx.send(embed=e)

    @modman.command(name='clear', hidden=True)
    @commands.check(is_dev)
    async def modmanClear(self, ctx):
        try:
            shutil.rmtree('cogs/__pycache__')
        except Exception as e:
            e = discord.Embed(title='Could not clear cache', description='Python error while clearing cache:\n```' + str(e) + '```', color=0xff0000)
            e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title='Cache cleared', color=0x00ff00)
            e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=e)

    @modman.group(name='list', hidden=True, invoke_without_command=True)
    @commands.check(is_dev)
    async def modmanList(self, ctx):
        e = discord.Embed(title='No action specified', description='You can use:\n`avaliable`\n`loaded`', color=0xff0000)
        e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=e)

    @modmanList.command(name='avaliable', hidden=True)
    @commands.check(is_dev)
    async def modmanListAvaliable(self, ctx):
        mods = ''
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                mods += '`cogs.' + file.split('.py')[0].replace('/','.') + '`\n'
        e = discord.Embed(title='Avaliable Modules', description=mods, color=0x00ff00)
        e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=e)

    @modmanList.command(name='loaded', hidden=True)
    @commands.check(is_dev)
    async def modmanListLoaded(self, ctx):
        mods = ''
        for mod in self.loadedmods:
            mods += '`' + mod + '`\n'
        e = discord.Embed(title='Loaded Modules', description=mods, color=0x00ff00)
        e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=e)

    @modman.command(name='pull', hidden=True)
    @commands.check(is_dev)
    async def modmanPull(self, ctx):
        args = shlex.split('git pull')
        output = Popen(args, stdout=PIPE, stderr=STDOUT).communicate()[0]
        if output == b'Already up-to-date.\n':
            e = discord.Embed(title='Already up to date', color=0xffff00)
            e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=e)
        else:
            #output = b'From https://github.com/jbuelow1/Cancer-Bot\n   04f217e..0626e1a  stable     -> origin/stable\nUpdating 04f217e..0626e1a\nFast-forward\n cogs/manager.py | 1 -\n 1 file changed, 1 deletion(-)'
            await ctx.send('```' + output + '```')
            files = ''
            lines = output.decode().split('\n')
            del lines[:4]
            del lines[-1]
            del lines[-1]
            for file in lines:
                files += file.split('|')[0].split(' ')[0] + ' - ' + file.split('|')[1].split(' ')[1] + ' edits'
            final = 'Repository: ' + output.decode().split('\n')[1].split(' ')[1] + '\nBranch: ' + output.decode().split('\n')[1].split(' ')[3] + '\n----------\n' + files
            e = discord.Embed(title='Files pulled from GitHub', description=final, color=0x00ff00)
            e.set_author(name='Cancer Bot Module Manager', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=e)
            #hi

def setup(bot):
    bot.add_cog(managerCog(bot))
