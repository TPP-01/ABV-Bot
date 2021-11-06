import discord
from discord.ext import commands


class ReactionRole(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.roles = []

    # returns the emojis of the roles
    def emojireturn(self):
        emojis = []
        for role in self.roles:
            emojis.append(role[1])
        return emojis

    # gets the configuration of the channel
    def getconf(self, chid):
        self.roles = []
        with open(f"channels/{chid}", "r") as f:
            _data = f.readlines()
            if _data != []:
                for r in range(len(_data)):
                    self.roles.append(_data[r].split(","))
            f.close()
        return self.roles

    # saves the configuration
    def config(self):
        with open(f"channels/{self.channelid}", "w") as f:
            for role in self.roles:
                for r in role:
                    conf = r
                    if r == role[0]:
                        conf = conf + ","
                f.write(conf + "\n")
            f.close()

    # returns the role for a emoji
    def rolereturn(self, emoji):
        for r in self.roles:
            if r[1] == emoji:
                ro = r[0]
        return discord.utils.get(guild.roles, name=ro)

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
        channel = self.bot.get_channel(payload.channel_id)
        guild = self.bot.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)
        message = await channel.fetch_message(payload.message_id)

        try:
            self.getconf(payload.channel_id)
        except:
            pass

        for em in self.emojireturn():
            if str(em) == str(payload.emoji):
                if not user.bot:
                    await user.add_roles(self.rolereturn(em))
                break

    @commands.Cog.listener(name="on_raw_reaction_remove")
    async def on_raw_reaction_remove(self, payload):
        channel = self.bot.get_channel(payload.channel_id)
        guild = self.bot.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)
        message = await channel.fetch_message(payload.message_id)

        try:
            self.getconf(payload.channel_id)
        except:
            pass

        for em in self.emojireturn():
            if str(em) == str(payload.emoji):
                if not user.bot:
                    await user.remove_roles(self.rolereturn(em))
                break


def setup(bot):
    bot.add_cog(ReactionRole(bot))
