from discord.ext import commands
import discord

import traceback
import sys

class errorCog:
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(':no_entry_sign: ' + ctx.author.mention + ', that command is on cooldown. Please try again in ' + str(error.retry_after) + ' seconds. :no_entry_sign:')

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(':no_entry_sign: ' + ctx.author.mention + ', that command is currently disabled. Please try again later. :no_entry_sign:')

        if isinstance(error, commands.NotOwner):
            await ctx.send(':raised_hand: HALT! That command is for senpai only!')

        if isinstance(error, commands.MissingPermissions):
            perms = ''
            for perm in error.missing_perms:
                perms = perms + '\n' + str(perm)
            await ctx.send(':no_entry_sign: Sorry, ' + ctx.author.mention + ', but you do not have sufficient permissions to do that here. Contact an admin of this server for help. :no_entry_sign:\n```Missing Permissions for ' + ctx.author.nick + ':' + perms + '```')

        if isinstance(error, commands.BotMissingPermissions):
            perms = ''
            for perm in error.missing_perms:
                perms = perms + '\n' + str(perm)
            await ctx.send(':no_entry_sign: Sorry, ' + ctx.author.mention + ', but I do not have sufficient permissions to do that here. Contact an admin of this server for help. :no_entry_sign:\n```Missing Permissions for ' + self.bot.user.nick + ':' + perms + '```')

        if await self.bot.is_owner(ctx.author):
            await ctx.send(':warning: An error has occoured in that command! :warning:\nTraceback:```' + sys.exc_info() + '```')

def setup(bot):
    bot.add_cog(errorCog(bot))
