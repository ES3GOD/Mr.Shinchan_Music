from pyrogram import Client as Bot

from ShinchanMusic.config import API_HASH, API_ID, BOT_TOKEN
from ShinchanMusic.services.callsmusic import run

# os.system(f"wget -O ./etc/foreground.png {BG_IMAGE}")
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="ShinchanMusic.modules"),
)

bot.start()
run()
