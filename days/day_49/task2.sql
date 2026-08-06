/*
Задача 2 (Легкая, 7 мин)
Даны таблицы:

    services (id, service_name)

    logs (id, service_id, error_message)
    Напиши LEFT JOIN запрос, который выведет названия всех сервисов и тексты ошибок из логов.
    Условие: В выводе должны быть даже те сервисы, у которых нет ошибок (в столбце error_message будет NULL).

*/
CREATE TABLE services (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  service_name TEXT
);
CREATE TABLE logs(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  service_id INTEGER,
  error_message TEXT
);
INSERT INTO services (service_name)
VALUES
  ('Dolphin'),
  ('Obsidian'),
  ('Steam'),
  ('Neovim');
INSERT INTO logs (service_id, error_message)
VALUES
  (1, 'Memory is empty'),
  (2, NULL),
  (3, 'Proton is not enable');
SELECT services.service_name, logs.error_message
FROM services
LEFT JOIN logs ON services.id = logs.service_id;

