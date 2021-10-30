import discord
from discord.ext import commands



class BotOwner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="leaveguild", description="leave server", hidden=True)
    @commands.is_owner()
    async def leaveguild(ctx):
        # to_leave = client.get_guild(arg1)
        # await to_leave.leave()
        # await message.server.leave()
        await ctx.guild.leave()
        print(f"left server: {ctx.guild}")


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





def setup(bot):
    bot.add_cog(BotOwner(bot))