import datetime
import json
import secrets

import requests
from discord.ext import commands, tasks


class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.twitch_client_id = secrets.twitch_client_id
        self.twitch_authorization_key = secrets.twitch_authorization_key
        self.twitchreminder.start()

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

    @commands.command(name="unremind", help="Unremind streamer' streams")
    async def unremind(self, ctx, login):
        with open("twitch.json", "r") as j:
            s = j.read()
            with open("twitch.json", "w") as j:
                if s != "":
                    twitchjson = json.loads(s)
                    try:
                        streamerslist = twitchjson[str(ctx.author.id)]
                        try:
                            streamerslist.pop(streamerslist.index(login))
                            twitchjson[str(ctx.author.id)] = streamerslist
                            await ctx.send("Der Reminder wurde gelöscht.")
                            await ctx.message.delete()

                        except IndexError:
                            await ctx.send("Du hast keinen Reminder für diesen Streamer gesetzt.")
                            await ctx.message.delete()

                    except KeyError:
                        await ctx.send("Du bist nicht in der Datenbank.")
                        await ctx.message.delete()

    @commands.command(name="remind", help="Remind when specific twitch-streamers stream.")
    async def remind(self, ctx, login):
        with open("twitch.json", "r") as j:
            s = j.read()
            with open("twitch.json", "w") as j:
                if s != "":
                    twitchjson = json.loads(s)
                    try:
                        streamerlist = twitchjson[str(ctx.author.id)]
                        if not login in streamerlist:
                            streamerlist.append(login)
                        twitchjson[str(ctx.author.id)] = streamerlist

                    except KeyError:
                        twitchjson[str(ctx.author.id)] = [login]
                    json.dump(twitchjson, j)
                    await ctx.send("Der Reminder wurde gesetzt")
                    if ctx.guild:
                        await ctx.message.delete()

                else:
                    with open("twitch.json", "w") as j:
                        json.dump({str(ctx.author.id): [login]}, j)
                        await ctx.send("Der Reminder wurde gesetzt")
                        if ctx.guild:
                            await ctx.message.delete()

    @tasks.loop(seconds=120)
    async def twitchreminder(self):
        sent = False
        with open("twitch.json", "r") as j:
            s = j.read()
            if s != "":
                twitchjson = json.loads(s)
                for userid, streamers in twitchjson.items():
                    userid = int(userid)
                    for guild in self.bot.guilds:
                        if sent:
                            sent = False
                            break
                        else:
                            for member in guild.members:
                                if int(member.id) == userid:
                                    if member is not None:
                                        for streamer in streamers:
                                            streams, gamename, since = self.doesstream(streamer)
                                            if streams:
                                                last3min = (datetime.datetime.now().minute + 60 * (
                                                        datetime.datetime.now().hour + 1)) - (
                                                                   int(since.split(":")[1]) + 60 * (
                                                                   int(since.split(":")[0]) + 1))
                                                if 2 >= last3min > 0:
                                                    await member.send(f"Der Streamer {streamer} streamt {gamename}!")
                                                    sent = True

    @twitchreminder.before_loop
    async def twitchremider_before_ready(self):
        await self.bot.wait_until_ready()


def setup(bot):
    t = twitch(bot)
    bot.add_cog(t)

# ToDo: Code beschreiben
