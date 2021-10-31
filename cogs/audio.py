import discord
from discord.ext import commands







class audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="play")
    async def play(self, ctx, song:int):
        await ctx.send("tbd")

    @commands.command(name="list_songs", aliases=["list"])
    async def list_songs(self, ctx):
        await ctx.send("tbd")









def setup(bot):
    bot.add_cog(audio(bot))