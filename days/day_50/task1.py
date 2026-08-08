"""
(Легкая, 10 мин) Напиши скрипт, который подключается к файлу backend.db и создает таблицу servers с полями id (INTEGER PRIMARY KEY), ip_address (TEXT), status (TEXT). Закрой соединение после выполнения.

    Ожидаемый вывод (в консоли через print): Table 'servers' created successfully.
"""

import sqlite3

with sqlite3.connect("backend.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE servers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip_address TEXT,
        status TEXT
    );
    """)
    print("Table 'servers' created successfully.")
