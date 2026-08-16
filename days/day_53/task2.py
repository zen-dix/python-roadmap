"""Задача 2: Множественная вставка данных (Средняя, 10 мин)  При инициализации приложения часто нужно загрузить базовые данные. Напиши функцию, которая принимает список словарей и добавляет их в таблицу users (столбцы login, role) за один запрос, используя метод executemany.Входные данные (передаются в коде):Pythonusers_data = [
    {"login": "zen-dix", "role": "admin"},
    {"login": "guest_01", "role": "user"},
    {"login": "moderator", "role": "moderator"}
]
Ожидаемый результат: Три новые записи в базе. Функция должна возвращать количество добавленных строк."""


def add_users(users, cursor):
    cursor.executemany("INSERT INTO users (login, role) VALUES (:login, :role)", users)
    return cursor.rowcount


users_data = [
    {"login": "zen-dix", "role": "admin"},
    {"login": "guest_01", "role": "user"},
    {"login": "moderator", "role": "moderator"},
]
