"""
Задача 6 (Повторение ООП, Средняя, 10 мин)
Напиши Python-класс DatabaseConfig, который при инициализации (__init__) принимает host, port, user и скрытый атрибут __password.
Реализуй метод get_dsn(), который возвращает строку подключения в формате:
"postgres://<user>:********@<host>:<port>" (пароль должен быть заменен на звездочки при выводе).
Входные данные в коде:  Pythondb = DatabaseConfig("localhost", 5432, "admin", "supersecret")
print(db.get_dsn())
  Ожидаемый вывод:postgres://admin:********@localhost:5432
"""


class DatabaseConfig:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.__password = password

    def get_dsn(self):
        return f"postgres://{self.user}:{len(self.__password) * '*'}@{self.host}:{self.port}"


db = DatabaseConfig("localhost", 5432, "admin", "supersecret")
print(db.get_dsn())
