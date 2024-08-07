import discord
import os
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
            data = f.readlines()
            if data != []:
                for r in range(len(data)):
                    self.roles.append(data[r].replace("\n", "").split(","))
            f.close()
        return self.roles

    # deletes configuration of the channel
    def delconf(self, chid):
        os.remove(f"channels/{chid}")

    # saves the configuration
    def config(self):
        with open(f"channels/{self.channelid}", "w") as f:
            for role in self.roles:
                conf = ""
                for r in role:
                    conf = conf + r
                    if r == role[0]:
                        conf = conf + ","
                f.write(conf + "\n")
            f.close()

    # returns the role for a emoji
    def rolereturn(self, emoji, guild):
        for r in self.roles:
            if r[1] == emoji:
                ro = r[0]
        return discord.utils.get(guild.roles, name=ro)

    # initiates the name and channel


    @commands.slash_command(guild_ids=[760547427152560160, 1227685392602370088], name="roinit")
    async def roinit(self, ctx, arg):
        """
        Initialises a reaction role thingy
        """
        self.roles = []
        self.channelid = ctx.channel.id
        self.text = arg
        await ctx.respond("Init Done!")

    # adds the roles to the list


    @commands.slash_command(guild_ids=[760547427152560160, 1227685392602370088], name="roadd")
    async def roadd(self, ctx, role, emoji):
        """
        Adds a role and corresponding emoji to the reaction role modal
        """
        self.roles.append([role, emoji])
        await ctx.respond(f"Add \"{role},{emoji}\"")
    # deploys everything together
    @commands.slash_command(guild_ids=[760547427152560160, 1227685392602370088], name="rodeploy")
    async def rodeploy(self, ctx, delete_channel:str):
        """
        This command deploys the reaction role message and sets a channel to be purged
        """

        self.config()
        if delete_channel == "y" or delete_channel == "j":
            await ctx.channel.purge(limit=len(await ctx.channel.history().flatten()))
        #await ctx.channel.purge(limit=len(await ctx.channel.history().flatten()))
        msg = await ctx.channel.send(self.text)
        for emoji in self.emojireturn():
            await msg.add_reaction(emoji)



    # deletes reaction role conf of the channel and purges it
    @commands.slash_command(guild_ids=[760547427152560160, 1227685392602370088], name="rodelete")
    async def rodelete(self, ctx):
        """
        This Command purges the channel specified in the rodeploy command
        USE WITH CAUTION
        """
        await ctx.channel.purge(limit=len(await ctx.channel.history().flatten()))
        self.delconf(ctx.channel.id)

    # reaction listeners
    @commands.Cog.listener(name="on_raw_reaction_add")
    async def on_raw_reaction_add(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)

        try:
            self.getconf(payload.channel_id)
        except:
            pass

        for em in self.emojireturn():
            if str(em) == str(payload.emoji):
                if not user.bot:
                    await user.add_roles(self.rolereturn(em, guild))
                break

    @commands.Cog.listener(name="on_raw_reaction_remove")
    async def on_raw_reaction_remove(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)

        try:
            self.getconf(payload.channel_id)
        except:
            pass

        for em in self.emojireturn():
            if str(em) == str(payload.emoji):
                if not user.bot:
                    await user.remove_roles(self.rolereturn(em, guild))
                break


def setup(bot):
    bot.add_cog(ReactionRole(bot))
