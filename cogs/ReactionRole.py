import discord
from discord.ext import commands

class ReactionRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    def emojireturn(self):
        self.emojis = []
        for self.role in self.roles:
            self.emojis.append(self.role[1])
        return self.emojis

    def rolereturn(self, emoji):
        self.r = ""
        self.ro = ""
        for self.r in self.roles:
            if self.r[1] == emoji:
                self.ro = self.r[0]
        return self.ro

    @commands.command(name="roinit")
    async def roinit(self, ctx, arg):
        self.roles = []
        self.channel = ctx.channel
        self.channelid = ctx.channel.id
        self.text = arg
        await ctx.send("Init Done!")

    @commands.command(name="roadd")
    async def roadd(self, ctx, arg):
        self.args = arg.split(",")
        self.roles.append(self.args)
        await ctx.send(f"Add \"{self.args}\" ")

    @commands.command(name="rodeploy")
    async def rodeploy(self, ctx):
        await ctx.channel.purge()
        self.msg = await self.channel.send(self.text)
        for self.emoji in self.emojireturn():
            await self.msg.add_reaction(self.emoji)

    @commands.Cog.listener(name="on_reaction_add")
    async def on_reaction_add(self, reaction, user):
        if reaction.message.channel.id == self.channelid:
            for self.em in self.emojireturn():
                if reaction.emoji == self.em:
                    self.roget = discord.utils.get(user.guild.roles, name=self.rolereturn(self.em))
                    break
            if not user.bot:
                await user.add_roles(self.roget)

def setup(bot):
    bot.add_cog(ReactionRole(bot))