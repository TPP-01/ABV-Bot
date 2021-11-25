import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    image = Image.open('assets/welcome_backgrnd2.jpg')
    draw = ImageDraw.Draw(image)


    #run_in_executor muss hier sein wg PIL welches nicht async ist dcpy schon
    # tut https://www.haptik.ai/tech/putting-text-on-image-using-python/




def setup(bot):
    bot.add_cog(Welcome(bot))