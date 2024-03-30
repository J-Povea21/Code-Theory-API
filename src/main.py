from fastapi import FastAPI
from src.schemas.caesar import Message
from src.schemas.lineal_code import GeneratorMatrix
from src.schemas.control_matrix import ControlMatrix
from src.core.encryptor import encrypt, decrypt
from src.core.code_elems import lineal_code
from src.core.control_matrix import control_matrix
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
async def lineal_code_params(code_info: GeneratorMatrix):
    return lineal_code(code_info.matrix, code_info.z)

# Generator Matrix to Control Matrix (Clau210605)
@app.post("/generator-to-control")
async def generator_to_control(code_info: ControlMatrix):
    return {"matrix": control_matrix(code_info.n, code_info.k,code_info.matrix,code_info.z)}