CREATE TABLE IF NOT EXISTS links (
    id INTEGER PRIMARY KEY,
    link TEXT NOT NULL,
    identifier TEXT UNIQUE,
    TL INTEGER DEFAULT 0
);
--TL means Tracking Level

CREATE TABLE IF NOT EXISTS my_location_table (
    id INTEGER PRIMARY KEY,
    identifier INTEGER,
    ip TEXT NOT NULL,
    user_agent TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    latitude REAL,
    longitude REAL,
    FOREIGN KEY (identifier) REFERENCES links(id)
);

