from googletrans import Translator
import discord
from discord.ext import commands


class translation(commands.Cog):

    def __init__(self, bot):
        self.translator = Translator()
        self.bot = bot

    @commands.command(name="translate", aliases=["tr"])
    async def translate(self, ctx, text, target_lang):
        translate = self.translator.translate(text, dest=target_lang)
        textout = translate.text
        pronout = translate.pronunciation
        embed = discord.Embed(title="Translator")
        embed.add_field(name="Input", value=text, inline=True)
        embed.add_field(name="Output", value=f"Translation: {textout}\nPronunciation: {pronout}", inline=True)
        embed.set_footer(text="made by the ABV-Bot Development Team")
        if ctx.guild:
            await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=60)


async def setup(bot):
    await bot.add_cog(translation(bot))