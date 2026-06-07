import asyncio
import os
from telethon import TelegramClient, events, Button
from fastapi import FastAPI
import uvicorn

Environment Variables

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

Links to send

links = [
"https://diskwala.link/abc123",
"https://diskwala.link/xyz456"
]

ad_text = "🔥 Want full access to all premium videos? Buy now!"
ad_button_url = "https://t.me/diskwalabot?start=premium"

Telegram client

client = TelegramClient("bot", api_id, api_hash)

FastAPI app

app = FastAPI()

@app.get("/")
async def home():
return {"status": "Bot Running"}

Start bot when server starts

@app.on_event("startup")
async def startup_event():
await client.start(bot_token=bot_token)
print("Bot Started")

/start command

@client.on(events.NewMessage(pattern=r"^/start"))
async def start_handler(event):
msg_text = "\n".join(links) + "\n\n" + ad_text

msg = await event.respond(
    msg_text,
    buttons=[
        Button.url("Buy Premium", ad_button_url)
    ]
)

await asyncio.sleep(1800)
await msg.delete()

Run server

if name == "main":
uvicorn.run(app, host="0.0.0.0", port=8080)

