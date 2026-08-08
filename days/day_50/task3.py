"""
(Средняя, 10 мин) В коде дан список кортежей: nodes = [('10.0.0.1', 'offline'), ('10.0.0.2', 'active'), ('10.0.0.3', 'maintenance')]. Напиши функцию add_multiple_servers(nodes_list), которая вставит все данные из списка за один запрос, используя метод .executemany().
"""

import sqlite3

nodes = [("10.0.0.1", "offline"), ("10.0.0.2", "active"), ("10.0.0.3", "maintenance")]


def add_multiple_servers(nodes_list):
    with sqlite3.connect("servers.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS servers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            status TEXT
            );
        """)
        cursor.executemany("INSERT INTO servers (ip, status) VALUES (?, ?)", nodes_list)
        print(f"{len(nodes_list)} servers added via executemany")


add_multiple_servers(nodes)
