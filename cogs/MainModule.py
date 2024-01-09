import sys
import traceback
import discord
from discord.ext import commands

from configdir import config
from discord.ext import commands
from discord.commands import slash_command
import discord
import ezcord


class MainModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='coolbot', hidden=True)
    async def cool_bot(self, ctx):
        await ctx.respond('This bot is cool. :)')

    @slash_command(name='version', description='Shows bot and API version')
    async def version(self, ctx):
        await ctx.respond(f"Used discord.py version : {discord.__version__}, Bot version : {config.bot_version}")

    # @commands.command(name="help", help="well yk what help is, do you?")
    # async def help(self, ctx):
    #     embed = discord.Embed(title="Help", color=0xff2600)
    #     embed.add_field(name="Please visit our GitHub wiki for all comands",
    #                     value="https://github.com/TPP-01/ABV-Bot/wiki/Commands", inline=False)
    #     embed.set_footer(text="made by the ABV-Team")
    #     await ctx.respond(embed=embed)

    @commands.slash_command(name="msg", description="Write a DM to a use")
    async def msg(self, ctx, member: discord.Member, *, content):
        print(member)
        print(ctx.author)
        await member.send(content)
        if ctx.guild:
            await ctx.message.delete()

    # @commands.Cog.listener()
    # async def on_command(self,ctx):
    # logging.info(f"on {ctx.guild} in {ctx.channel} executed by {ctx.author} a command was executed")




def setup(bot):
    bot.add_cog(MainModule(bot))
