from pydantic import BaseModel

class Note(BaseModel):
    user: str
    message: str