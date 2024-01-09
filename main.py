import discord
import os
from dotenv import load_dotenv
import ezcord

intents = discord.Intents(messages=True, guilds=True)

status = discord.Status.online

bot = ezcord.Bot(
    intents=intents,
    language="de",
    debug_guilds=[760547427152560160],
    status=status,
    #activity=activity
)
bot.add_help_command()

@bot.event
async def on_ready():
   # print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\nBot Latency: {round(bot.latency * 1000, 2)}ms')
    print(f"{bot.user} ist online")
    # The command below displays all guilds where the bot has been added
    #print([str(i).replace(',', '\n') for i in bot.guilds])

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

load_dotenv()
bot.run(os.getenv("TOKEN"), reconnect=True)