import configparser
import time

import discord
from discord.ext import commands


class ReactionRole(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.conf = configparser.ConfigParser()
        self.conf.read("rorole.conf")
        self.roles = self.conf.items("roles")
        self.channelid = self.conf.get("channel", "channelid")
        print(f"Debug: {self.roles}, {self.channelid}")

    def roconfig(self, mode="w"):
        if mode == "w":
            self.roledic = {}
            for self.role in self.roles:
                self.roledic[self.role[0]] = self.role[1]
            self.conf["roles"] = self.roledic
            self.conf["channel"] = {"channelid": self.channelid}
            with open("rorole.conf", "w") as file:
                self.conf.write(file)

    # returns the emojis of the roles
    def emojireturn(self):
        self.emojis = []
        for self.role in self.roles:
            self.emojis.append(self.role[1])
        return self.emojis

    # returns the role for a emoji
    def rolereturn(self, emoji):
        self.r = ""
        self.ro = ""
        for self.r in self.roles:
            if self.r[1] == emoji:
                self.ro = self.r[0]
        return self.ro

    # initiates the name and channel
    @commands.command(name="roinit")
    async def roinit(self, ctx, arg):
        self.roles = []
        self.channel = ctx.channel
        self.channelid = ctx.channel.id
        self.text = arg
        try:
            await self.msg.delete()
        except:
            print("First init this session")
        await ctx.send("Init Done!")

    # adds the roles to the list
    @commands.command(name="roadd")
    async def roadd(self, ctx, arg):
        self.args = arg.split(",")
        self.roles.append(self.args)
        await ctx.send(f"Add \"{self.args}\" ")

    # deploys everything together
    @commands.command(name="rodeploy")
    async def rodeploy(self, ctx):
        self.roconfig()
        await self.channel.purge(limit=len(await ctx.channel.history().flatten()))
        self.msg = await self.channel.send(self.text)
        for self.emoji in self.emojireturn():
            await self.msg.add_reaction(self.emoji)

    # reaction listeners
    @commands.Cog.listener(name="on_reaction_add")
    async def on_reaction_add(self, reaction, user):
        reaction.message.channel.send("Debug: on_reaction_add")
        if reaction.message.channel.id == self.channelid:
            for self.em in self.emojireturn():
                if reaction.emoji == self.em:
                    self.roget = discord.utils.get(user.guild.roles, name=self.rolereturn(self.em))
                    break
            if not user.bot:
                await user.add_roles(self.roget)

    @commands.Cog.listener(name="on_reaction_remove")
    async def on_reaction_remove(self, reaction, user):
        if reaction.message.channel.id == self.channelid:
            for self.em in self.emojireturn():
                if reaction.emoji == self.em:
                    self.roget = discord.utils.get(user.guild.roles, name=self.rolereturn(self.em))
                    break
            if not user.bot:
                await user.remove_roles(self.roget)


def setup(bot):
    time.sleep(5)
    bot.add_cog(ReactionRole(bot))
