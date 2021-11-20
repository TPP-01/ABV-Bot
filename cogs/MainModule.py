import sys
import traceback
import discord
from discord.ext import commands
import config

class MainModule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='coolbot', hidden=True)
    async def cool_bot(self, ctx):
        await ctx.send('This bot is cool. :)')
    @commands.command(name="version", help="shows the used discord.py version andtheversion of la bot", delete_after=60)
    async def version(self, ctx):
        await ctx.send(f"Used discord.py version : {discord.__version__}, Bot version : {config.bot_version}")


    @commands.command(name="help", help="well yk what help is do you?")
    async def help(self, ctx):
        embed = discord.Embed(title="Help", color=0xff2600)
        embed.add_field(name="Please visit our GitHub wiki for all comands",
                        value="https://github.com/TPP-01/ABV-Bot/wiki/Commands", inline=False)
        embed.set_footer(text="made by the ABV-Team")
        await ctx.send(embed=embed)

    @commands.command(name="msg")
    async def msg(self, ctx, member: discord.Member, *, content):
        print(member)
        await member.send(content)

    #@commands.Cog.listener()
    #async def on_command(self,ctx):
        #logging.info(f"on {ctx.guild} in {ctx.channel} executed by {ctx.author} a command was executed")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = ()
        error = getattr(error, 'original', error)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Der Command existiert nicht / the command was not found")
            #logging.warning(f"on {ctx.guild} in {ctx.channel} executed by {ctx.author} the following error oncurred [Command not found]")

        elif isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                await ctx.send('I could not find that member. Please try again.')

        elif isinstance(error, commands.MissingRequiredArgument):
            print(error)
            await ctx.send(f"You forgot an argument: {error}")

        elif isinstance(error, discord.errors.NotFound):
            print("some404 error")


        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)



def setup(bot):
    bot.add_cog(MainModule(bot))
