from pydantic import BaseModel

# Caesar
class Message(BaseModel):
    shift: int
    content:str 

# Lineal Code
class GeneratorMatrix(BaseModel):
    z: int
    matrix: list[list[int]]    

# Code to Generator matrix
class LinealCode(BaseModel):
    z: int
    code: list[str]

# Generator to Control Matrix
class ControlMatrix(BaseModel):
    n: int
    z: int
    k: int
    matrix: list[list[int]]
