from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from dotenv import load_dotenv
import os
from app import crud, models, database, schemas, dependencies

load_dotenv()

app = FastAPI()

# Database Initialization
database.Base.metadata.create_all(bind=database.engine)

# Token
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

# OAuth2PasswordBearer is a class that will help you get the token from the request
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Token function to verify token and get user information
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = schemas.TokenData(**payload)
    except JWTError:
        raise credentials_exception
    return token_data

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Add logic for validating username and password and issuing access token
    # For simplicity, we're not implementing user authentication here
    # You should replace this with your own authentication logic
    pass

@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(database.get_db)):
    return crud.create_author(db=db, author=author)

@app.get("/authors/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(database.get_db)):
    return crud.get_author(db=db, author_id=author_id)

@app.get("/authors/", response_model=List[schemas.Author])
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_authors(db=db, skip=skip, limit=limit)

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_books(db=db, skip=skip, limit=limit)

@app.get("/books/by_author/{author_id}", response_model=List[schemas.Book])
def read_books_by_author(author_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_books_by_author(db=db, author_id=author_id, skip=skip, limit=limit)

@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(database.get_db)):
    return crud.create_client(db=db, client=client)

@app.get("/clients/", response_model=List[schemas.Client])
def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_clients(db=db, skip=skip, limit=limit)

@app.get("/clients/books/", response_model=List[schemas.Book])
def read_client_books(current_user: schemas.TokenData = Depends(dependencies.get_current_user), db: Session = Depends(database.get_db)):
    return crud.get_client_books(db=db, token=current_user.sub)

@app.post("/clients/books/link/{book_id}", response_model=bool)
def link_client_book(book_id: int, current_user: schemas.TokenData = Depends(dependencies.get_current_user), db: Session = Depends(database.get_db)):
    return crud.link_client_book(db=db, token=current_user.sub, book_id=book_id)

@app.post("/clients/books/unlink/{book_id}", response_model=bool)
def unlink_client_book(book_id: int, current_user: schemas.TokenData = Depends(dependencies.get_current_user), db: Session = Depends(database.get_db)):
    return crud.unlink_client_book(db=db, token=current_user.sub, book_id=book_id)
