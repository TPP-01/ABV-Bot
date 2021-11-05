import discord
from discord.ext import commands


class ReactionRole(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.roles = []
        self._rep = lambda x: x.replace("'", "").replace("[", "").replace("]", "").replace("\n", "").replace(" ", "").split(",")  # xD Hat jemand eine bessere Lösung?

    # returns the emojis of the roles
    def emojireturn(self):
        emojis = []
        for role in self.roles:
            emojis.append(role[1])
        return emojis

    def getconf(self, chid):
        self.roles = []
        with open(f"channels/{chid}", "r") as f:
            _data = f.readlines()
            if _data != [] and int(chid) == int(_data[0]):
                for r in range(len(_data)):
                    self.roles.append(self._rep(_data[r]))
            f.close()
        return self.roles

    def config(self):
        with open(f"channels/{self.channelid}", "w") as f:
            for role in self.roles:
                f.write(str(role) + "\n")
            f.close()

    # returns the role for a emoji
    def rolereturn(self, emoji):
        for r in self.roles:
            if r[1] == emoji:
                ro = r[0]
        return ro

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
        self.getconf(payload.channel_id)

        if int(payload.channel_id) == int(self.channelid):
            for self.em in self.emojireturn():
                if str(self.em) == str(payload.emoji):
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
        self.getconf(payload.channel_id)

        if int(payload.channel_id) == int(self.channelid):
            for self.em in self.emojireturn():
                if str(self.em) == str(payload.emoji):
                    self.roget = discord.utils.get(self.guild.roles, name=self.rolereturn(self.em))
                    if not self.user.bot:
                        await self.user.remove_roles(self.roget)
                    break


def setup(bot):
    bot.add_cog(ReactionRole(bot))
