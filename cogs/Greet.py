from discord.ext import commands
from discord.commands import slash_command
import discord
import ezcord

class Greet(ezcord.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Begrüßungsnachricht erstellen
        embed = discord.Embed(
            title="Willkommen",
            description=f" Herzlich Willkommen auf dem Server {member.mention} \nSchau dir bitte die <#709707058882150460> an. ^^",
            color=discord.Color.blue(),  # random Color aus ner Liste mit verschiedenen Farben wär nice :D

        )
        embed.set_thumbnail(url=member.display_avatar.url)
        # Den Kanal mit der angegebenen ID abrufen und die Begrüßungsnachricht senden
        channel = await self.bot.fetch_channel(709475684560404515)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Greet(bot))