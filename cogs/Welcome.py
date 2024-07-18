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
#def sync_func(one, two, three=None):
    # do blocking stuff
    #return some_stuff

#async def async_func(whatever):
    # obtain one, two, three from somewhere?
    # supports args & kwargs
    #thing = functools.partial(sync_func, one, two, three=3)

    # run_in_executor supports passing args directly, e.g.
    # 'run_in_executor(None, func, one, two, three)' but using
    # partial makes stuff a bit easier to read if you have a
    # large amount of arguments you don't want to stack onto
    # a single line.
    #some_stuff = await bot.loop.run_in_executor(None, thing)

# WTF is this code lol

def setup(bot):
    bot.add_cog(Welcome(bot))