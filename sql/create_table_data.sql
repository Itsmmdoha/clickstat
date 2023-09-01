CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    identifier TEXT NOT NULL,
    ip VARCHAR(15) NOT NULL,
    user_agent TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (identifier) REFERENCES links(id)
);


