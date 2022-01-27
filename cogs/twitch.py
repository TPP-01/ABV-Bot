import discord
from discord.ext import commands
import requests
import json
import asyncio


class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.twitch_client_id = "c6ntn3sbtupd03nwe9qhlh2ek2at9d"
        self.twitch_authorization_key = "r26y5m85n32s1paqug9dgvc2qxkzy1"

    def doesstream(self, login_name):
        ret = json.loads(requests.get(f'https://api.twitch.tv/helix/streams?user_login="{login_name}"',
                                      headers={"Authorization": f"Bearer {self.twitch_authorization_key}",
                                               "Client-Id": f"{self.twitch_client_id}"}).content.decode())

        streams, gamename, since = ret["data"] != [], ret["data"][0]["game_name"], \
                                   ret["data"][0]["started_at"].replace("Z", "").split("T")[1]

        return streams, gamename, since

    @commands.command(name="streams", help="Show the streaming state with login_names")
    async def streams(self, ctx, login):
        streams, gamename, since = self.doesstream(login)
        if streams:
            await ctx.send(f"{login} streamt {gamename} seit {since}")
        else:
            await ctx.send(f"{login} streamt nicht")


def setup(bot):
    bot.add_cog(twitch(bot))
