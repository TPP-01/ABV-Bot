import discord
from discord.ext import commands

import secrets

intents = discord.Intents.default()
intents.members = True

def get_prefix(bot, message):
    # in this list are all prefixes allowed
    prefixes = ['=']

    # if the command is not in a guild use only this prefixes
    if not message.guild:
        return '='
    return commands.when_mentioned_or(*prefixes)(bot, message)


#cogs to use
initial_extensions = ["cogs.MainModule", "cogs.Fun", "cogs.NSFW", "cogs.BotOwner", "cogs.Admin", "cogs.Utility", "cogs.ReactionRole", "cogs.translation", "cogs.sound"]

bot = commands.Bot(command_prefix=get_prefix, description="The official ABV bot",intents=intents, help_command=None)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')
    print([str(i).replace(',', '\n') for i in bot.guilds])

bot.run(secrets.token, bot=True, reconnect=True)
