from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

VALID_KEYS = set(
    key.strip().upper()
    for key in os.getenv("VALID_KEYS", "").split(",")
    if key.strip()
)

class ActivateRequest(BaseModel):
    key: str

@app.get("/")
def root():
    return {"status": "ok", "message": "Activation server is running"}

@app.post("/activate")
def activate(data: ActivateRequest):
    key = data.key.strip().upper()
    if key in VALID_KEYS:
        return {"valid": True}
    return {"valid": False}