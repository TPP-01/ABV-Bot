import asyncio

import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import ezcord


class BotOwner(ezcord.Cog):
    def __init__(self, bot):
        self.bot = bot



    @slash_command(description="makes bot go shutdown")
    @commands.is_owner()
    async def exit(self, ctx):
        await ctx.respond("the bot will be shutdown on all servers in 5 sec", delete_after=1)
        if ctx.guild:
            await ctx.message.delete()
        await asyncio.sleep(5)
        exit(0)
        







def setup(bot):
    bot.add_cog(BotOwner(bot))
