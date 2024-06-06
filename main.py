from src.core.logger import Logger
import os
import src.core.bot
from dotenv import load_dotenv

log = Logger().logger

log.debug("Loading environment variables...")
load_dotenv()
token = os.getenv("BOT_TOKEN")
log.debug(f"Fetched token token: {token}")

log.info("Starting up.")

bot = src.core.bot.bot

bot.run(os.getenv("BOT_TOKEN"))
