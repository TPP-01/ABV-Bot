import discord
from discord.ext import commands
from pyowm import OWM

owm = OWM('05a07849f4d10547a2894eefb2b3c23f')
mgr = owm.weather_manager()

class Wetter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Wetter", aliases=["wetter"], description="zeig das wetter an",help="Gibt Wetterinformationen zum angegebenen ort aus")
    async def wetter(ctx, Ort):
        observation = mgr.weather_at_place(str(Ort))
        w = observation.weather
        hum_var = w.humidity
        weather_var = w.temperature('celsius')
        weather_var["temp_max"]
        embed = discord.Embed(title="Wetter aktuell")
        embed.add_field(name=f"Maximale Temperatur in {Ort}", value=weather_var["temp_max"], inline=False)
        embed.add_field(name=f"Aktuelle Temperatur in {Ort}", value=weather_var["temp"], inline=False)
        embed.add_field(name=f"Aktuelle Luftfeuchtigkeit in {Ort}", value=hum_var, inline=False)
        embed.add_field(name="Aktuelles Wetter (zusammengefasst)", value=w.detailed_status, inline=True)
        embed.set_footer(text="made by blockcrafter#5759")
        await ctx.send(embed=embed, delete_after=30)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Wetter(bot))