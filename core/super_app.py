from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from extras.extras import *

app = FastAPI(title="Taherion AI Super App", version="3.0.0", description="Ultimate AI-powered Super App")

USERS = {}
WALLETS = {}
MESSAGES = []

class User(BaseModel):
    username: str
    password: str

class Message(BaseModel):
    sender: str
    receiver: str
    text: str

@app.post("/auth/register")
def register(user: User):
    USERS[user.username] = {"password": user.password}
    WALLETS[user.username] = 0.0
    return {"status": "registered"}

@app.post("/auth/login")
def login(user: User):
    if USERS.get(user.username, {}).get("password") == user.password:
        return {"status": "login_success"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/ai")
def ai(question: str):
    return {"answer": basic_ai(question)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("core.super_app:app", host="0.0.0.0", port=8000, reload=True)
