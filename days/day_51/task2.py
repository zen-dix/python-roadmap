"""Задача 2: Поиск с параметром (Легкая, 10 мин)  Используя таблицу products из Задачи 1, напиши функцию get_affordable_products(max_price: float) -> list, которая делает SELECT запрос и возвращает список товаров, цена которых меньше или равна max_price.Входные данные: get_affordable_products(50.0)Ожидаемый результат: [(2, 'Mouse', 25.0, 50)]"""

import sqlite3


def get_affordable_products(max_price: float) -> list:
    with sqlite3.connect("products.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE price <= (?)", (max_price,))
        return cursor.fetchall()


print(get_affordable_products(50.0))
