CREATE TABLE IF NOT EXISTS data (
    id SERIAL PRIMARY KEY,
    identifier TEXT NOT NULL,
    ip VARCHAR(15) NOT NULL,
    user_agent TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
