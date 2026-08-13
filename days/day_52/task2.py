"""Задача 2. Извлечение с помощью JOIN (Средняя, 15 мин)  Используя базу данных из первой задачи, напиши функцию get_articles_with_authors(). Она должна выполнять SQL-запрос с использованием JOIN и возвращать список всех статей вместе с именами их авторов.Ожидаемый результат (возврат из функции): [("My first backend", "admin")].  Пример вывода в консоль: Result: [("My first backend", "admin")]."""

import sqlite3


def get_articles_with_authors():
    with sqlite3.connect("blog.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT articles.title, authors.name FROM authors JOIN articles ON authors.id = articles.author_id"
        )
        return cursor.fetchall()


print(f"Result: {get_articles_with_authors()}")
