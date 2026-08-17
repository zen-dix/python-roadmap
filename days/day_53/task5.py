"""Итоговая задача: ООП-обёртка для базы данных (Сложная, 25 мин)
Напиши класс DatabaseManager, который управляет таблицей logs (столбцы id, event_type, message, created_at). Задача объединяет понимание классов и SQLite.
Класс должен работать как контекстный менеджер (использовать магические методы __enter__ и __exit__), чтобы соединение открывалось на старте и безопасно закрывалось (с вызовом commit) при выходе.  Требования к классу:Метод __init__(self, db_path: str).Метод __enter__ возвращает сам объект менеджера.Метод __exit__ закрывает курсор и соединение.Метод log_event(self, event_type: str, message: str) для вставки лога.Метод get_error_count(self) -> int для возврата количества записей с event_type = 'ERROR'.Входные данные:Pythonwith DatabaseManager('app.db') as db:
    db.log_event('INFO', 'System started')
    db.log_event('ERROR', 'Connection timeout')
    print(db.get_error_count())
Ожидаемый результат: Данные успешно вставляются, метод get_error_count возвращает корректное число (например, 1), соединение корректно закрывается."""

import sqlite3


class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT,
                message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        return self

    def __exit__(self, *args):
        if self.conn and self.cursor:
            self.conn.commit()
            self.conn.close()

    def log_event(self, event_type: str, message: str):
        self.cursor.execute(
            "INSERT INTO logs (event_type, message) VALUES (?, ?)",
            (event_type, message),
        )

    def get_error_count(self) -> int:
        self.cursor.execute("SELECT COUNT(*) FROM logs WHERE event_type = 'ERROR'")
        result = self.cursor.fetchone()
        return result[0] if result else 0


with DatabaseManager("app.db") as db:
    db.log_event("INFO", "System started")
    db.log_event("ERROR", "Connection timeout")
    print(f"Количество ошибок: {db.get_error_count()}")
