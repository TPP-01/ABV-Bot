from discord.ext import commands
import discord
import json
import requests


class minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="serverinfo", aliases=["si"])
    async def serverinfo(self, ctx, ip):
        player_list_cut = []
        API_URL = f"https://api.mcsrvstat.us/2/{str(ip)}"
        r = requests.get(API_URL)
        response = r.json()
        res = response
        print(response["debug"]["apiversion"])
        IMG_API = f"https://api.iapetus11.me/mc/servercard/{str(ip)}"
        #img_r = requests.get(IMG_API)
        if res["debug"]["ping"]:
            online_players = res["players"]["online"]
            max_players = res["players"]["max"]
            player_list = res["players"]["list"]
            for p in player_list:
                if not ("§" in p or len(p) > 16 or len(p) < 3 or " " in p or "-" in p):
                    player_list_cut.append(p)
            embed = discord.Embed(title=f"{ip} is online", color=0x07e43e)
            embed.set_image(url=IMG_API)
            embed.add_field(name="Ip", value=ip, inline=True)
            embed.add_field(name="Version", value=res["version"], inline=True)
            embed.add_field(name=f"Online Players ({online_players}/{max_players}", value=player_list_cut, inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(minecraft(bot))