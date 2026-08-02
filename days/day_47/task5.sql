/*
Задача 5 (Сложная, 15 мин)
Напиши запрос, который выведет hostname и load_avg двух самых ненагруженных (с наименьшим load_avg) серверов среди тех, которые сейчас находятся в статусе 'online'.
Ожидаемый вывод:
Plaintext

worker-02|0.5
web-01|1.2
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
SELECT hostname, load_avg
FROM servers
WHERE status = 'online'
ORDER BY load_avg ASC
LIMIT 2;
