/*
Задача 5 (Сложная, 12 мин)
Даны таблицы:

    api_keys (id, key_string, user_id)

    users (id, username, status)
    Напиши запрос, который выведет username, но только тех пользователей, у которых нет ни одного API-ключа.
    Подсказка: Используй LEFT JOIN и отфильтруй результат с помощью WHERE ... IS NULL по столбцу из правой таблицы. Пользователи со статусом 'banned' не должны попасть в финальную выборку.
*/
CREATE TABLE api_keys(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key_string TEXT,
  user_id INTEGER
);
CREATE TABLE users(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT,
  status TEXT
);

INSERT INTO users (username, status)
VALUES 
  ('flsadjlfs', 'banned'),
  ('oiewuds', 'online'),
  ('ofwwiherf', 'online');
INSERT INTO api_keys (key_string, user_id)
VALUES
  (NULL, 1),
  ('salkdflaslk3ior', 2),
  (NULL, 3);
SELECT users.username
FROM users 
LEFT JOIN api_keys ON users.id = api_keys.user_id
WHERE api_keys.key_string IS NULL AND users.status != 'banned';
