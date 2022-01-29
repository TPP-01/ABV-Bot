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

    @commands.command(name="remind", help="Remind when specific twitch-streamers stream.")
    async def remind(self, ctx, login):
        with open("twitch.json", "w+") as j:# ToDo: Komplett überarbeiten und testen
            s = j.read()
            print(str(s))
            print("Test")
            if s != "":
                twitchjson = json.loads(s)
                print(twitchjson)
                streamerlist = twitchjson[str(ctx.author.id)]
                print(streamerlist)
                streamerlist.append(login)
                print(streamerlist)
                twitchjson[str(ctx.author.id)] = streamerlist
                print(streamerlist)
                print(twitchjson)
                j.write(json.dumps(twitchjson))
                await ctx.send("Der Reminder wurde gesetzt")
                if ctx.guild:
                    await ctx.message.delete()

            else:
                with open("twitch.json", "w") as j:
                    json.dump({str(ctx.author.id): [login]}, j)
                    await ctx.send("Der Reminder wurde gesetzt")
                    if ctx.guild:
                        await ctx.message.delete()
            j.close()

    @tasks.loop(seconds=120)
    async def twitchreminder(self):
        with open("twitch.json", "r") as j:
            s = j.read()
            if s != "":
                twitchjson = json.loads(s)
                print(twitchjson)  ###################
                for userid, streamers in twitchjson.items():
                    userid = int(userid)
                    user = None
                    for guild in self.bot.guilds:
                        for member in guild.members:
                            if int(member.id) == userid:
                                user = member
                                break
                    if user is not None:
                        for streamer in streamers:
                            streams, gamename, since = self.doesstream(streamer)
                            if streams == True:
                                if (datetime.datetime.now().minute + 60 * datetime.datetime.now().hour) - (
                                        int(since.split(":")[2]) + 60 * int(since.split(":")[1])) <= 3:
                                    await user.send(f"Der Streamer {streamer} streamt {gamename}!")
            j.close()

    @twitchreminder.before_loop
    async def twitchremider_before_ready(self):
        await self.bot.wait_until_ready()


def setup(bot):
    t = twitch(bot)
    bot.add_cog(t)

# ToDo: Debug entfernen, Code beschreiben + überarbeiten
