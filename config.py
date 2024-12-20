# © 𝘼𝙗𝙊𝙪𝙩𝙈𝙚_𝘿𝙆 🌿

import os
import logging
from os import environ
from logging.handlers import RotatingFileHandler
from time import time

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your Telegram Bot's API Token from @BotFather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Get your Telegram ID from @tgBaSiCbOt using "/id" command.
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#No Need to Change This 
PORT = os.environ.get("PORT", "8080")

#No need to Change This 
BOT_WORKERS = int(os.environ.get("BOT_WORKERS", "4"))

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
  
