import discord
from discord.ext import commands
import cogs.minecraft
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
initial_extensions = ["cogs.MainModule", "cogs.Fun", "cogs.NSFW", "cogs.BotOwner", "cogs.Admin", "cogs.Utility", "cogs.ReactionRole", "cogs.translation", "cogs.sound", "cogs.slashtest", "cogs.minecraft", "cogs.memes"]

bot = commands.Bot(command_prefix=get_prefix, description="The official ABV bot",intents=intents, help_command=None)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\nBot Latency: {round(bot.latency * 1000,2)}ms')
    print(f'Successfully logged in and booted...!')
    print([str(i).replace(',', '\n') for i in bot.guilds])
    #for server in bot.guilds:
        #for channel in server.channels:
            #if channel.permission_for(server.me).create_instant_invite:
                #print(f"Invite für {server.name}: {await channel.create_invite()}")
                #break


bot.run(secrets.token, reconnect=True)
