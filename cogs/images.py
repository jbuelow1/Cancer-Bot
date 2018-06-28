from discord.ext import commands
import discord

from PIL import Image
from io import StringIO, BytesIO
import requests

class imagesCog:
    def __init__(self, bot):
        self.bot = bot

    def getImages(message):
        if message.attachments == []:
            return []
        else:
            images = []
            for attachment in message.attachments:
                if any([
                attachment.filename.lower().endswith('png'),
                attachment.filename.lower().endswith('jpg'),
                attachment.filename.lower().endswith('jpeg'),
                attachment.filename.lower().endswith('bmp')
                ]):
                    image_request_result = requests.get(attachment.url)
                    image = Image.open(StringIO(image_request_result.content))
                    images.append(image)
            return images

    def addjpeg(image, quality=1):
        image = image.convert('RGB')
        output = StringIO()
        image.save(output, format="JPEG", quality=quality)
        done = output.getvalue()
        output.close()
        return done

    @commands.command(name='jpeg')
    async def jpeg(self, ctx):
        images = self.getImages(ctx.message)
        if len(images) > 0:
            if len(images) < 10:
                outputImages = []
                for image in images:
                    image = self.addjpeg(image)
                    outputImages.append(discord.File(BytesIO(image)))
                ctx.send(':white_check_mark: Done! :white_check_mark:', files=outputImages)
            else:
                ctx.send(':warning: Too many files! Please supply 1-10 per message. :warning:')
        else:
            ctx.send(':warning: Please supply a `.png`, `.jpg`/`.jpeg`, or `.bmp` image file! :warning:')

    @commands.command(name='destroy')
    async def destroy(self, ctx):
        pass

def setup(bot):
    bot.add_cog(imagesCog(bot))
