import discord
from discord.ext import commands




class audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="play")
    async def play(self, ctx):
        await ctx.send("tbd")
        voice_channel = ctx.message.author.voice.channel
        voice_client = await voice_channel.connect()
        voice_client.play(discord.FFmpegPCMAudio(source="russia.mp3"), after=voice_client.disconnect)


    @commands.command(name="list_songs", aliases=["list"])
    async def list_songs(self, ctx):
        await ctx.send("tbd")

    @commands.command()






















def setup(bot):
    bot.add_cog(audio(bot))