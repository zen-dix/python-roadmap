"""Задача 4: Агрегация через JOIN (Сложная, 15 мин)  В базе есть две таблицы: users (id, username) и orders (id, user_id, amount). Напиши SQL-запрос (и функцию для его выполнения), который объединяет эти таблицы и возвращает список всех пользователей вместе с суммарным объёмом их заказов. Отсортируй результат по убыванию суммы. Если заказов у пользователя нет, сумма должна отображаться как 0 (потребуется функция COALESCE или IFNULL).Ожидаемый результат: Список кортежей, например: [('zen-dix', 15000), ('guest_01', 0)]."""

import sqlite3


def get_users_summary(cursor):
    cursor.execute("""
        SELECT users.username, COALESCE(SUM(orders.amount), 0) AS total
        FROM users
        LEFT JOIN orders ON users.id = orders.user_id
        GROUP BY users.id
        ORDER BY total DESC;
    """)
    return cursor.fetchall()


conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT
    );
""")
cursor.execute("""
    CREATE TABLE orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount INTEGER
    );
""")

cursor.execute("INSERT INTO users (username) VALUES (?)", ("zen-dix",))
user_id = cursor.lastrowid
cursor.execute("INSERT INTO orders (user_id, amount) VALUES (?, ?)", (user_id, 15000))

cursor.execute("INSERT INTO users (username) VALUES (?)", ("guest_01",))

get_users_summary(cursor)
print(get_users_summary(cursor))
conn.close()
