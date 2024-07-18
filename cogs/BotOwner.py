import asyncio

import discord
from discord.ext import commands
from discord.utils import get


class BotOwner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[760547427152560160, 1227685392602370088], name="leaveguild",
                            description="leave server", hidden=True)
    @commands.is_owner()
    async def leaveguild(self, ctx):
        # to_leave = client.get_guild(arg1)
        # await to_leave.leave()
        # await message.server.leave()
        print(f"left server: {ctx.guild}")
        await ctx.guild.leave()

    @commands.slash_command(guild_ids=[760547427152560160, 1227685392602370088], name='load', hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.respond(f'**`ERROR:`** {type(e).__name__} - {e}', ephemeral=True)

        else:
            await ctx.respond('**`SUCCESS`**', ephemeral=True)


    @commands.slash_command(guild_ids = [760547427152560160, 1227685392602370088], name='unload', hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.respond(f'**`ERROR:`** {type(e).__name__} - {e}', ephemeral=True)

        else:
            await ctx.respond('**`SUCCESS`**', ephemeral=True)


    @commands.slash_command(guild_ids = [760547427152560160, 1227685392602370088], name='reload', hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.respond(f'**`ERROR:`** {type(e).__name__} - {e}', ephemeral=True)

        else:
            await ctx.respond('**`SUCCESS`**', ephemeral=True)

    @commands.command(name="exit", hidden=True, aliases=["shutdown", "poweroff"])
    @commands.is_owner()
    async def exit(self, ctx):
        await ctx.respond("the bot will shutdown on all servers in 5 sec")
        await asyncio.sleep(5)
        exit(0)


def setup(bot):
    bot.add_cog(BotOwner(bot))
