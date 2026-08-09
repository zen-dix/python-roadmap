"""(Средняя, 10 мин) Напиши функцию get_active_servers() -> list, которая выполняет SELECT запрос к таблице servers, фильтрует записи на уровне SQL (WHERE status = ?) и возвращает список кортежей только с активными серверами. Для получения результата используй cursor.fetchall(). Распечатай результат вызова функции.

Ожидаемый вывод (пример): [('192.168.1.10', 'active'), ('10.0.0.2', 'active')]"""

import sqlite3


def get_active_servers() -> list:
    with sqlite3.connect("servers.db") as conn:
        cursor = conn.cursor()
        # Используем параметризацию вместо жесткого 'active'
        cursor.execute("SELECT ip, status FROM servers WHERE status = ?", ("active",))
        return cursor.fetchall()


# Пример вывода результата
print(get_active_servers())
