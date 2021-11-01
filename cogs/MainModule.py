import sys
import traceback
import logging
import discord
from discord.ext import commands
from pyowm import OWM
import config

def roleconf(messageid, zeichen, role):
    with open("../abv.conf", "a") as conf:
        conf.write("[]\n"+messageid)
        for z in range(len(zeichen)):
            conf.write(f"{zeichen[z]},{role[z]}")

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
        embed = discord.Embed(title="HELP (fun module)",description="help ah wait we cant help you anymore (btw prefix is = )", color=0xff0000)
        embed.add_field(name="blame [user]", value="blames someone", inline=False)
        embed.add_field(name="slap [user]", value="slaps someone", inline=False)
        embed.add_field(name="wahrheitoderpflicht", value="wahrheit oder pflicht", inline=False)
        embed.set_footer(text="made with hate by blockcrafter#5759")
        await ctx.send(embed=embed, delete_after=60)

        embed = discord.Embed(title="Help utility", color=0xff2600)
        embed.add_field(name="covid", value="gibt die aktuelle Coronazahlen in DE wieder", inline=False)
        embed.set_footer(text="made by blockcrafter#5759")
        await ctx.send(embed=embed)

        embed = discord.Embed(title="Help Admin Modul", color=0xff2600)
        embed.add_field(name="ban [member] [reason]", value="bannt einen user", inline=False)
        embed.add_field(name="unban [member][reason]", value="entmannt einen user", inline=True)
        embed.set_footer(text="made by blockcrafter#5759")
        await ctx.send(embed=embed)

    @commands.command(name="msg")
    async def msg(self, ctx, member: discord.Member, *, content):
        print(member)
        await member.send(content)
        print(ctx.command.qualified_name.main.main.main.main.main.main.main.main.main.main.main.main.main.main.main.main.main.main.main.main.main.main.main.main.main())

    @commands.command(name="roinit", help="text,role role,🐍🐍")
    async def msg(self, ctx, msgID: int, content):
        content = content.split(",")
        text = content[0]
        roles = content[1].split(" ")
        zeichen = content[2]
        roleconf(msgID, zeichen, roles)
        ask = await ctx.send(text)
        for z in zeichen:
            await ctx.add_reaction(ask, emoji=z)
        await ctx.delete()



    #@commands.Cog.listener()
    #async def on_command(self,ctx):
        #logging.info(f"on {ctx.guild} in {ctx.channel} executed by {ctx.author} a command was executed")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """

        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        # This prevents any cogs with an overwritten cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = ()

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
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

        # For this error example we check to see where it came from...
        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':  # Check if the command being invoked is 'tag list'
                await ctx.send('I could not find that member. Please try again.')

        elif isinstance(error, discord.errors.NotFound):
            print("some404 error")


        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)





def setup(bot):
    bot.add_cog(MainModule(bot))