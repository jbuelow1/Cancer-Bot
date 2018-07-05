from discord.ext import commands
import discord

import requests

class imagestestCog:
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

    @commands.command(name='findimages', hidden=True)
    async def test_images(self, ctx):
        async with ctx.typing():
            print('Collecting images from invoke message...')
            #images = self.getImages(ctx.message)
            images = []
            if images == []:
                print('No images found in invoke message. Searching history...')
                channel = ctx.message.channel
                messages = await channel.history(limit=25).flatten()
                print(str(messages[0].attachments))
                for message in messages:
                    print('Searching a message from history...')
                    #print('Searching message #' + str(message.id) + ' by ' + str(message.author))
                    images = self.getImages(message)
                    if not images == []:
                        #print('Images found in message #' + str(message.id) + ' by ' + str(message.author))
                        print('breaking')
                        break
            filenum = 0
            print('Converting images...')
            for image in images:
                print('Converting image #' + str(filenum) + '...')
                output = BytesIO()
                image.save(output, format="PNG")
                image = output.getvalue()
                output.close()
                outputImages.append(discord.File(BytesIO(image), filename='jpeg' + str(filenum) + '.png'))
                filenum += 1
            print('Sending images...')
            await ctx.send(':white_check_mark: Done! :white_check_mark:', files=outputImages)

def setup(bot):
    bot.add_cog(imagestestCog(bot))
