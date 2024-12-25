-- Add and populate the books table.
CREATE TABLE IF NOT EXISTS books (
    book_id SERIAL PRIMARY KEY,
    goodreads_book_id INTEGER,
    best_book_id INTEGER,
    work_id INTEGER,
    books_count INTEGER,
    isbn VARCHAR(20),
    isbn13 VARCHAR(20),
    authors TEXT,
    original_publication_year FLOAT,
    original_title TEXT,
    title TEXT,
    language_code VARCHAR(10),
    average_rating FLOAT,
    ratings_count INTEGER,
    work_ratings_count INTEGER,
    work_text_reviews_count INTEGER,
    ratings_1 INTEGER,
    ratings_2 INTEGER,
    ratings_3 INTEGER,
    ratings_4 INTEGER,
    ratings_5 INTEGER,
    image_url TEXT,
    small_image_url TEXT
);

\copy books FROM 'C:\Users\yezda\OneDrive\IOT\FOP\assignment4\books.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8');

----------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------

--Add and populate the book_tags table.

CREATE TABLE IF NOT EXISTS book_tags(
goodreads_book_id INTEGER,
tag_id INTEGER,
count INTEGER
);

\copy book_tags FROM 'C:\Users\yezda\OneDrive\IOT\FOP\assignment4\book_tags(1).csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8');

---------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------

-- create and populate the tags table

CREATE TABLE IF NOT EXISTS tags(
    tag_id INTEGER,
    tag_name VARCHAR(50)
);

\copy tags FROM 'C:\Users\yezda\OneDrive\IOT\FOP\assignment4\tags.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8');

---------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------
 
--create and populate the ratings table

CREATE TABLE IF NOT EXISTS ratings(
    user_id INTEGER,
    book_id INTEGER,
    rating INTEGER
);

\copy ratings FROM 'C:\Users\yezda\OneDrive\IOT\FOP\assignment4\ratings.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8');

---------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------

--create and populate the to_read table

CREATE TABLE IF NOT EXISTS to_read(
    user_id INTEGER,
    book_id INTEGER
);

\copy to_read from 'C:\Users\yezda\OneDrive\IOT\FOP\assignment4\to_read.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8');