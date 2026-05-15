from fastapi import FastAPI
from app.routes.webhook import router as webhook_router

app = FastAPI(
    title="Nistula Technical Assessment",
    version="1.0.0"
)

app.include_router(webhook_router)


@app.get("/")
async def root():
    return {
        "message": "Nistula backend is running"
    }