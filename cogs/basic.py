from discord.ext import commands
import discord

import math
import shlex

class basicCog:
    def __init__(self, bot):
        self.bot = bot

    def get_simple_cmd_output(cmd, stderr=STDOUT):
        """
        Execute a simple external command and get its output.
        """
        args = shlex.split(cmd)
        return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0]

    def get_ping_time(host):
        host = host.split(':')[0]
        cmd = "fping {host} -C 1 -q".format(host=host)
        # result = str(get_simple_cmd_output(cmd)).replace('\\','').split(':')[-1].split() if x != '-']
        result = str(self.get_simple_cmd_output(cmd)).replace('\\', '').split(':')[-1].replace("n'", '').replace("-",
                                                                                                            '').replace(
            "b''", '').split()
        res = [float(x) for x in result]
        if len(res) > 0:
            return sum(res) / len(res)
        else:
            return 999999

    @commands.command(name='ping')
    async def ping(self, ctx, *, host: str):
        t1 = time.perf_counter()
        await ctx.trigger_typing()
        t2 = time.perf_counter()
        await ctx.message.delete()
        typingPing = str(math.floor((t2-t1)*1000)) + ' ms'
        dnsPing = str(math.floor(self.get_ping_time('8.8.8.8'))) + ' ms'
        googlePing = str(math.floor(self.get_ping_time('google.com'))) + ' ms'
        lanPing = str(math.floor(self.get_ping_time('192.168.1.1'))) + ' ms'
        emPing = discord.Embed(title=':ping_pong: Pong! :ping_pong:', description='Ping statistics for this bot', color=0x00ff00)
        emPing.add_field(name='Typing ping', value=typingPing, inline=False)
        emPing.add_field(name='DNS (8.8.8.8) ping', value=dnsPing, inline=False)
        emPing.add_field(name='Google (google.com) ping', value=googlePing, inline=False)
        emPing.add_field(name='LAN (192.168.1.1) ping', value=lanPing, inline=False)
        emPing.set_thumbnail(url='https://i.imgur.com/q60RAcT.jpg')
        emPing.set_footer(icon_url=message.author.avatar_url, text=str(message.author.display_name) + ' requested this command')
        await bot.send_message(message.channel, embed=emPing)

    @commands.command(name='whois')
    async def whois(self, ctx):
        await ctx.trigger_typing()
        await ctx.message.delete()
        if len(ctx.message.mentions) > 0:
            if len(ctx.message.mentions) > 3:
                await ctx.send(ctx.message.author.mention + ', you supplied more than 3 users to lookup. Because of this, the userinfo is being sent to your DMs.')
                for user in ctx.message.mentions:
                    emWhois = discord.Embed(title='User Info', color=0x00ff00)
                    emWhois.add_field(name='Nickname', value=user.display_name, inline=True)
                    emWhois.add_field(name='Global Name', value=user.name, inline=True)
                    emWhois.add_field(name='Discriminator', value=user.discriminator, inline=True)
                    emWhois.add_field(name='ID', value=user.id, inline=True)
                    emWhois.set_footer(icon_url=message.author.avatar_url, text=str(message.author.display_name) + ' requested this command')
                    emWhois.set_image(url=user.avatar_url)
                    await user.send(embed=emWhois)
            else:
                for user in message.mentions:
                    emWhois = discord.Embed(title='User Info', color=0x00ff00)
                    emWhois.add_field(name='Nickname', value=user.display_name, inline=True)
                    emWhois.add_field(name='Global Name', value=user.name, inline=True)
                    emWhois.add_field(name='Discriminator', value=user.discriminator, inline=True)
                    emWhois.add_field(name='ID', value=user.id, inline=True)
                    emWhois.set_footer(icon_url=message.author.avatar_url, text=str(message.author.display_name) + ' requested this command')
                    emWhois.set_image(url=user.avatar_url)
                    await ctx.send(embed=emWhois)
        else:
            emWhois = discord.Embed(title='User Info', color=0x00ff00)
            emWhois.add_field(name='Nickname', value=ctx.message.author.display_name, inline=True)
            emWhois.add_field(name='Global Name', value=ctx.message.author.name, inline=True)
            emWhois.add_field(name='Discriminator', value=ctx.message.author.discriminator, inline=True)
            emWhois.add_field(name='ID', value=ctx.message.author.id, inline=True)
            emWhois.set_footer(icon_url=ctx.message.author.avatar_url, text=str(ctx.message.author.display_name) + ' requested this command')
            emWhois.set_image(url=ctx.message.author.avatar_url)
            await ctx.send(embed=emWhois)

    
