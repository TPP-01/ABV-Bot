from discord.ext import commands
from discord.commands import slash_command
import discord
from pyowm import OWM
import ezcord


owm = OWM('05a07849f4d10547a2894eefb2b3c23f')
mgr = owm.weather_manager()


class Wetter(ezcord.Cog):
    def __init__(self, bot):
        self.bot = bot


    @slash_command(description="zeigt das Wetter an einem Ort an")
    async def wetter(self, ctx, ort):
        observation = mgr.weather_at_place(str(ort))
        w = observation.weather
        hum_var = w.humidity
        weather_var = w.temperature('celsius')
        embed = discord.Embed(title="Wetter aktuell")
        embed.add_field(name=f"Maximale Temperatur in {ort}", value=f'{weather_var["temp_max"]}°C', inline=False)
        embed.add_field(name=f"Aktuelle Temperatur in {ort}", value=f'{weather_var["temp"]}°C', inline=False)
        embed.add_field(name=f"Aktuelle Luftfeuchtigkeit in {ort}", value=hum_var, inline=False)
        embed.add_field(name="Aktuelles Wetter (zusammengefasst)", value=w.detailed_status, inline=True)
        embed.set_footer(text="made by blockcrafter#5759")

        await ctx.respond(embed=embed, delete_after=60)


def setup(bot):
    bot.add_cog(Wetter(bot))