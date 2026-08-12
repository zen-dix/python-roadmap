"""
Задача 5: Итоговая задача — Менеджер базы данных (Сложная, 30 мин)  Объединим ООП, обработку исключений и SQL. Напиши класс DBManager, который инкапсулирует логику работы с базой.Требования к классу:Метод __init__(self, db_name: str): устанавливает соединение, создает курсор и таблицу api_tokens (id INTEGER PRIMARY KEY, service TEXT UNIQUE, token TEXT, is_active INTEGER).Метод add_token(self, service: str, token: str) -> None: добавляет новый сервис (поле is_active равно 1 по умолчанию). Оберни execute в блок try/except sqlite3.IntegrityError, чтобы перехватывать попытку добавить существующий service (так как поле UNIQUE). При ошибке выведи в консоль Error: Service already exists..Метод get_active_tokens(self) -> list: возвращает список кортежей с сервисами, где is_active = 1.Метод deactivate_token(self, service: str) -> None: обновляет is_active на 0 для конкретного сервиса.Метод __del__(self): магический метод, который гарантирует вызов self.connection.close() при уничтожении объекта сборщиком мусора, предотвращая утечку ресурсов.Пример использования:Pythondb = DBManager("tokens.db")
db.add_token("GitHub", "ghp_12345...")
db.add_token("OpenAI", "sk-abcdef...")
db.add_token("GitHub", "ghp_duplicate...") # Должно вызвать перехват IntegrityError
db.deactivate_token("GitHub")
print(db.get_active_tokens())"""

import sqlite3


class DBManager:
    def __init__(self, db_name: str):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS api_tokens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT UNIQUE,
                token TEXT,
                is_active INTEGER
            );
        """)
        self.connection.commit()

    def add_token(self, service: str, token: str) -> None:
        try:
            self.cursor.execute(
                "INSERT INTO api_tokens (service, token, is_active) VALUES (?, ?, 1)",
                (service, token),
            )
            self.connection.commit()
        except sqlite3.IntegrityError:
            print("Error: Service already exists.")

    def get_active_tokens(self) -> list:
        self.cursor.execute("SELECT * FROM api_tokens WHERE is_active = 1")
        return self.cursor.fetchall()

    def deactivate_token(self, service: str) -> None:
        self.cursor.execute(
            "UPDATE api_tokens SET is_active = 0 WHERE service = ?",
            (service,),
        )
        self.connection.commit()

    def __del__(self):
        if hasattr(self, "connection"):
            self.connection.close()


db = DBManager("tokens.db")
db.add_token("GitHub", "ghp_12345...")
db.add_token("OpenAI", "sk-abcdef...")
db.add_token("GitHub", "ghp_duplicate...")  # Должно вызвать перехват IntegrityError
db.deactivate_token("GitHub")
print(db.get_active_tokens())
