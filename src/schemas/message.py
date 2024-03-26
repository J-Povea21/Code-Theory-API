from pydantic import BaseModel

class Message(BaseModel):
    shift: int
    content:str 

