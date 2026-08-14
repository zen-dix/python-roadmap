"""Задача 3. Агрегация данных (Средняя, 15 мин)  Реализуй функцию count_articles_per_author(). Она должна подсчитывать количество написанных статей для каждого автора, используя SQL-функцию COUNT() и группировку GROUP BY.Ожидаемый результат (возврат из функции): [("admin", 1)].  Пример вывода в консоль: Author stats: [("admin", 1)]."""

import sqlite3


def count_articles_per_author():
    with sqlite3.connect("blog.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT authors.name, COUNT(articles.id) FROM authors LEFT JOIN articles ON authors.id = articles.author_id GROUP BY authors.name"
        )
        return cursor.fetchall()


print(f"Author stats: {count_articles_per_author()}")
