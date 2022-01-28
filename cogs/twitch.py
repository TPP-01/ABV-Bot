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
            try:
                twitchjson = json.load(j)
                twitchjson[str(ctx.author.id)] = repr(eval(twitchjson[str(ctx.author.id)]).append(login))
                json.dump(twitchjson, j)
                await ctx.send("Der Reminder wurde gesetzt")
                if ctx.guild:
                    await ctx.message.delete()

            except json.decoder.JSONDecodeError:
                twitchjson = {str(ctx.author.id): repr([login])}
                json.dump(twitchjson, j)
                await ctx.send("Der Reminder wurde gesetzt")
                if ctx.guild:
                    await ctx.message.delete()

    @tasks.loop(seconds=10)
    async def twitchreminder(self):
        with open("twitch.json", "r") as j:
            print(j.read())
            twitchjson = json.load(j)
            print(twitchjson)###################
            for userid, streamers in twitchjson.items():
                userid = int(userid)
                streamers = eval(streamers)
                print(twitchjson.items())###################
                user = await self.bot.get_user(userid)
                for streamer in streamers:
                    print(streamers)###################
                    streams, gamename, since = self.doesstream(streamer)
                    if streams == True:
                        print("Doesstream")###################
                        await user.send(f"Der Streamer {streamer} streamt das Spiel {gamename}!")
            print("Errorcode: 0")###################


def setup(bot):
    t = twitch(bot)
    t.twitchreminder.start()
    bot.add_cog(t)
