from discord.ext import commands
from configdir import lists
import random
commands.Bot.nsfw_wop_questions = lists.nsfw_wop_questions
commands.Bot.nsfw_wop_tasks = lists.nsfw_wop_tasks

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="nsfwwop", help="NSFW warheit oder pflicht")
    @commands.is_nsfw()
    @commands.guild_only()
    async def nsfwwop(self,ctx):
        truth_items = commands.Bot.nsfw_wop_questions
        dare_items = commands.Bot.nsfw_wop_tasks
        await ctx.send("ACHTUNG DIESE AUFGABEN UND FRAGEN KÖNNEN VERSTÖREND SEIN", delete_after=30)
        await ctx.send("please type t for truth and d for dare, bitte schreibe t für wahrheit und d für pflicht", delete_after=30)

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ("t", "d")

        message = await self.bot.wait_for("message", check=check)
        choice = message.content.lower()
        if choice == "t":
            await ctx.send(f"{random.choice(truth_items)}", delete_after=30)
        if choice == "d":
            await ctx.send(f"{random.choice(dare_items)}", delete_after=30)
        #await ctx.send(f"{ctx.author.mention} you have to do the task : {random.choice(commands.Bot.nsfwrouletteTasks)}",delete_after=20)
        #await ctx.message.delete()













def setup(bot):
    bot.add_cog(NSFW(bot))