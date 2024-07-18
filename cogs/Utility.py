import discord
from discord.ext import commands
from custom_modules import rki
import secrets
from github import Github
import platform
import psutil


class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    data = rki.get_daily_data()
    commands.Bot.data = data
    #
    @commands.slash_command(guild_ids = [760547427152560160, 1227685392602370088], name="covid", aliases=["corona", "virus"])
    async def covid(self, ctx):
        """
        Shows current data from the RKI
        """
        embed = discord.Embed(title="Covid in Germany")
        embed.add_field(name="Neue Fälle DE", value=commands.Bot.data.get("cases"), inline=False)
        embed.add_field(name="Neue Todesfälle DE", value=commands.Bot.data.get("deaths"), inline=False)
        embed.add_field(name="7-Tages-Inzidenz DE", value=f'{commands.Bot.data.get("weekIncidence"):.2f}', inline=False)
        embed.set_footer(text="made by the ABV-Bot Development Team")
        await ctx.send(embed=embed, delete_after=30)
        if ctx.guild:
            await ctx.message.delete()


# RIP suggest and bug commands, you were very unsafe


    @commands.slash_command(guild_ids = [760547427152560160, 1227685392602370088], name="info",aliases=["bot"])
    async def info(self, ctx):
        """
        Shows basic system information
        """
        cpufreq = psutil.cpu_freq()
        embed = discord.Embed(title="Sys Info", color=0x0000f0)
        embed.add_field(name="Cores(Logical and Physical)", value=psutil.cpu_count(logical=True), inline=True)
        embed.add_field(name="Cpu Type", value=platform.processor(), inline=True)
        embed.add_field(name="CPU Freq", value=f"{cpufreq.current:.2f}Mhz", inline=True)
        embed.add_field(name="CPU Usage", value=f"{psutil.cpu_percent()}%", inline=True)
        embed.add_field(name="Ping", value=f"{round(self.bot.latency * 1000,2)}ms", inline=True)
        embed.set_footer(text="made by the ABV-Bot Development Team")
        await ctx.respond(embed=embed)





















def setup(bot):
    bot.add_cog(utility(bot))