import discord
from discord.ext import commands
import random
from configdir import lists
from discord.ext import commands
from discord.commands import slash_command
import discord
import ezcord



class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @slash_command(description="U can slap people")
    async def slap(self, ctx, user_to_be_slapped: discord.Member):
        if ctx.author == user_to_be_slapped:
            await ctx.respond(f"{ctx.author.mention} was dumb and slapped himself", delete_after=20)
            await ctx.respond("https://tenor.com/bd1Da.gif", delete_after=20)
        else:
            await ctx.respond(f"{ctx.author.mention} slapped {user_to_be_slapped.mention}", delete_after=20)
            await ctx.respond("https://tenor.com/bd1Da.gif", delete_after=20)



    @slash_command(name="lapogusamogus", aliases=["amogus", "lapog", "sus"], hidden=True)
    async def lapogusamogus(self, ctx, user_to_sus: discord.Member=None):
        if user_to_sus is not None:
            await ctx.respond(f"{user_to_sus.mention} is now a lapogusamogus")
            await ctx.respond("https://tenor.com/view/19dollar-fortnite-card-among-us-amogus-sus-red-among-sus-gif-20549014")

        else:
            await ctx.respond(f"{ctx.author.mention} is now a lapogusamogus")
            await ctx.respond("https://tenor.com/view/19dollar-fortnite-card-among-us-amogus-sus-red-among-sus-gif-20549014")


def setup(bot):
    bot.add_cog(Fun(bot))
