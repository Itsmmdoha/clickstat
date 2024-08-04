CREATE TABLE IF NOT EXISTS links (
    id SERIAL PRIMARY KEY,
    url TEXT NOT NULL,
    owner_ip VARCHAR(15) NOT NULL,
    identifier VARCHAR(6) UNIQUE,
    TL INTEGER DEFAULT 0,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
--TL means Tracking Level

CREATE TABLE IF NOT EXISTS data (
    id SERIAL PRIMARY KEY,
    identifier TEXT NOT NULL,
    ip VARCHAR(15) NOT NULL,
    user_agent TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
