import discord
from discord.ext import commands
import cogs.minecraft
import secrets
from dotenv import load_dotenv
import os

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
load_dotenv()
token = os.environ['TOKEN']




#cogs to use
initial_extensions = ["cogs.MainModule", "cogs.Fun", "cogs.NSFW", "cogs.BotOwner", "cogs.Admin", "cogs.Utility", "cogs.ReactionRole", "cogs.translation", "cogs.sound", "cogs.minecraft", "cogs.memes"]

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='=', intents=intents)
        self.initial_extensions = [
            'cogs.Admin',
            'cogs.MainModule',
            'cogs.BotOwner',
            'cogs.Fun',
            'cogs.memes',
            'cogs.minecraft',
        ]

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)


    async def close(self):
        await super().close()

    async def on_ready(self):
        print('Ready!')

bot = MyBot()
bot.run(token, reconnect=True)
