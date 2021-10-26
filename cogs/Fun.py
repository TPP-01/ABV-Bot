import discord
from discord.ext import commands

import lists

commands.Bot.wop_questions = lists.warheitoderpflicht

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="blame", help="Blamed einen User mit dem angegebenen Grund")
    async def blame(ctx, arg1, arg2):
        username = ctx.message.author.name
        await ctx.send(f"{ctx.author.mention} blamed {arg1} for {arg2}", delete_after=30)
        await ctx.message.delete()#

    @commands.command(name="wahrheitoderpflicht", aliases=["wop"], help="SFW warheit oder pflicht")
    async def wahrheitoderpflicht(self, ctx):
        await ctx.send(
            f"{ctx.author.mention} you have to do the task : {random.choice(commands.Bot.wop_questions)}",delete_after=20)
        await ctx.message.delete()



    @commands.command(name="slap", help="now you can slap peaple")
    async def slap(self, ctx, user_to_be_slapped: discord.Member):
        if ctx.author == user_to_be_slapped:
            await ctx.send(f"{ctx.author.mention} was dumb and slapped himself", delete_after=20)
            await ctx.send("https://tenor.com/bd1Da.gif", delete_after=20)
        else:
            await ctx.send(f"{ctx.author.mention} slapped {user_to_be_slapped.mention}", delete_after=20)
            await ctx.send("https://tenor.com/bd1Da.gif", delete_after=20)
        await ctx.message.delete()














def setup(bot):
    bot.add_cog(Fun(bot))