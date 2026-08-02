/*
Задача 6 (Итоговая, 15 мин)
Представь, что мы собираем метрики для дашборда. Напиши запрос, который выберет hostname, os и status для серверов, у которых ОС НЕ 'Ubuntu', статус либо 'offline', либо нагрузка load_avg больше 2.0. Отсортируй результат по hostname в алфавитном порядке (по возрастанию) и ограничь вывод 3 записями.
Ожидаемый вывод:
Plaintext

cache-01|CachyOS|offline
web-02|Arch Linux|online
worker-01|Debian|online
*/
CREATE TABLE servers (
    id INTEGER,
    hostname TEXT,
    os TEXT,
    status TEXT,
    load_avg REAL
);

INSERT INTO servers VALUES
(1, 'web-01', 'CachyOS', 'online', 1.2),
(2, 'web-02', 'Arch Linux', 'online', 3.5),
(3, 'db-01', 'Ubuntu', 'maintenance', 0.1),
(4, 'db-02', 'Ubuntu', 'online', 4.8),
(5, 'cache-01', 'CachyOS', 'offline', 0.0),
(6, 'worker-01', 'Debian', 'online', 2.1),
(7, 'worker-02', 'Debian', 'online', 0.5);
SELECT hostname, os, status
FROM servers
WHERE os != 'Ubuntu' AND (status = 'offline' OR load_avg > 2.0)
ORDER BY hostname ASC 
LIMIT 3;

