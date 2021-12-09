import discord

from discord.commands import slash_command
from discord.ext import commands


class slashtest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[760547427152560160])
    async def hi(self, ctx):
        await ctx.respond("Hi, this is a slash command from a cog!")


def setup(bot):
    bot.add_cog(slashtest(bot))