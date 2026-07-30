CREATE TABLE  user_profiles(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL UNIQUE,
  registration_timestamp TEXT
);
