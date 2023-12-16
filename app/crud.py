from sqlalchemy.orm import Session
from app.models import Author, Book, Client, Borrowing

def create_author(db: Session, author: AuthorCreate):
    db_author = Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Author).offset(skip).limit(limit).all()

def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()

def get_books_by_author(db: Session, author_id: int, skip: int = 0, limit: int = 10):
    return db.query(Book).filter(Book.author_id == author_id).offset(skip).limit(limit).all()

def create_client(db: Session, client: ClientCreate):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Client).offset(skip).limit(limit).all()

def get_client_books(db: Session, token: str):
    client = db.query(Client).filter(Client.token == token).first()
    if client:
        return client.borrowed_books
    return []

def link_client_book(db: Session, token: str, book_id: int):
    client = db.query(Client).filter(Client.token == token).first()
    if client:
        book = db.query(Book).filter(Book.id == book_id).first()
        if book:
            client.borrowed_books.append(book)
            db.commit()
            return True
    return False

def unlink_client_book(db: Session, token: str, book_id: int):
    client = db.query(Client).filter(Client.token == token).first()
    if client:
        book = db.query(Book).filter(Book.id == book_id).first()
        if book:
            client.borrowed_books.remove(book)
            db.commit()
            return True
    return False
