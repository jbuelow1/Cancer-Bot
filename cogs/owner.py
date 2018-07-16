from discord.ext import commands
import discord

class ownerCog:
    def __init__(self, bot):
        self.bot = bot

    async def on_guild_join(self, guild):
        owner = await self.bot.get_user_info('273940917596061698')
        guildDesc = '**Guild Joined**\n\nName: `' + guild.name + '`\nMember count: `' + str(guild.member_count) + '`\nID: `' + str(guild.id) + '`\nChannels: `' + str(len(guild.channels)) + '`\nCreated at: `' + str(guild.created_at) + '`\nisLarge: `' + str(guild.large) + '`\nOwner: `' + str(guild.owner) + '`\nOwner ID: `' + str(guild.owner.id) + '`'
        if (len(guild.features) > 0):
            guildDesc += '\n\n𝓢𝓹𝓮𝓬𝓲𝓪𝓵 𝓕𝓮𝓪𝓽𝓾𝓻𝓮𝓼: `' + str(guild.features) + '`'
        await owner.send(guildDesc)

    @commands.command(name='lsguilds', hidden=True)
    @commands.is_owner()
    async def lsguilds(self, ctx):
        guildList = ''
        for guild in self.bot.guilds:
            guildList = guildList + guild.name + '\n'
        emLsGuilds = discord.Embed(title='Cancer Bot\'s Guild List', description=guildList)
        await ctx.send(embed=emLsGuilds)

    #why in the actual fucking fuck did i decide to make this command? Like when the fuck will i even use this shit???? ITS SO FUCKING LONG!!!! WHY!!!! WHY THE FUCK DID I WASTE SOOO MUCH FUCKING TIME DOING THIS SHIT?!?!??!?! REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    '''@commands.command(name='lsreport', hidden=True)
    @commands.is_owner()
    async def lsreport(self, ctx):
        d = {}

        d['client']['latency'] = self.bot.latency
        guilds = {}
        for guild in self.bot.guilds:
            guildD = {}
            guildD['name'] = guild.name
            guildD['id'] = guild.id

            guildD['roles'] = {}
            roles = {}
            for role in guild.roles:
                roleD = {}
                roleD['name'] = role.name
                roleD['id'] = role.id
                roleD['permissions'] = role.permissions
                roleD['guild__id'] = role.guild.id
                roleD['color'] = role.color
                roleD['hoist'] = role.hoist
                roleD['position'] = role.position
                roleD['managed'] = role.managed
                roleD['mentionable'] = role.mentionable
                roleD['is_default'] = role.is_default()
                roleD['created_at'] = role.created_at
                roleD['mention'] = role.mention
                roleD['members'] = {}
                for member in role.members:
                    roleD['members'][member.id]['name'] = member.name
                    roleD['members'][member.id]['id'] = member.id
                roles[role.id] = roleD
            guildD['roles'] = roles

            guildD['emojis'] = {}
            emojis = {}
            for emoji in guild.emojis:
                emojiD = {}
                emojiD['name'] = emoji.name
                emojiD['id'] = emoji.id
                emojiD['require_colons'] = emoji.require_colons
                emojiD['animated'] = emoji.animated
                emojiD['managed'] = emoji.managed
                emojiD['guild_id'] = emoji.guild_id
                emojiD['created_at'] = emoji.created_at
                emojiD['url'] = emoji.url
                emojiD['roles'] = {}
                for role in emoji.roles:
                    emojiD['roles'][role.id]['name'] = role.name
                    emojiD['roles'][role.id]['id'] = role.id
                emojiD['guild']['name'] = emoji.guild.name
                emojiD['guild']['id'] = emoji.guild.id
                emojis[emoji.id] = emojiD
            guildD['emojis'] = emojis

            guildD['region'] = guild.region
            guildD['afk_timeout'] = guild.afk_timeout
            #guildD['afk_channel'] #add the thing from guild.channels here
            guildD['icon'] = guild.icon
            guildD['owner_id'] = guild.owner_id
            guildD['unavaliable'] = guild.unavaliable
            guildD['mfa_level'] = guild.mfa_level
            guildD['verification_level'] = guild.verification_level
            guildD['explicit_content_filter'] = guild.explicit_content_filter
            guildD['features'] = guild.features
            guildD['splash'] = guild.splash

            guildD['channels'] = {}
            channels = {}
            for channel in guild.channels:
                channelD = {}
                channelD['name'] = channel.name
                channelD['id'] = channel.id
                channelD['']

        d['client']['guilds'] = guilds
        d['client']['emojis'] = self.bot.emojis
        d['client']['private_channels'] = self.bot.private_channels
        d['client']['voice_clients'] = self.bot.voice_clients
        d['client']['is_ready'] = self.bot.is_ready()
        d['client']['is_closed'] = self.bot.is_closed()
        d['client']['activity'] = self.bot.activity
        d['client']

        userD = {}
        user = self.bot.user
        userD['name'] = user.name
        userD['id'] = user.id
        userD['discriminator'] = user.discriminator
        userD['avatar'] = user.avatar
        userD['bot'] = user.bot
        userD['verified'] = user.verified
        userD['email'] = user.email
        userD['mfa_enabled'] = user.mfa_enabled
        userD['premium'] = user.premium
        userD['relationships'] = user.relationships
        userD['friends'] = user.friends
        userD['blocked'] = user.blocked
        userD['avatar_url'] = user.avatar_url
        userD['created_at'] = user.created_at
        userD['default_avatar'] = user.default_avatar
        userD['default_avatar_url'] = user.default_avatar_url
        userD['display_name'] = user.display_name
        userD['is_avatar_animated'] = user.is_avatar_animated()
        userD['mention'] = user.mention
        d['client']['user'] = userD'''

    @commands.command(name='suggest', usage='<Text>', brief='Sends senpai your "wonderful" ideas')
    async def suggest(self, ctx, *, arg):
        owner = await self.bot.get_user_info('273940917596061698')
        await owner.send('HEWWO SENPAI I HAS FEEDBACK FROM `' + str(ctx.message.author) + '`:```' + arg.replace('```', '<REMOVED>') + '```')
        await ctx.send('Thanks for your feedback! Senpai has been notified!')

def setup(bot):
    bot.add_cog(ownerCog(bot))
