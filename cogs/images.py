from discord.ext import commands
import discord

from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw, ImageFont
from io import StringIO, BytesIO
import requests
import asyncio
import os
import textwrap

class imagesCog:
    def __init__(self, bot):
        self.bot = bot

    def getImages(self, message):
        images = []
        for attachment in message.attachments:
            if os.path.splitext(attachment.filename)[1].lower() in ('.png', '.jpg', '.jpeg', '.bmp'):
                image_request_result = requests.get(attachment.url)
                image = Image.open(BytesIO(image_request_result.content))
                images.append(image)
        for user in message.mentions:
            image_request_result = requests.get(user.avatar_url)
            image = Image.open(BytesIO(image_request_result.content))
            images.append(image)
        """messages = await message.channel.history(limit=25).flatten()
        for testMessage in messages:
            for attachment in testMessage.attachments:
                if os.path.splitext(attachment.filename)[1].lower() in ('.png', '.jpg', '.jpeg', '.bmp'):
                    image_request_result = requests.get(attachment.url)
                    image = Image.open(BytesIO(image_request_result.content))
                    images.append(image)
            if not images == []:
                break"""
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

    def rescale(self, img, max_width, max_height, force=True):
    	"""Rescale the given image, optionally cropping it to make sure the result image has the specified width and height."""
    	if not force:
    		img.thumbnail((max_width, max_height), Image.ANTIALIAS)
    	else:
    		src_width, src_height = img.size
    		src_ratio = float(src_width) / float(src_height)
    		dst_width, dst_height = max_width, max_height
    		dst_ratio = float(dst_width) / float(dst_height)

    		if dst_ratio < src_ratio:
    			crop_height = src_height
    			crop_width = crop_height * dst_ratio
    			x_offset = float(src_width - crop_width) / 2
    			y_offset = 0
    		else:
    			crop_width = src_width
    			crop_height = crop_width / dst_ratio
    			x_offset = 0
    			y_offset = float(src_height - crop_height) / 3
    		img = img.crop((x_offset, y_offset, x_offset+int(crop_width), y_offset+int(crop_height)))
    		img = img.resize((dst_width, dst_height), Image.ANTIALIAS)

    	return img


    def picInPic(self, image, background, size, location):
        image = image.convert('RGBA')
        image = self.rescale(image, size[0], size[1], True)
        background.paste(image, location, mask=image)
        return background


    @commands.command(name='jpeg')
    @commands.cooldown(1, 10, commands.BucketType.channel)
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
    @commands.cooldown(1, 10, commands.BucketType.channel)
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
    @commands.cooldown(1, 10, commands.BucketType.channel)
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
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def unfortunate(self, ctx):
        async with ctx.typing():
            images = self.getImages(ctx.message)
            if len(images) > 0:
                if len(images) < 10:
                    outputImages = []
                    filenum = 0
                    for image in images:
                        background = Image.open('imgsrc/unfortunate.png')
                        image = self.picInPic(image, background, (350, 300), (625, 400))

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

    @commands.command(name='14rw')
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def reasonswhy(self, ctx):
        async with ctx.typing():
            images = self.getImages(ctx.message)
            if len(images) > 0:
                if len(images) < 10:
                    outputImages = []
                    filenum = 0
                    for image in images:
                        background = Image.open('imgsrc/14rw.png')
                        image = self.picInPic(image, background, (744, 484), (0, 225))

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

    @commands.command(name='facts')
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def facts(self, ctx, *, text):
        async with ctx.typing():
            background = Image.open('imgsrc/facts.png')
            textarea = Image.new('RGBA', (344, 276), (0,0,0,0))
            font = ImageFont.truetype('fonts/facts.ttf', 32)
            d = ImageDraw.Draw(textarea)
            lines = textwrap.wrap(text, width=20)
            if len(lines) > 7:
                await ctx.send(':warning: Too much text! :warning:')
                return
            y_text = 38
            w = 322
            for line in lines:
                width, height = font.getsize(line)
                d.text(((w - width) / 2, y_text), line, font=font, fill=(0,0,0,255))
                y_text += height
            textarea = textarea.rotate(-16)
            image = self.picInPic(textarea, background, (344, 276), (10, 490))
            output = BytesIO()
            image.save(output, format="PNG")
            image = output.getvalue()
            output.close()
            await ctx.send(':white_check_mark: Done! :white_check_mark:', file=discord.File(BytesIO(image), filename='facts.png'))

def setup(bot):
    bot.add_cog(imagesCog(bot))
