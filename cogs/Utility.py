import discord
from discord.ext import commands
import rki
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
        await ctx.message.delete()

















def setup(bot):
    bot.add_cog(utility(bot))