from discord.ext import commands
import discord

from PIL import Image
from PIL import ImageFilter
from io import StringIO, BytesIO
import requests
import asyncio

class imagesCog:
    def __init__(self, bot):
        self.bot = bot

    def getImages(self, message):
        images = []
        for attachment in message.attachments:
            if any([
            attachment.filename.lower().endswith('png'),
            attachment.filename.lower().endswith('jpg'),
            attachment.filename.lower().endswith('jpeg'),
            attachment.filename.lower().endswith('bmp')
            ]):
                image_request_result = requests.get(attachment.url)
                image = Image.open(BytesIO(image_request_result.content))
                images.append(image)
        for user in message.mentions:
            image_request_result = requests.get(user.avatar_url)
            image = Image.open(BytesIO(image_request_result.content))
            images.append(image)
        return images

    def addjpeg(self, image, quality=1):
        image = image.convert('RGB')
        output = BytesIO()
        image.save(output, format="JPEG", quality=quality)
        done = output.getvalue()
        output.close()
        done = Image.open(BytesIO(done))
        return done

    def unsharpenimg(self, image, ammount=80000):
        image = image.filter(ImageFilter.UnsharpMask(ammount,ammount,0))
        output = BytesIO()
        image.save(output, format="PNG")
        done = output.getvalue()
        output.close()
        done = Image.open(BytesIO(done))
        return done

    def unfortunateProcess(self, image):
        image = image.resize((350, 300))
        unfortunate = Image.open('imgsrc/unfortunate.png')
        unfortunate.paste(image, (625, 400), mask=image)
        return unfortunate


    @commands.command(name='jpeg')
    async def jpeg(self, ctx):
        async with ctx.typing():
            images = self.getImages(ctx.message)
            if len(images) > 0:
                if len(images) < 10:
                    outputImages = []
                    filenum = 0
                    for image in images:
                        image = self.addjpeg(image)

                        output = BytesIO()
                        image.save(output, format="PNG")
                        image = output.getvalue()
                        output.close()

                        outputImages.append(discord.File(BytesIO(image), filename='jpeg' + str(filenum) + '.jpeg'))
                        filenum += 1
                        print(outputImages)
                    await ctx.send(':white_check_mark: Done! :white_check_mark:', files=outputImages)
                else:
                    await ctx.send(':warning: Too many files! Please supply 1-10 per message. :warning:')
            else:
                await ctx.send(':warning: Please supply a `.png`, `.jpg`/`.jpeg`, or `.bmp` image file! :warning:')

    @commands.command(name='unsharpen')
    async def unsharpen(self, ctx):
        async with ctx.typing():
            images = self.getImages(ctx.message)
            if len(images) > 0:
                if len(images) < 10:
                    outputImages = []
                    filenum = 0
                    for image in images:
                        image = self.unsharpenimg(image, 20000)

                        output = BytesIO()
                        image.save(output, format="PNG")
                        image = output.getvalue()
                        output.close()

                        outputImages.append(discord.File(BytesIO(image), filename='jpeg' + str(filenum) + '.jpeg'))
                        filenum += 1
                        print(outputImages)
                    await ctx.send(':white_check_mark: Done! :white_check_mark:', files=outputImages)
                else:
                    await ctx.send(':warning: Too many files! Please supply 1-10 per message. :warning:')
            else:
                await ctx.send(':warning: Please supply a `.png`, `.jpg`/`.jpeg`, or `.bmp` image file! :warning:')


    @commands.command(name='destroy')
    async def destroy(self, ctx):
        async with ctx.typing():
            images = self.getImages(ctx.message)
            if len(images) > 0:
                if len(images) < 10:
                    outputImages = []
                    filenum = 0
                    for image in images:
                        image = self.unsharpenimg(image)
                        image = self.addjpeg(image)

                        output = BytesIO()
                        image.save(output, format="PNG")
                        image = output.getvalue()
                        output.close()

                        outputImages.append(discord.File(BytesIO(image), filename='jpeg' + str(filenum) + '.jpeg'))
                        filenum += 1
                        print(outputImages)
                    await ctx.send(':white_check_mark: Done! :white_check_mark:', files=outputImages)
                else:
                    await ctx.send(':warning: Too many files! Please supply 1-10 per message. :warning:')
            else:
                await ctx.send(':warning: Please supply a `.png`, `.jpg`/`.jpeg`, or `.bmp` image file! :warning:')

    @commands.command(name='unfortunate')
    async def unfortunate(self, ctx):
        async with ctx.typing():
            images = self.getImages(ctx.message)
            if len(images) > 0:
                if len(images) < 10:
                    outputImages = []
                    filenum = 0
                    for image in images:
                        image = self.unfortunateProcess(image)

                        output = BytesIO()
                        image.save(output, format="PNG")
                        image = output.getvalue()
                        output.close()

                        outputImages.append(discord.File(BytesIO(image), filename='jpeg' + str(filenum) + '.jpeg'))
                        filenum += 1
                        print(outputImages)
                    await ctx.send(':white_check_mark: Done! :white_check_mark:', files=outputImages)
                else:
                    await ctx.send(':warning: Too many files! Please supply 1-10 per message. :warning:')
            else:
                await ctx.send(':warning: Please supply a `.png`, `.jpg`/`.jpeg`, or `.bmp` image file! :warning:')

def setup(bot):
    bot.add_cog(imagesCog(bot))
