from typing import List
from pydantic import BaseModel

class ClientBase(BaseModel):
    token: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    borrowed_books: List[Book] = []

    class Config:
        orm_mode = True
