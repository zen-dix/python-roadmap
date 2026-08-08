"""
(Легкая, 10 мин) Напиши функцию add_server(ip: str, status: str) -> None, которая принимает IP и статус, подключается к backend.db с использованием контекстного менеджера with и добавляет сервер в таблицу servers. Не забудь про безопасную параметризацию запроса (?). Вызови функцию для IP 192.168.1.10 и статуса active.
"""

import sqlite3


def add_server(ip: str, status: str) -> None:
    with sqlite3.connect("backend.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS servers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT,
                status TEXT
            )
        """)
        cursor.execute(
            "INSERT INTO servers (ip_address, status) VALUES (?, ?)",
            (ip, status),
        )
    print(f"Server {ip} added.")


add_server("192.168.1.10", "active")
