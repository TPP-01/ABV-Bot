import discord
import  requests
import json

class mcsrv_functs():
    def __init__(self):
        print("good")
    def server_info_funct(self, ip):
        player_list_cut = []
        API_URL = f"https://api.iapetus11.me/mc/status/{str(ip)}"
        r = requests.get(API_URL)
        response = r.json()
        res = response
        backtick = "`"
        seperator = ","
        players = ""
        # IMG_API = f"https://api.iapetus11.me/mc/servercard/{str(ip)}"
        if res["online"]:
            online_players = res["players_online"]
            max_players = res["players_max"]
            player_list = res["players"]
            for p in player_list:
                name = p["name"]
                player_list_cut.append(name)
                # print(player_list)[debug]
                # print(player_list_cut)[debug]
            for name in player_list_cut:
                if player_list_cut.index(name) == len(player_list_cut) - 1:
                    players = players + backtick + name + backtick

                else:
                    players = players + backtick + name + backtick + seperator  # add \n to make new line for every player
            embed = discord.Embed(title=f"{ip} is online", color=0x07e43e)
            embed.set_image(url=f"https://api.iapetus11.me/mc/servercard/{str(ip)}?v={random.random() * 100000}")
            embed.add_field(name="Ip", value=ip, inline=True)
            embed.add_field(name="Version", value=res["version"]["software"], inline=True)
            embed.add_field(name=f"Online Players ({online_players}/{max_players}", value=players, inline=False)
            embed.set_footer(
                text="made by the ABV-Bot Development Team, (inspired by https://github.com/Iapetus-11 `s Villager-Bot)")
            return embed
        else:
            embed = discord.Embed(title=f"No Minecraft Server detected at: {str(ip)} !", color=0xff0000)
            return embed


if __name__ == "__main__":
    mcsrv_functs.server_info_funct("1.1.1.1")