from discord.ext import commands
import discord

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
        await message.channel.history(limit=25).flatten()
        for testMessage in messages:
            for attachment in testMessage.attachments:
                if os.path.splitext(attachment.filename)[1].lower() in ('.png', '.jpg', '.jpeg', '.bmp'):
                    image_request_result = requests.get(attachment.url)
                    image = Image.open(BytesIO(image_request_result.content))
                    images.append(image)
            if not images == []:
                break
        ctx.send(str(images))
        return images

    def filler():
        print('this most certainly should not have been run!')

    @commands.command(name='findimages', hidden=True)
    async def test_images(self, ctx):
        async with ctx.typing():
            images = self.getImages(ctx.message)
            for image in images:
                output = BytesIO()
                image.save(output, format="PNG")
                image = output.getvalue()
                output.close()
                outputImages.append(discord.File(BytesIO(image), filename='jpeg' + str(filenum) + '.png'))
                filenum += 1
            await ctx.send(':white_check_mark: Done! :white_check_mark:', files=outputImages)

def setup(bot):
    bot.add_cog(imagestestCog(bot))
