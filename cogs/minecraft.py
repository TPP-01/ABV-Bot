import json
import aiosqlite
from discord.ext import commands, tasks
import discord
import requests
import random
import asyncio
import custom_modules.mcserv_functs
# Credits to the API to https://github.com/Iapetus-11
class minecraft(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        def json_para():
            with open("config.json") as f:
                data = json.load(f)
                print(type(data))
                return data
        self.lock = asyncio.Lock()
        #self.mysticcraft_serv_checker.start()
        self.minecraft_server_checker.start()
        self.json_data = json_para()
    #only here for demo
    #@tasks.loop(seconds=5.0)
    #async def mysticcraft_serv_checker(self):
        #server_ip_my = "185.208.205.128:25565"
        #guild_id_my = 907991840408608768
        #message_id_my = 931238519576330370
        #ch_id_my = 930547160376827914
        #channel = self.bot.get_channel(ch_id_my)
        #message = await channel.fetch_message(message_id_my)
        #embed1 = custom_modules.mcserv_functs.mcsrv_functs.server_info_funct(ip=server_ip_my)
        #await message.edit(embed=embed1)


    @tasks.loop(seconds=5.0)
    async def minecraft_server_checker(self):
        data = self.json_data
        servers = data.get("Servers")
        for k,v in servers.items():
            message_id = v.get("message_id")
            channel_id = v.get("channel_id")
            server_ip = v.get("ip")
            channel = self.bot.get_channel(channel_id)
            message = await channel.fetch_message(message_id)
            embed1 = custom_modules.mcserv_functs.mcsrv_functs.server_info_funct(ip=server_ip)
            await message.edit(embed=embed1)






    #@mysticcraft_serv_checker.before_loop
    #async def before_mineservchecker(self):
        #print('waiting...')
        #await self.bot.wait_until_ready()


    @minecraft_server_checker.before_loop
    async def before_minecrft_chern(self):
        await self.bot.wait_until_ready()
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
            embed = discord.Embed(title=f"No Minecraft Server detected at: {str(ip)} !", color=0xff0000)
            embed.set_footer(
                text="made by the ABV-Bot Development Team, (inspired by https://github.com/Iapetus-11 `s Villager-Bot)")
            await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(minecraft(bot))
