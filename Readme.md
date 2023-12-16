# FastAPI Book Library API

This project is a simple FastAPI-based API for managing a book library. It includes functionalities to add books, edit book details, retrieve lists of books with filtering options, manage authors, create clients, and handle book borrowings.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Project](#running-the-project)
- [API Documentation](#api-documentation)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Features

- Add a book.
- Edit the book's title and author.
- Retrieve a list of books with filtering options for the first letter of the book's title and author.
- Add multiple books by the same author.
- Add an author.
- Create a client.
- Retrieve a list of books borrowed by the client.
- Link a client to a book (client borrowed the book).
- Unlink a client from a book (client returned the book).
- Secured using Bearer authentication with access tokens.
- Dockerized for easy deployment.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

## Project Structure

The project follows a structured directory layout:

- `app/`: Contains the FastAPI application code.
- `docker/`: Includes Docker configuration files.
- `scripts/`: Contains SQL scripts for database initialization.
- `.env`: Environment variables file.
- `requirements.txt`: List of Python dependencies.

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-book-library.git
   cd fastapi-book-library
   ```
Create a virtual environment (optional but recommended):
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

Install dependencies:
   ```bash
    pip install -r requirements.txt
   ```

Set up environment variables:

Create a .env file in the project root with the following content:
    ```bash
        DATABASE_URL=postgresql://user:password@db:5432/booksdb
        SECRET_KEY=mysecretkey
    ```
Replace the database URL, user, password, and secret key with your own values.

Initialize the database:
 ```bash
docker-compose up --build
    ```
