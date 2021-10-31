import discord
from discord.ext import commands
import ffmpeg




class audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="play")
    async def play(self, ctx):
        await ctx.send("tbd")
        voice_channel = ctx.message.author.voice.channel
        await voice_channel.connect()
        voice_client = ctx.channel.guild.voice_client
        voice_client.play(discord.FFmpegPCMAudio(source="russia.mp3"))


    @commands.command(name="list_songs", aliases=["list"])
    async def list_songs(self, ctx):
        await ctx.send("tbd")






















def setup(bot):
    bot.add_cog(audio(bot))