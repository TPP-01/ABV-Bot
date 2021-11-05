import time

import discord
from discord.ext import commands


class ReactionRole(commands.Cog):

    def __init__(self, bot):
        try:
            with open("rorole.conf", "r") as f:
                self._data = f.readlines
                if self._data != [] or self._data != None:
                    self.channelid = int(self._data[0])
                    for self.r in range(len(1, len(self._data))):
                        self.roles.append(list(self._data[self.r]))
                else:
                    print("No Data loaded")
                f.close()
        except:
            print("No Data loaded")

        self.bot = bot
        #print(f"Debug: {self.roles}, {self.channelid} {self.rolereturn(self.roles[0][1])}")

    # returns the emojis of the roles
    def emojireturn(self):
        self.emojis = []
        for self.role in self.roles:
            self.emojis.append(self.role[1])
        return self.emojis

    def config(self):
        with open("rorole.conf", "w") as f:
            f.write(str(self.channelid)+"\n")
            for self.role in self.roles:
                f.write(str(self.role)+"\n")
            f.close()

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
        self.args[1] = self.args[1].replace("\\", "")
        self.roles.append(self.args)
        await ctx.send(f"Add \"{self.args}\" ")

    # deploys everything together
    @commands.command(name="rodeploy")
    async def rodeploy(self, ctx):
        self.config()
        await self.channel.purge(limit=len(await ctx.channel.history().flatten()))
        await ctx.send(self.emojireturn())
        self.msg = await self.channel.send(self.text)
        for self.emoji in self.emojireturn():
            await self.msg.add_reaction(self.emoji)

    # reaction listeners
    @commands.Cog.listener(name="on_raw_reaction_add")
    async def on_raw_reaction_add(self, payload):
        self.channel = self.bot.get_channel(payload.channel_id)
        self.guild = self.bot.get_guild(payload.guild_id)
        self.user = self.guild.get_member(payload.user_id)
        self.message = await self.channel.fetch_message(payload.message_id)

        print("Debug: on_reaction_add")
        await self.message.channel.send(f"Debug: on_reaction_add: {payload.channel_id} {self.channelid} {self.emojireturn()} {payload.emoji.name} {self.user.name} {self.rolereturn(payload.emoji)}")

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
