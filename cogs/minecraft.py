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
            with open("servers.json") as f:
                data = json.load(f)
                print(type(data))
                return data
        self.lock = asyncio.Lock()
        #self.mysticcraft_serv_checker.start()
        self.minecraft_server_checker.start()
        self.json_data = json_para()


    @tasks.loop(seconds=10.0)
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



    @minecraft_server_checker.before_loop
    async def before_minecrft_chern(self):
        await self.bot.wait_until_ready()
    @commands.slash_command(guild_ids = [760547427152560160, 1227685392602370088], name="serverinfo", aliases=["si"])
    async def serverinfo(self, ctx, ip):
        """
        Retrives basic server information for a given address
        """
        embed = custom_modules.mcserv_functs.mcsrv_functs.server_info_funct(ip=ip)
        await ctx.respond(embed=embed)





def setup(bot):
    bot.add_cog(minecraft(bot))
