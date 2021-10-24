import discord
from discord.ext import commands
from pyowm import OWM

class MainModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='coolbot')
    async def cool_bot(self, ctx):
        """Is the bot cool?"""
        await ctx.send('This bot is cool. :)')


def setup(bot):
    bot.add_cog(MainModule(bot))