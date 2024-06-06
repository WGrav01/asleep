import discord
from src.core.logger import Logger

log = Logger().logger

intents = discord.Intents.default()
intents.message_content = True

bot = discord.AutoShardedClient(intents=intents)


@bot.event
async def on_ready():
    log.debug(f"Logged in successfully as {bot.user}")
