from fastapi import FastAPI

from .auth import router as auth_router
from .core_routes import router as core_router
from .database import init_db
from .model import generate_response
from .stripe_routes import router as stripe_checkout_router
from .stripe_webhook import router as stripe_webhook_router


app = FastAPI(title="Ultimate Health Center API")


@app.on_event("startup")
async def on_startup() -> None:
    init_db()


@app.get("/")
async def root():
    return {"message": "Ultimate Health Center API is running"}


@app.post("/api/chat")
async def chat(payload: dict):
    message = payload.get("message", "")
    if not message:
        return {"reply": "Please send a message to get started."}

    reply = generate_response(message)
    return {"reply": reply}


app.include_router(auth_router, prefix="/api")
app.include_router(core_router, prefix="/api")
app.include_router(stripe_checkout_router, prefix="/api")
app.include_router(stripe_webhook_router, prefix="/api")
