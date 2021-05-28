import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
BG_IMAGE = getenv("BG_IMAGE", "")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_USERNAME = getenv("BOT_USERNAME", "")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "")
PROJECT_NAME = getenv("PROJECT_NAME", "")
SOURCE_CODE = getenv("SOURCE_CODE", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "")
PMPERMIT = getenv("PMPERMIT", "")
LOG_GRP = getenv("LOG_GRP", "")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
