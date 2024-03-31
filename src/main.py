from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.schemas.schemas import *
from src.core.encryptor import encrypt, decrypt
from src.core.lineal import lineal_code
from src.core.generator import generator_matrix
from src.core.control import control_matrix


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
    return {"success": True, "message": "Hello! This is the Code Theory API :)"}

# Caesar Cipher Endpoints (Amdres)
@app.post("/encrypt")
async def encrypt_text(msg: Message):
    return encrypt(msg.shift, msg.content)

@app.post("/decrypt")
async def decrypt_text(msg: Message):
    return decrypt(msg.shift, msg.content)

# Lineal code to generator matrix (Sandro119)
@app.post("/code-to-generator")
async def code_to_generator(code: LinealCode):
    return generator_matrix(code.code, code.z)

# Matrix Endpoints (Keiver123)
@app.post("/lineal-code")
async def lineal_code_params(code_info: GeneratorMatrix):
    return lineal_code(code_info.matrix, code_info.z)

# Generator Matrix to Control Matrix (Clau210605)
@app.post("/generator-to-control")
async def generator_to_control(code_info: ControlMatrix):
    return control_matrix(code_info.n, code_info.k,code_info.matrix,code_info.z)