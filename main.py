import discord
from discord.ext import commands

import secrets

intents = discord.Intents.default()
intents.members = True

def get_prefix(bot, message):
    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['=']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '='
    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ["cogs.MainModule", "cogs.Fun", "cogs.NSFW", "cogs.BotOwner", "cogs.Admin", "cogs.Utility", "cogs.ReactionRole"]

bot = commands.Bot(command_prefix=get_prefix, description="The official ABV bot",intents=intents, help_command=None)

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')
    print([str(i).replace(',', '\n') for i in bot.guilds])

bot.run(secrets.token, bot=True, reconnect=True)
