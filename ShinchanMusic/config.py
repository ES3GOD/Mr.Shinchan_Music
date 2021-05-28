import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCyzl4BKQhw3XjKHd2m5PGrYlXMgl7tFEQj2BnEaxZ3uas1KnS4qXJpsA09gk_pU9YxkawFliQsszTDeARR9hXz85DuRlk0HhxQ_7Tz0-R0GTZWKUMUBgj42hFAXcyAom3qPjz10dQLNrMgbqSILW3y8qrUI3_omA1IYnk-xAUMVWxhceRFe4uzy3K7ybKnlWX3VkrmgzyKAxxMUFs7dbVaZYWpYl__MflNHnAADIDrM5W532CLUfBgoCvwny0YQIC-_VJEXZ9VUp2DfTrlatCkqp1CrNZJDSMdWodBtpfLBBgufSZ-ZYh_pzkmz57dhJ131Cmf_OhOLAUOOT3O-N9abrpWSwA")
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
