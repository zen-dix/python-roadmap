/*
Задача 1 (Легкая, 5 мин)  Дана таблица users с колонками id, username, is_active.Условие: Добавь в систему нового пользователя.Входные данные: username = 'backend_dev', is_active = 1. Поле id заполняется автоматически (указывать не нужно).Ожидаемый результат в таблице:Plaintextid | username    | is_active
1  | backend_dev | 1
*/

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  is_active INTEGER NOT NULL
);
INSERT INTO users (username, is_active)
  VALUES ('backend_dev', 1);
SELECT  username, is_active
FROM users
