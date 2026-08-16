"""Задача 1: Безопасный SELECT (Лёгкая, 10 мин)
Ниже представлен кусок кода, который ищет email пользователя по username. Он нарушает базовые стандарты безопасности. Перепиши эту функцию: избавься от f-строк, используй параметризованный запрос и добавь аннотации типов для аргументов и возвращаемого значения.  Python# Исходный код:
def get_user_email(username, cursor):
    query = f"SELECT email FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()
Входные данные: username = "admin".Ожидаемый результат: Отрефакторенный код, возвращающий ('admin@localhost',) или None."""

import sqlite3

from typing import Optional, Tuple


def get_user_email(username: str, cursor: sqlite3.Cursor) -> Optional[Tuple[str, ...]]:
    query = "SELECT email FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchone()
