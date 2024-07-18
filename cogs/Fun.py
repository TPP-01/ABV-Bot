import discord
from discord.ext import commands
import random



class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[760547427152560160, 1227685392602370088], name="slap",
                            help="now you can slap peaple")
    async def slap(self, ctx, user_to_be_slapped: discord.Member):
        if ctx.author == user_to_be_slapped:
            await ctx.respond(f"{ctx.author.mention} was dumb and slapped themselves", delete_after=20)
            await ctx.send("https://tenor.com/bd1Da.gif", delete_after=20)
        else:
            await ctx.respond(f"{ctx.author.mention} slapped {user_to_be_slapped.mention}", delete_after=20)
            await ctx.send("https://tenor.com/bd1Da.gif", delete_after=20)


# RIP lapogusamongus command


def setup(bot):
    bot.add_cog(Fun(bot))
