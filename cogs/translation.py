from googletrans import Translator
import discord
from discord.ext import commands


class translation(commands.Cog):

    def __init__(self, bot):
        self.translator = Translator()
        self.bot = bot

    @commands.slash_command(guild_ids = [760547427152560160, 1227685392602370088], name="translate", aliases=["tr"])
    async def translate(self, ctx, text, target_lang):
        """
        Slash command for translating text to a specified language.

        Args:
            ctx (commands.Context): The context in which the command is being invoked.
            text (str): The text to be translated.
            target_lang (str): The language code or name to translate the text into.

        Returns:
            None

        Raises:
            None

        Notes:
            This command uses a translator instance initialized in the class to perform the translation.
            Deletes the invoking message if the command is invoked in a guild context.
            Sends an embed with the translation result, including the translated text and pronunciation if available.
            The embed message auto-deletes after 60 seconds.
        """
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


def setup(bot):
    bot.add_cog(translation(bot))
