import asyncio
from telethon import TelegramClient, events, Button
from fastapi import FastAPI
import uvicorn
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

links = [
    "https://diskwala.link/abc123",
    "https://diskwala.link/xyz456"
]

ad_text = "🔥 Want full access to all premium videos? Buy now!"
ad_button_url = "https://t.me/diskwalabot?start=premium"

client = TelegramClient('bot', api_id, api_hash)

@client.on(events.NewMessage(pattern=r"^/start"))
async def start_handler(event):
    msg_text = "\n".join(links) + "\n\n" + ad_text

    msg = await event.respond(
        msg_text,
        buttons=[Button.url("Buy Premium", ad_button_url)]
    )

    await asyncio.sleep(1800)
    await msg.delete()

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Bot Running"}

async def bot_main():
    await client.start(bot_token=bot_token)
    await client.run_until_disconnected()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(bot_main())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

