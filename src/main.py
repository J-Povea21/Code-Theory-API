from fastapi import FastAPI
from src.schemas.message import Message
from src.schemas.matrix import Matrix
from src.core.encryptor import encrypt, decrypt
from src.core.code_elems import ejecutable
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Root Endpoint
@app.get("/")
async def root():
    return {"message": "Hello! This is the Code Theory API :)"}

# Caesar Cipher Endpoints (Amdres)
@app.post("/encrypt")
async def encrypt_text(msg: Message):
    return {"message": encrypt(msg.shift, msg.content)}

@app.post("/decrypt")
async def decrypt_text(msg: Message):
    return {"message": decrypt(msg.shift, msg.content)}

# Matrix Endpoints (Keiver123)
@app.post("/lineal-code")
async def lineal_code(matrix: Matrix):
    return {"message": ejecutable(matrix.MatrisG, matrix.z)}