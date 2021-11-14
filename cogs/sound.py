import discord
from discord.ext import commands
import time

class sound(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="earrape", aliases=["er"])
    async def earrape(self, ctx):
        voice_channel = ctx.author.voice.channel

        channelname = None
        if voice_channel is not None:
            channelname = voice_channel.name
            await ctx.send(f"Playing in {channelname}")
            self.vc = await self.voice_channel.connect()
            self.vc.play(discord.FFmpegPCMAudio(source="music/earrape.mp3"))
            while vc.is_playing():
                time.sleep(0.5)
            try:
                await self.vc.disconnect()
            except: pass
        else:
            ctx.send(f"{ctx.author.name} is not in a channel")
        await ctx.message.delete()

    @commands.command(name="disconnect", aliases=["dc"])
    async def disconnect(self):
        self.vc.disconnect()
        await ctx.send("Disconnected!")
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(sound(bot))
