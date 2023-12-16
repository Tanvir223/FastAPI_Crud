-- Create books table
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    UNIQUE (title, author_id)
);

-- Create authors table
CREATE TABLE IF NOT EXISTS authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE
);

-- Create clients table
CREATE TABLE IF NOT EXISTS clients (
    id SERIAL PRIMARY KEY,
    token VARCHAR(255) UNIQUE
);

-- Create borrowings table
CREATE TABLE IF NOT EXISTS borrowings (
    book_id INTEGER,
    client_id INTEGER,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (client_id) REFERENCES clients(id),
    PRIMARY KEY (book_id, client_id)
);
