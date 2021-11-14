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
            ctx.send(f"Playing in {channelname}")
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(source="music/earrape.mp3"))
            while vc.is_playing():
                time.sleep(0.5)
            await vc.disconnect()
        else:
            ctx.send(f"{ctx.author.name} is not in a channel")
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(sound(bot))
