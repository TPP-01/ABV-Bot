import discord
from discord.ext import commands





class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban", help="command to ban user")
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.message.delete()
            await ctx.channel.send(f'{member.name} has been banned from server'
                                   f'Reason: {reason}')
        except Exception:
            await ctx.channel.send(f"Bot doesn't have enough permission to ban someone. Upgrade the Permissions")

    @commands.command(name="unban", help="command to unban user")
    @commands.has_permissions(administrator=True)
    async def unban(self,ctx, *, member_id: int):
        await ctx.guild.unban(discord.Object(id=member_id))
        await ctx.send(f"Unban {member_id}")

    @commands.command(name="purge", help="deletes spectifed number of messages ")
    @commands.has_permissions(manage_messages=True)
    async def purge(self,ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        print(f"{ctx.channel} on {ctx.guild} was cleared")
        await ctx.message.delete()






def setup(bot):
    bot.add_cog(admin(bot))