from googletrans import Translator
import discord
from discord.ext import commands




class translation(commands.Cog):

    translator = Translator()
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="translate",  aliases=["tr"])
    async def translate(self, ctx, text, target_lang):
        translator = Translator()
        output = translator.translate(text, dest=target_lang)
        embed = discord.Embed(title="Translator")
        embed.add_field(name="Input", value=text, inline=True)
        embed.add_field(name="Output", value=output, inline=True)
        embed.set_footer(text="made by the ABV-Bot Development Team")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(translation(bot))