CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    identifier TEXT NOT NULL,
    ip TEXT NOT NULL,
    user_agent TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    latitude REAL,
    longitude REAL,
    FOREIGN KEY (identifier) REFERENCES links(id)
);


