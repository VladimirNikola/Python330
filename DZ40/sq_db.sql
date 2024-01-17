CREATE TABLE IF NOT EXISTS mainmenu(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    price TEXT NOT NULL,
    text TEXT NOT NULL,
    url TEXT NOT NULL,
    time INTEGER NOT NULL
);



