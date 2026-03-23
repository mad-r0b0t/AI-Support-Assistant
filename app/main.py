from fastapi import FastAPI
from api.webhook import router as webhook_router

app = FastAPI(title="AI Support Assistant")

app.include_router(webhook_router)

@app.get("/")
def root():
    return {"status": "AI Support Assistant running"}
