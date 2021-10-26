import discord
from discord.ext import commands
from pyowm import OWM
import config
class MainModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='coolbot', hidden=True)
    async def cool_bot(self, ctx):
        await ctx.send('This bot is cool. :)')
    @commands.command(name="version", help="shows the used discord.py version andtheversion of la bot", delete_after=60)
    async def version(self, ctx):
        await ctx.send(f"Used discord.py version : {discord.__version__}, Bot version : {config.bot_version}")
    @commands.command(name="help", help="well yk what help is do you?")
    async def help(self, ctx):
        embed = discord.Embed(title="HELP (fun module)",description="help ah wait we cant help you anymore (btw prefix is = )", color=0xff0000)
        embed.add_field(name="blame [user]", value="blames someone", inline=False)
        embed.add_field(name="slap [user]", value="slaps someone", inline=False)
        embed.add_field(name="wahrheitoderpflicht", value="wahrheit oder pflicht", inline=False)
        embed.add_field(name="undefined", value="undefined", inline=False)
        embed.set_footer(text="made with hate by blockcrafter#5759")
        await ctx.send(embed=embed, delete_after=60)




def setup(bot):
    bot.add_cog(MainModule(bot))