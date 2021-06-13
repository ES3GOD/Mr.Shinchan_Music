from pyrogram import Client

from ShinchanMusic import config
from ShinchanMusic.services.callsmusic.callsmusic import pytgcalls, run
from ShinchanMusic.services.queues import queues

client = Client(SESSION_NAME, API_ID, API_HASH)
run = client.run
