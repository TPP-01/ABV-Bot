import discord
import time
from discord.ext import commands
import asyncio
from gtts import gTTS
import os
class sound(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids = [760547427152560160, 1227685392602370088], name="earrape", aliases=["er"])
    async def earrape(self, ctx):
        """
        Plays a very very loud sound in the channel you are currently in
        """
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
            await ctx.send(f"{ctx.author.name} is not in a channel")
        await ctx.message.delete()


    @commands.slash_command(guild_ids = [760547427152560160, 1227685392602370088], name="tts")
    async def tts(self, ctx, text, lang="de"):
        """
        Does TTS in the vc you are currently in
        """
        tts = gTTS(text, lang=lang)
        filename = f"temp.mp3"
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
            await ctx.send(f"{ctx.author.name} is not in a channel")
        if ctx.guild:
            await ctx.message.delete()

    @commands.slash_command(guild_ids = [760547427152560160, 1227685392602370088], name="disconnect", aliases=["dc"])
    async def disconnect(self, ctx):
        """
        Disconnects the bot from any VC
        """
        await self.vc.disconnect()
        await ctx.send("Disconnected!")
        try:
            if ctx.guild:
                await ctx.message.delete()
        except:
            print("No Permissions to delete ctx.message")


def setup(bot):
    bot.add_cog(sound(bot))
