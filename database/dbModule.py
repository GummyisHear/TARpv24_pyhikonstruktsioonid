from sqlite3 import *

tablesSql = """
-- Keeled
CREATE TABLE IF NOT EXISTS languages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);

-- Riigid
CREATE TABLE IF NOT EXISTS countries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);

-- Žanrid
CREATE TABLE IF NOT EXISTS genres (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);

-- Režissöörid
CREATE TABLE IF NOT EXISTS directors (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);

-- Filmid (viidete kaudu seotud ülejäänud tabelitega)
CREATE TABLE IF NOT EXISTS movies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  director_id INTEGER,
  release_year INTEGER,
  genre_id INTEGER,
  duration INTEGER,
  rating REAL,
  language_id INTEGER,
  country_id INTEGER,
  description TEXT,
  FOREIGN KEY (director_id) REFERENCES directors(id),
  FOREIGN KEY (genre_id) REFERENCES genres(id),
  FOREIGN KEY (language_id) REFERENCES languages(id),
  FOREIGN KEY (country_id) REFERENCES countries(id)
);
"""

def initDb():
    try:
        conn = connect('movies.db')
        cursor = conn.cursor()

        cursor.executescript(tablesSql)
        createMoviesTable(cursor)

        conn.commit()
        conn.close()
    except:
        if (conn): 
            conn.close()
        raise Exception("Viga!")

def createMoviesTable(cursor:Cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    director TEXT,
    release_year INTEGER,
    genre TEXT,
    duration INTEGER,
    rating REAL,
    language TEXT,
    country TEXT,
    description TEXT
    );
    """)

    cursor.execute("SELECT COUNT(*) FROM movies")
    count = cursor.fetchone()[0]
    if count == 0:
        populateMoviesTable(cursor)

def populateMoviesTable(cursor:Cursor):
    cursor.execute("""
    INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description) VALUES
    ('The From In With.', 'Francis Ford Coppola', 1994, 'Drama', 142, 9.3, 'English', 'USA', 'The In With By On. A In From By The At. On A With By By On To A.'),
    ('The By On To.', 'Christopher Nolan', 2010, 'Sci-Fi', 148, 8.8, 'English', 'UK', 'The A The On The In. By To A At On The. From The In With At In To A.'),
    ('In The With On.', 'Quentin Tarantino', 1972, 'Crime', 175, 9.2, 'English', 'USA', 'On From The By At The A. In From By With To On. A The By In With At On To A.'),
    ('The A To From.', 'Steven Spielberg', 1994, 'Adventure', 154, 8.9, 'English', 'France', 'With By In The A On. The With To A At The From. On A From With At By The.'),
    ('On The From With.', 'Martin Scorsese', 2008, 'Action', 152, 9.0, 'English', 'Germany', 'The A By On In The. At With To A From On The. With On By The A In To From.'),
    ('From The By With.', 'Christopher Nolan', 1960, 'Drama', 134, 8.5, 'English', 'UK', 'The A On From The At. With To By In A The On. At The In From With By To A.'),
    ('The By On A.', 'Francis Ford Coppola', 1999, 'Thriller', 112, 7.8, 'English', 'USA', 'A The On By In The At. From With A On By To The. In The By With At A From.'),
    ('On A The From.', 'Quentin Tarantino', 2015, 'Comedy', 126, 7.9, 'English', 'Italy', 'By With A On In The From. The By At A With On To. At In The By From With A.'),
    ('By The On From.', 'Steven Spielberg', 1975, 'Action', 143, 8.7, 'English', 'France', 'A With On The By From In. The A At On With To From. By In The A From With At On.'),
    ('From With The By.', 'Martin Scorsese', 1980, 'Crime', 163, 9.1, 'English', 'Germany', 'On The A By In The From. With By On A The In From. To The In At By With On A.');
    """)

def selectAll(table:str, cursor:Cursor = None, query="")->list[any]:
    if (not cursor):
        conn = connect('movies.db')
        cursor = conn.cursor()

    rows = cursor.execute(f"SELECT * FROM {table} WHERE {query or True}").fetchall()
    for row in rows:
        print(row)
    return rows



