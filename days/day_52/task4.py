"""Задача 4. Итоговая задача: Инкапсуляция логики (Сложная, 30 мин)
Эта задача объединяет текущую тему таблиц с концепциями ООП из предыдущей фазы. Создай модуль store_db.py.  Напиши класс StoreDB, который при инициализации (__init__) подключается к базе store.db и создаёт таблицы categories (id, name) и products (id, name, price, category_id).  Добавь методы класса: add_category(name), add_product(name, price, category_id) и get_catalog().  Метод get_catalog должен использовать JOIN и возвращать список кортежей вида (название_товара, цена, название_категории).  Пример входных данных: db = StoreDB(), db.add_category("Electronics"), db.add_product("Keyboard", 100, 1), print(db.get_catalog()).  Ожидаемый результат вывода в консоль: Catalog: [("Keyboard", 100, "Electronics")]"""

import sqlite3


class StoreDB:
    def __init__(self):
        self.conn = sqlite3.connect("store.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                category_id INTEGER
            );
        """)

    def add_category(self, name):
        self.cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        self.conn.commit()

    def add_product(self, name, price, category_id):
        self.cursor.execute(
            "INSERT INTO products (name, price, category_id) VALUES (?, ?, ?)",
            (name, price, category_id),
        )
        self.conn.commit()

    def get_catalog(self):
        self.cursor.execute(
            "SELECT products.name, products.price, categories.name FROM categories JOIN products ON categories.id = products.category_id"
        )
        return self.cursor.fetchall()


db = StoreDB()
db.add_category("Electronics")
db.add_product("Keyboard", 100, 1)
print(db.get_catalog())
