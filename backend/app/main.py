import os
import httpx
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("CHAT_ID")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


async def send_telegram_message(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload)
            response.raise_for_status()
        except Exception as e:
            print(f"Ошибка отправки в Telegram: {e}")


@app.post("/api/visit")
async def track_visit(request: Request):
    data = await request.json()
    ip = request.client.host

    # if data.get("referrer") == 'direct': # если страницу перезагрузили
    #     return {"status": "success"}


    message = (
        f"<b>Время:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"<b>IP:</b> {ip}\n"
        f"<b>Экран:</b> {data.get('screen_resolution')}\n"
        f"<b>Источник:</b> {data.get('referrer')}\n"
        f"<b>Браузер:</b> {data.get('user_agent')[:50]}..."
    )

    await send_telegram_message(message)
    return {"status": "success"}