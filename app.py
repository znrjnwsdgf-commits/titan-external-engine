
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="TITAN AI ENGINE")

@app.get("/")
def home():
    return {
        "project": "TITAN AI ENGINE",
        "status": "running",
        "message": "External engine is ready",
        "time": datetime.now(timezone.utc).isoformat()
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
