import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import ezcord


class Admin(ezcord.Cog, description="Befehle für Administratoren"):
    @slash_command(description="Kicke einen Member")
    @discord.default_permissions(administrator=True, kick_members=True)
    @discord.guild_only()
    async def kick(self, ctx, member: Option(discord.Member, "Wähle einen Member")):
        try:
            await member.kick()
        except discord.Forbidden:
            await ctx.respond("Ich habe keine Berechtigung, um diesen Member zu kicken", ephemeral=True)
            return
        await ctx.respond(f"{member.mention} wurde gekickt!", ephemeral=True)

    @slash_command(description="Banne einen Member")
    @discord.default_permissions(administrator=True, ban_members=True)
    @discord.guild_only()
    async def ban(self, ctx, member: Option(discord.Member, "Wähle einen Member")):
        try:
            await member.ban()
        except discord.Forbidden:
            await ctx.respond("Ich habe keine Berechtigung, um diesen Member zu bannen", ephemeral=True)
            return
        await ctx.respond(f"{member.mention} wurde gebannt!", ephemeral=True)

    @staticmethod
    def convert_time(seconds):
        if seconds < 60:
            return f"{round(seconds)} Sekunden"
        minutes = seconds / 60
        if minutes < 60:
            return f"{round(minutes)} Minuten"
        hours = minutes / 60
        return f"{round(hours)} Stunden"




def setup(bot):
    bot.add_cog(Admin(bot))