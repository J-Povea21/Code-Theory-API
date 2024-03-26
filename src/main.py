from fastapi import FastAPI
from src.schemas.message import Message
from src.core.encryptor import encrypt, decrypt

app = FastAPI()

# Root Endpoint
@app.get("/")
async def root():
    return {"message": "Hello! This is the Caesar Cipher API :)"}

# Caesar Cipher Endpoints
@app.post("/encrypt")
async def encrypt_text(msg: Message):
    return {"message": encrypt(msg.shift, msg.content)}

@app.post("/decrypt")
async def decrypt_text(msg: Message):
    return {"message": decrypt(msg.shift, msg.content)}

