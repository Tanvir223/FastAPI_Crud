from typing import List
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str

class BookCreate(BookBase):
    author_id: int

class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True
