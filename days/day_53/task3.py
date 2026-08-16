"""Задача 3: Каскадное обновление (Средняя, 15 мин)
Реализуй функцию, которая деактивирует пользователей, не заходивших в систему определенное количество дней. Таблица users содержит столбцы id, last_login (в формате YYYY-MM-DD) и is_active (boolean). Обновление должно выполняться одним запросом UPDATE.  Входные данные: Аргументы функции days_limit = 30 и текущая дата (например, 2026-08-16).Ожидаемый результат: Значение is_active меняется на False для подходящих пользователей. Функция возвращает cursor.rowcount (число изменённых строк)."""

import sqlite3
from datetime import datetime, timedelta


def deactivate_not_active_users(cursor, date_limit: int, date_str: str):
    current_date = datetime.strptime(date_str, "%Y-%m-%d")
    target_date = current_date - timedelta(days=date_limit)
    target_date_str = target_date.strftime("%Y-%m-%d")
    cursor.execute(
        "UPDATE users SET is_active = ? WHERE last_login < ?", (0, target_date_str)
    )
    return cursor.rowcount


conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        last_login TEXT,
        is_active INTEGER 
    );
""")
cursor.executemany(
    "INSERT INTO users (last_login, is_active) VALUES (?, ?)",
    [("2026-08-16", 1), ("2026-07-13", 1), ("2026-08-13", 0)],
)
print(deactivate_not_active_users(cursor, 30, "2026-08-16"))
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
conn.close()
