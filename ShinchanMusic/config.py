import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAu-fIyAGgY2Fm-4d5cDIBrSjllxjB6wdrhTtvCjVMc4kDe0gZDE_G88H3iDdIMajwQJjMTHjQFx6FgKoVxsIP1D7ZGET8VGNZS2fsvDHqG4MxnkYjLZt_783jXcnAdL57xYjqzmiMIQj-QcxMNJ8BsbK-hJqYU6Rp8sFd8DrWvOOFV6jpJHdQGsHB69pnN4IXqcG4NIFUWfEdTECTID-2pU4ozXXciOlRCSnrRJvauZ1DEDZW405ZmERcRSTubo9nCE-2mnJIAbzYhofTw_v0ucpMfUncZ1Z-7dS1UPovQnTuf1aSJBxedmOuptkWuYk-v8vdhY7GBvCXYnZvk9b14brpWSwA")
BOT_TOKEN = getenv("BOT_TOKEN", "1742763844:AAGh63thV8YSn8W4V2rvSzC0eamYFzlCgag")
BOT_NAME = getenv("BOT_NAME", "Mr.Shinchan")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Shinchan_Updates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/544da923c008df67f98f4.png")
admins = {}
API_ID = int(getenv("API_ID", "3299005"))
API_HASH = getenv("API_HASH", "5eb2104272ac85a936a28d3b7efc73d2")
BOT_USERNAME = getenv("BOT_USERNAME", "ShinchanHelper_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Shinchan_Helper")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Shinchan_Support")
PROJECT_NAME = getenv("PROJECT_NAME", "ShinchanMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/Shinchan-Helper/Mr.Shinchan_Music")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "HNFPFJ-VUHJBN-HVUSQF-SOLLKZ-ARQ")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
LOG_GRP = getenv("LOG_GRP", "None")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1857705547").split()))
