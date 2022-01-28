import json
import secrets

import requests
from discord.ext import commands, tasks


class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.twitch_client_id = secrets.twitch_client_id
        self.twitch_authorization_key = secrets.twitch_authorization_key

    def doesstream(self, login_name):
        ret = json.loads(requests.get(f'https://api.twitch.tv/helix/streams?user_login={login_name}',
                                      headers={"Authorization": f"Bearer {self.twitch_authorization_key}",
                                               "Client-Id": f"{self.twitch_client_id}"}).content.decode())

        streams = ret["data"] != []
        if streams:
            gamename, since = ret["data"][0]["game_name"], ret["data"][0]["started_at"].replace("Z", "").split("T")[1]
        else:
            gamename, since = None, None

        return streams, gamename, since

    @commands.command(name="streams", help="Show the streaming state with login_names")
    async def streams(self, ctx, login):
        streams, gamename, since = self.doesstream(login)
        if streams:
            await ctx.send(f"{login} streamt {gamename} seit {since}!")
        else:
            await ctx.send(f"{login} streamt nicht.")
        if ctx.guild:
            await ctx.message.delete()

    @commands.command(name="remind", help="Remind when specific twitch-streamers stream.")
    async def remind(self, ctx, login):
        with open("twitch.json", "r+") as j:
            twitchjson = json.loads(j.read())
            twitchjson[ctx.user.id] = twitchjson[ctx.user.id].append(login)
            j.write(json.dumps(twitchjson))

    @tasks.loop(seconds=120)
    async def twitchreminder(self):
        with open("twitch.json", "r") as j:
            twitchjson = json.loads(j.read())
            for userid, streamers in twitchjson.items():
                user = self.bot.get_user(userid)
                for streamer in streamers:
                    streams, gamename, since = self.doesstream(streamer)
                    if streams == True:
                        user.send(f"Der Streamer {streamer} streamt das Spiel {gamename}!")


def setup(bot):
    bot.add_cog(twitch(bot))
