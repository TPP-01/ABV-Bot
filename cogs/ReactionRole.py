import configparser
import time

import discord
from discord.ext import commands


class ReactionRole(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.conf = configparser.ConfigParser()
        self.conf.read("rorole.conf")
        try:
            self.roles = self.conf.items("roles")
            for self.role in self.roles:
                self.swap = self.role[0]
                self.role[0] = self.role[1]
                self.role[1] = self.swap
            print("Roles loaded")
        except:
            print("Role load Error")

        self.channelid = self.conf.get("channel", "channelid")
        #print(f"Debug: {self.roles}, {self.channelid} {self.rolereturn(self.roles[0][1])}")

    def roconfig(self, mode="w"):
        if mode == "w":
            self.roledic = {}
            for self.role in self.roles:
                self.roledic[self.role[1]] = self.role[0]
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

    def emojiiter(self, ctx, emname):
        for self.emoji in ctx.guild.emojis:
            if self.emoji.name == emname:
                return self.emoji
                break

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
        self.args[1] = self.args[1].replace("\\", "")
        self.roles.append(self.args)
        await ctx.send(f"Add \"{self.args}\" ")

    # deploys everything together
    @commands.command(name="rodeploy")
    async def rodeploy(self, ctx):
        self.roconfig()
        await self.channel.purge(limit=len(await ctx.channel.history().flatten()))
        await ctx.send(self.emojireturn())
        self.msg = await self.channel.send(self.text)
        for self.emoji in self.emojireturn():
            await self.msg.add_reaction(self.emojiiter(ctx, self.emoji))

    # reaction listeners
    @commands.Cog.listener(name="on_raw_reaction_add")
    async def on_raw_reaction_add(self, payload):
        self.channel = self.bot.get_channel(payload.channel_id)
        self.guild = self.bot.get_guild(payload.guild_id)
        self.user = self.guild.get_member(payload.user_id)
        self.message = await self.channel.fetch_message(payload.message_id)

        print("Debug: on_reaction_add")
        await self.message.channel.send(f"Debug: on_reaction_add: {payload.channel_id} {self.channelid} {self.emojireturn()} {payload.emoji} {self.user.name} {self.rolereturn(payload.emoji)}")

        if int(payload.channel_id) == int(self.channelid):
            await self.message.channel.send(f"Debug: on_channel_check: Check True!")
            for self.em in self.emojireturn():
                await self.message.channel.send(f"Debug: on_emoji_return: {self.em}")
                if str(self.em) == str(payload.emoji.name):
                    self.roget = discord.utils.get(self.guild.roles, name=self.rolereturn(self.em))
                    if not self.user.bot:
                        await self.user.add_roles(self.roget)
                    break

    @commands.Cog.listener(name="on_raw_reaction_remove")
    async def on_raw_reaction_remove(self, payload):
        self.channel = self.bot.get_channel(payload.channel_id)
        self.guild = self.bot.get_guild(payload.guild_id)
        self.user = self.guild.get_member(payload.user_id)
        self.message = await self.channel.fetch_message(payload.message_id)

        if payload.channel_id == self.channelid:
            for self.em in self.emojireturn():
                if payload.emoji == self.em:
                    self.roget = discord.utils.get(self.user.guild.roles, name=self.rolereturn(self.em))
                    if not self.user.bot:
                        self.user.remove_role(self.roget)
                    break


def setup(bot):
    time.sleep(5)
    bot.add_cog(ReactionRole(bot))
