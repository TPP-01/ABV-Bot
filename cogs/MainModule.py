import discord
from discord.ext import commands
from pyowm import OWM
import config
class MainModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='coolbot', hidden=True)
    async def cool_bot(self, ctx):
        await ctx.send('This bot is cool. :)')
    @commands.command(name="version", help="shows the used discord.py version and the version of the bot")
    async def version(self, ctx):
        await ctx.send(f"Used discord.py version : {discord.__version__}, Bot version : {config.bot_version}")


def setup(bot):
    bot.add_cog(MainModule(bot))