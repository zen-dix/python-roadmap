"""(Сложная / Итоговая, 20 мин) Спроектируй класс DatabaseManager для управления таблицей users.  Метод __init__(self, db_name: str) должен подключаться к БД (можно использовать ':memory:' для этой задачи) и автоматически создавать таблицу users (id, username, role), если её нет.Реализуй метод add_user(self, username: str, role: str), который добавляет пользователя и выводит лог.Реализуй метод get_users_by_role(self, role: str) -> list, возвращающий список пользователей с указанной ролью.Продемонстрируй работу: создай экземпляр класса, добавь пользователей ('admin_gleb', 'admin'), ('guest_1', 'user'), ('moderator_x', 'admin'). Затем вызови метод получения всех admin и распечатай их.Ожидаемый вывод:PlaintextUser admin_gleb initialized.
User guest_1 initialized.
User moderator_x initialized.
Admins list: [('admin_gleb', 'admin'), ('moderator_x', 'admin')]"""

import sqlite3


class DatabaseManager:
    def __init__(self, db_name: str):
        self.db_name = db_name
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    role TEXT
                );
            """)

    def add_user(self, username: str, role: str):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            user_data = (username, role)
            cursor.execute(
                "INSERT INTO users (username, role) VALUES (?, ?)", user_data
            )
            print(f"User {username} initialized.")

    def get_users_by_role(self, role: str) -> list:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT username, role FROM users")
            return cursor.fetchall()


database = DatabaseManager("users.db")
database.add_user("admin_gleb", "admin")
database.add_user("guest_1", "user")
database.add_user("moderator_x", "admin")
