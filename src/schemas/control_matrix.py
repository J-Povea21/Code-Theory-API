from pydantic import BaseModel

class ControlMatrix(BaseModel):
    n: int
    z: int
    k: int
    matrix: list[list[int]]