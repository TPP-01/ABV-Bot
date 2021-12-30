from discord.ext import commands
import discord
import json
import requests
import random
# Credits to the API to https://github.com/Iapetus-11
class minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="serverinfo", aliases=["si"])
    async def serverinfo(self, ctx, ip):
        player_list_cut = []
        API_URL = f"https://api.iapetus11.me/mc/status/{str(ip)}"
        r = requests.get(API_URL)
        response = r.json()
        res = response
        backtick = "`"
        seperator = ","
        players = ""
        #IMG_API = f"https://api.iapetus11.me/mc/servercard/{str(ip)}"
        if res["online"]:
            online_players = res["players_online"]
            max_players = res["players_max"]
            player_list = res["players"]
            for p in player_list:
                name = p["name"]
                player_list_cut.append(name)
                #print(player_list)[debug]
                #print(player_list_cut)[debug]
            for name in player_list_cut:
                if player_list_cut.index(name) == len(player_list_cut) - 1:
                    players = players + backtick + name + backtick

                else:
                    players = players + backtick + name + backtick + seperator            # add \n to make new line for every player
            embed = discord.Embed(title=f"{ip} is online", color=0x07e43e)
            embed.set_image(url=f"https://api.iapetus11.me/mc/servercard/{str(ip)}?v={random.random()*100000}")
            embed.add_field(name="Ip", value=ip, inline=True)
            embed.add_field(name="Version", value=res["version"]["software"], inline=True)
            embed.add_field(name=f"Online Players ({online_players}/{max_players}", value=players, inline=False)
            embed.set_footer(text="made by the ABV-Bot Development Team, (inspired by https://github.com/Iapetus-11 `s Villager-Bot)")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"No Minecraft Server detected at: {str(ip)} is down", color=0xff0000)
            embed.set_footer(
                text="made by the ABV-Bot Development Team, (inspired by https://github.com/Iapetus-11 `s Villager-Bot)")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(minecraft(bot))