import discord
from discord.ext import commands



class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="blame", help="Blamed einen User mit dem angegebenen Grund")
    async def blame(ctx, arg1, arg2):
        username = ctx.message.author.name
        await ctx.send(f"{ctx.author.mention} blamed {arg1} for {arg2}", delete_after=30)
        await ctx.message.delete()














def setup(bot):
    bot.add_cog(Fun(bot))