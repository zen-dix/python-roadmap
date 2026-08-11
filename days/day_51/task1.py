"""
Задача 1: Множественная вставка (Легкая, 10 мин)  Напиши скрипт, который создает таблицу products (поля: id INTEGER PRIMARY KEY, title TEXT, price REAL, stock INTEGER) и добавляет в неё список из 3 товаров с помощью executemany. Сделай SELECT и выведи все товары через fetchall().Входные данные: [("Laptop", 1200.50, 10), ("Mouse", 25.00, 50), ("Keyboard", 75.99, 30)]Ожидаемый результат в консоли:[(1, 'Laptop', 1200.5, 10), (2, 'Mouse', 25.0, 50), (3, 'Keyboard', 75.99, 30)]
"""

import sqlite3

with sqlite3.connect("products.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT, 
            price REAL, 
            stock INTEGER
        );
    """)
    stuff = [("Laptop", 1200.50, 10), ("Mouse", 25.00, 50), ("Keyboard", 75.99, 30)]
    cursor.executemany(
        "INSERT INTO products (title, price, stock) VALUES (?, ?, ?)", stuff
    )
    cursor.execute("SELECT * FROM products")
    print(cursor.fetchall())
