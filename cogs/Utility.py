import discord
from discord.ext import commands
import rki
import secrets
from github import Github
import platform
import psutil


class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    data = rki.get_daily_data()
    commands.Bot.data = data

    @commands.command(name="covid", aliases=["corona", "virus"])
    async def covid(self, ctx):
        embed = discord.Embed(title="Covid in Germany")
        embed.add_field(name="Neue Fälle DE", value=commands.Bot.data.get("cases"), inline=False)
        embed.add_field(name="Neue Todesfälle DE", value=commands.Bot.data.get("deaths"), inline=False)
        embed.add_field(name="7-Tages-Inzidenz DE", value=f'{commands.Bot.data.get("weekIncidence"):.2f}', inline=False)
        embed.set_footer(text="made by the ABV-Bot Development Team")
        await ctx.send(embed=embed, delete_after=30)
        if ctx.guild:
            await ctx.message.delete()


    @commands.command(name="bug")
    async def bug(self, ctx):
        g = Github(secrets.PAT_GH)
        await ctx.send("Sende nun bitte den Titel bzw eine Kurzbeschreibung des Bugs/Now please send the Title or a very very short description of your bug ")
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        message = await self.bot.wait_for("message", check=check)
        issue_title = message.content
        await ctx.send("Sende nun bitte die Beschreibung deines Bugs und wie man ihn erzeugt/Now please send the description of your bug and how to replicate it")
        message = await self.bot.wait_for("message", check=check)
        issue_body = message.content
        repo = g.get_repo("TPP-01/ABV-Bot")
        label = repo.get_label("bug_bot")
        repo.create_issue(title=issue_title,body=issue_body, labels=[label])
        embed = discord.Embed(title="Bug Issue was created", color = 0xff0000)
        embed.add_field(name="Title", value=issue_title, inline=False)
        embed.add_field(name="Body", value=issue_body, inline=True)
        await ctx.send(embed=embed)
    @commands.command(name="suggest", aliases=["sug", "idea"])
    async def suggest(self, ctx):
        g = Github(secrets.PAT_GH)
        await ctx.send(
            "Sende nun bitte den Titel bzw eine Kurzbeschreibung des Features das du vorschlagen möchtest/Now please send the Title or a very very short description of your feature that you want to suggest ")

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        message = await self.bot.wait_for("message", check=check)
        issue_title = message.content
        await ctx.send(
            "Sende nun bitte die ausführliche Beschreibung mit genauen Details/Now please send your feature and a detailed description of it ")
        message = await self.bot.wait_for("message", check=check)
        issue_body = message.content
        repo = g.get_repo("TPP-01/ABV-Bot")
        label = repo.get_label("suggestion_bot")
        repo.create_issue(title=issue_title, body=issue_body, labels=[label])
        embed = discord.Embed(title="Suggestion Issue was created", color=0xff0000)
        embed.add_field(name="Title", value=issue_title, inline=False)
        embed.add_field(name="Body", value=issue_body, inline=True)
        await ctx.send(embed=embed)


    @commands.command(name="info",aliases=["bot"])
    async def info(self, ctx):
        cpufreq = psutil.cpu_freq()
        embed = discord.Embed(title="Sys Info", color=0x0000f0)
        embed.add_field(name="Cores(Logical and Physical)", value=psutil.cpu_count(logical=True), inline=True)
        embed.add_field(name="Cpu Type", value=platform.processor(), inline=True)
        embed.add_field(name="CPU Freq", value=f"{cpufreq.current:.2f}Mhz", inline=True)
        embed.add_field(name="CPU Usage", value=f"{psutil.cpu_percent()}%", inline=True)
        embed.add_field(name="Ping", value=f"{round(self.bot.latency * 1000,2)}ms", inline=True)
        embed.set_footer(text="made by the ABV-Bot Development Team")
        await ctx.send(embed=embed)





















def setup(bot):
    bot.add_cog(utility(bot))