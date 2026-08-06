/*
Задача 1 (Легкая, 5 мин)
Даны две таблицы:

    users (id, email)

    profiles (id, user_id, bio, github_link)
    Напиши запрос, который выведет email пользователя и его github_link. Используй INNER JOIN.
*/
CREATE TABLE users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT
);
CREATE TABLE profiles(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  bio TEXT,
  github_link TEXT
);
INSERT INTO users (email)
VALUES
  ('linux@gmail.com'),
  ('frebsd@gmail.com');
INSERT INTO profiles (user_id, bio, github_link)
VALUES
  (1, '', 'github.com/....'),
  (2, '', 'github.com/super_programmer');
SELECT users.email, profiles.github_link
FROM users
INNER JOIN profiles ON users.id = profiles.user_id;
