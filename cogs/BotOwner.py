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
            if ctx.guild:
                await ctx.message.delete()
        else:
            await ctx.send('**`SUCCESS`**')
            if ctx.guild:
                await ctx.message.delete()

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            if ctx.guild:
                await ctx.message.delete()
        else:
            await ctx.send('**`SUCCESS`**')
            if ctx.guild:
                await ctx.message.delete()

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            if ctx.guild:
                await ctx.message.delete()
        else:
            await ctx.send('**`SUCCESS`**')
            if ctx.guild:
                await ctx.message.delete()

    @commands.command(name="exit", hidden=True, aliases=["shutdown", "poweroff"])
    @commands.is_owner()
    async def exit(self, ctx):
        await ctx.send("the bot will be shutdown on all servers in 5 sec", delete_after=1)
        if ctx.guild:
            await ctx.message.delete()
        await asyncio.sleep(5)
        exit(0)
        







def setup(bot):
    bot.add_cog(BotOwner(bot))
