from pydantic import BaseModel

class GeneratorMatrix(BaseModel):
    z: int
    matrix: list[list[int]]