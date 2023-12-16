from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True)

    borrowed_books = relationship("Book", secondary="borrowings")

class Borrowing(Base):
    __tablename__ = "borrowings"

    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"), primary_key=True)
