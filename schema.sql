DROP TABLE IF EXISTS details
CREATE TABLE details (
    email TEXT PRIMARY KEY,
    password TEXT UNIQUE,
    user_type TEXT NOT NULL
    name char,
    rollno number UNIQUE,
    semester varchar)