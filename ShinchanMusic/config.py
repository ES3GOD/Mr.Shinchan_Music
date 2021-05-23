import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQA8sTq8t4hDg-vUyx2EY-4f8CDrHlYQ5n_tW6SVDkGLHbYw8tCO7dAQBEUA2BkYYqm0b2nstZLGDIevt5lR1GQxP5C4QgxxSZhWs1pstkcJ-Wnj5dLawiiwVWqEhLxh8vitK5DYpVtSdUDreY9ihF8xMaDOul7Z5_vj3yGIpb09WHd7GPG_RepYAEC6ICnLdUVoYRy5HnJI-pSc1reukTVmhmUuv5C8XkUK9LPYqLfNF-9KsOw8RS8UIQfB88Pk3asdOQPNhzObwJFUjxq58DLgySn7ako5McK16KW363Uvtrr4YP_831Ikfs2M5NxfKz3rJJGm0ADPAj3xPilM_a5kaNSuXQA")
BOT_TOKEN = getenv("BOT_TOKEN", "1742763844:AAGh63thV8YSn8W4V2rvSzC0eamYFzlCgag")
BOT_NAME = getenv("BOT_NAME", "Mr.Shinchan")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@Shinchan_Updates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/544da923c008df67f98f4.png")
admins = {}
API_ID = int(getenv("API_ID", "4007894"))
API_HASH = getenv("API_HASH", "3e3b4931ce44aa2f406aea3b48ef0807")
BOT_USERNAME = getenv("BOT_USERNAME", "ShinchanHelper_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Shinchan_Helper")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Shinchan_Support")
PROJECT_NAME = getenv("PROJECT_NAME", "ShinchanMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/rihan2575/Mr.Shinchan_Music")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "ISRQZD-ZPZGCN-TOUUUS-FZIPEL-ARQ")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1782996378").split()))
