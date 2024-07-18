import sys
import traceback
import discord
from discord.ext import commands

from configdir import config

class MainModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(guild_ids=[760547427152560160, 1227685392602370088], name='coolbot', hidden=True)
    async def cool_bot(self, ctx):
        await ctx.respond('This bot is cool. :)')
    @commands.slash_command(guild_ids=[760547427152560160, 1227685392602370088], name="version")
    async def version(self, ctx):
        await ctx.respond(f"Used pycord version : {discord.__version__}, Bot version : {config.bot_version}")


    @commands.slash_command(guild_ids=[760547427152560160, 1227685392602370088], name="help", help="well yk what help is, do you?")
    async def help(self, ctx):
        embed = discord.Embed(title="Help", color=0xff2600)
        embed.add_field(name="Please visit our GitHub wiki for all comands",
                        value="https://github.com/TPP-01/ABV-Bot/wiki/Commands", inline=False)
        embed.set_footer(text="made by the ABV-Team")
        await ctx.respond(embed=embed)

# RIP msg command (removed bc it is built-in and could be abused)

    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, error):
    #
    #     if hasattr(ctx.command, 'on_error'):
    #         return
    #
    #     cog = ctx.cog
    #     if cog:
    #         if cog._get_overridden_method(cog.cog_command_error) is not None:
    #             return
    #
    #     ignored = ()
    #     error = getattr(error, 'original', error)
    #
    #     # Anything in ignored will return and prevent anything happening.
    #     if isinstance(error, ignored):
    #         return
    #     if isinstance(error, commands.CommandNotFound):
    #         await ctx.send("Der Command existiert nicht / the command was not found")
    #         if ctx.guild:
    #             await ctx.message.delete()
    #         #logging.warning(f"on {ctx.guild} in {ctx.channel} executed by {ctx.author} the following error oncurred [Command not found]")
    #
    #     elif isinstance(error, commands.DisabledCommand):
    #         await ctx.send(f'{ctx.command} has been disabled.')
    #
    #     elif isinstance(error, commands.NoPrivateMessage):
    #         try:
    #             await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
    #         except discord.HTTPException:
    #             pass
    #
    #     elif isinstance(error, commands.BadArgument):
    #         if ctx.command.qualified_name == 'tag list':
    #             await ctx.send('I could not find that member. Please try again.')
    #
    #     elif isinstance(error, commands.MissingRequiredArgument):
    #         print(error)
    #         await ctx.send(f"You forgot an argument: {error}")
    #
    #     elif isinstance(error, commands.MissingPermissions):
    #         await ctx.send(f"i have not enough permissions the following perms are missing: {error}. Please contact the Owner of this Server")
    #
    #     #elif isinstance(error, discord.errors.NotFound):
    #         #print("some404 error")
    #
    #
    #     else:
    #         # All other Errors not returned come here. And we can just print the default TraceBack.
    #         print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
    #         traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)



def setup(bot):
    bot.add_cog(MainModule(bot))
