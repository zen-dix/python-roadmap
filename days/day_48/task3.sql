/*

Задача 3 (Средняя, 10 мин)  Дана таблица server_logs с колонками id, level, message.Условие: База данных переполнена мусорными логами. Напиши запрос, который удалит все логи уровня 'DEBUG'.До удаления:Plaintextid | level | message
1  | ERROR | Failed to connect
2  | DEBUG | Variable initialized
Ожидаемый результат:Plaintextid | level | message
1  | ERROR | Failed to connect
*/
CREATE TABLE server_logs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  level TEXT,
  message TEXT
);
INSERT INTO server_logs(level, message)
VALUES
  ('ERROR', 'Failed to connect'),
  ('DEBUG', 'Variable initialized');
SELECT id, level, message
FROM server_logs;
DELETE FROM server_logs
WHERE level = 'DEBUG';
SELECT id, level, message 
FROM server_logs;
