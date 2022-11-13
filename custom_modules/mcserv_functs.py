import discord
import requests
import json
import random
from datetime import datetime
import pendulum
class mcsrv_functs():
    #the credit to the endpoints goes to https://iapetus11.me/
    def __init__(self):
        print("good")
    def server_info_funct(ip):
        player_list_cut = []
        API_URL = f"https://api.iapetus11.me/mc/server/status/{str(ip)}"
        r = requests.get(API_URL)
        response = r.json()
        res = response
        backtick = "`"
        seperator = ","
        players = ""
        # IMG_API = f"https://api.iapetus11.me/mc/servercard/{str(ip)}"
        if res["online"]:
            online_players = res["online_players"]
            max_players = res["max_players"]
            player_list = res["players"]
            if not player_list:
                players = "Nobody online"
            else:
                for p in player_list:
                    name = p["username"]
                    player_list_cut.append(name)
                    # print(player_list)[debug]
                    # print(player_list_cut)[debug]
                for name in player_list_cut:
                    if player_list_cut.index(name) == len(player_list_cut) - 1:
                        players = players + backtick + name + backtick

                    else:
                        players = players + backtick + name + backtick + seperator  # add \n to make new line for every player
            timezone2 = pendulum.timezone("Europe/Paris")
            current_time = datetime.now(timezone2)
            dt_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
            embed = discord.Embed(title=f"{ip} is online", color=0x07e43e)
            embed.set_image(url=f"https://api.iapetus11.me/mc/server/status/{str(ip)}/image?v={random.random() * 100000}")
            embed.add_field(name="IP", value=ip, inline=True)
            embed.add_field(name="Version", value=res["version"]["software"], inline=True)
            embed.add_field(name=f"Online Players ({online_players}/{max_players})", value=players, inline=False)
            embed.set_footer(
                text=f"made by the ABV-Bot Development Team, (inspired by https://github.com/Iapetus-11 `s Villager-Bot) \nlast updated at {dt_string}")
            return embed
        else:
            embed = discord.Embed(title=f"No Minecraft Server detected at: {str(ip)} !", color=0xff0000)
            return embed


if __name__ == "__main__":
    print(str(mcsrv_functs.server_info_funct("play.abv-ttp.de:25565")))