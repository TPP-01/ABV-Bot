import discord
from discord.ext import commands
import lists
import random
commands.Bot.nsfwrouletteTasks = lists.nsfwroulette

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="nsfwroulette", aliases=["nsfrou"], help="Lets you do a random Task")
    @commands.is_nsfw()
    async def nsfwroulette(self,ctx):
        await ctx.send(f"{ctx.author.mention} you have to do the task : {random.choice(commands.Bot.nsfwrouletteTasks)}",delete_after=20)
        await ctx.message.delete()













def setup(bot):
    bot.add_cog(NSFW(bot))