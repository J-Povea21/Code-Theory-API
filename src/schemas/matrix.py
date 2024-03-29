from pydantic import BaseModel

class Matrix(BaseModel):
    z: int
    MatrisG: list[list[int]]