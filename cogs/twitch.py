import discord
from discord.ext import commands
import requests
import json

class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.twitch_client_id = "c6ntn3sbtupd03nwe9qhlh2ek2at9d"
        self.twitch_authorization_key = "r26y5m85n32s1paqug9dgvc2qxkzy1"

    @commands.command(name="stream")
    async def stream(self, ctx, login):
        await ctx.send(requests.get(f'https://api.twitch.tv/helix/streams?user_login="{login}"',
                     headers=[f"Authorization: Bearer {self.twitch_authorization_key}", f"Client-Id: {self.twitch_client_id}"]).content.decode())


def setup(bot):
    bot.add_cog(twitch(bot))
