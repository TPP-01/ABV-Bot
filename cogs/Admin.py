import discord
from discord.ext import commands





class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_abv_or_manage_msg():
        async def predicate(ctx):
            return ctx.author.id == 550666880596049924 or ctx.author.id == 480026807580491798 or ctx.author.guild_permissions.manage_messages

        return commands.check(predicate)

    def is_abv_or_admin():
        async def predicate(ctx):
            return ctx.author.id == 550666880596049924 or ctx.author.id == 480026807580491798 or ctx.author.guild_permissions.administrator
        return commands.check(predicate)

    def is_abv_or_can_ban():
        async def predicate(ctx):
            return ctx.author.id == 550666880596049924 or ctx.author.id == 480026807580491798 or ctx.author.guild_permissions.ban_members
        return commands.check(predicate)

    @commands.command(name="ban", help="command to ban user")
    @is_abv_or_can_ban()
    async def ban(self,ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.message.delete()
            await ctx.channel.send(f'{member.name} has been banned from server'
                                   f'Reason: {reason}')
        except Exception:
            await ctx.channel.send(f"Bot doesn't have enough permission to ban someone. Upgrade the Permissions")

    @commands.command(name="unban", help="command to unban user")
    @is_abv_or_admin()
    async def unban(self,ctx, *, member_id: int):
        await ctx.guild.unban(discord.Object(id=member_id))
        await ctx.send(f"Unban {member_id}")

    @commands.command(name="purge", help="deletes spectifed number of messages ")
    @is_abv_or_manage_msg()
    async def purge(self, ctx, limit: int):
        if ctx.guild:
            deleted = await ctx.channel.purge(limit=limit)
            print(f"{ctx.channel} on {ctx.guild} was cleared")
        else:
            ctx.send("purge can only be run in servers")


    @commands.command(name="spam")
    @is_abv_or_admin()
    async def spam(self, ctx, times:int, content:str):
        for i in range(times):
            await ctx.send(f"{content}")







async def setup(bot):
    await bot.add_cog(admin(bot))