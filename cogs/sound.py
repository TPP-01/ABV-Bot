import discord
import time
from discord.ext import commands
import asyncio
from gtts import gTTS
import os
class sound(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="earrape", aliases=["er"])
    async def earrape(self, ctx):
        self.voice_channel = ctx.author.voice
        channelname = None

        if self.voice_channel is not None:
            self.voice_channel = self.voice_channel.channel
            channelname = self.voice_channel.name
            await ctx.send(f"Playing in {channelname}")
            self.vc = await self.voice_channel.connect()
            self.vc.play(discord.FFmpegPCMAudio(source="music/earrape.mp3"))
            while self.vc.is_playing():
                await asyncio.sleep(0.5)
            try:
                await self.vc.disconnect()
            except:
                pass
        else:
            ctx.send(f"{ctx.author.name} is not in a channel")
        await ctx.message.delete()


    @commands.command(name="tts")
    async def tts(self, ctx, text, lang="de"):

        tts = gTTS(text, lang=lang)
        filename = f"tts_file_{lang}_{text}.mp3"
        full_path = f"tts_audio/{filename}"
        tts.save(full_path)
        print("file saved")
        self.voice_channel = ctx.author.voice
        channelname = None

        if self.voice_channel is not None:
            self.voice_channel = self.voice_channel.channel
            channelname = self.voice_channel.name
            await ctx.send(f"Playing in {channelname}")
            self.vc = await self.voice_channel.connect()
            self.vc.play(discord.FFmpegPCMAudio(source=full_path))
            while self.vc.is_playing():
                await asyncio.sleep(0.5)
            try:
                await self.vc.disconnect()
                os.remove(full_path)
                print("file deleted")
            except:
                pass
        else:
            ctx.send(f"{ctx.author.name} is not in a channel")
        await ctx.message.delete()


    @commands.command(name="disconnect", aliases=["dc"])
    async def disconnect(self, ctx):
        await self.vc.disconnect()
        await ctx.send("Disconnected!")
        try:
            await ctx.message.delete()
        except:
            print("No Permissions to delete ctx.message")


def setup(bot):
    bot.add_cog(sound(bot))
