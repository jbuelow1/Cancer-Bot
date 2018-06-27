from discord.ext import commands

class helpCog:
    def __init__(self, bot):
        self.bot = bot

    @self.bot.listen()
    async def on_message(message):
        
