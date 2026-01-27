from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/visit")
async def track_visit(request: Request):
    data = await request.json()
    ip = request.client.host

    print(f"[{datetime.now()}] Новый визит!")
    print(f"IP: {ip}")
    print(f"Экран: {data.get('screen_resolution')}")
    print(f"Откуда пришел: {data.get('referrer')}")

    return {"status": "success"}