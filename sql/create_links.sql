CREATE TABLE IF NOT EXISTS links (
    id INTEGER PRIMARY KEY,
    link TEXT NOT NULL,
    identifier TEXT UNIQUE,
    TL INTEGER DEFAULT 0
);
--TL means Tracking Level

