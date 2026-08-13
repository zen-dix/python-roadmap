"""Задача 1. Базовые связи таблиц (Лёгкая, 15 мин)  Напиши скрипт, создающий базу данных blog.db. Создай таблицу authors (id, name) и таблицу articles (id, title, author_id). Установи внешний ключ. Напиши две функции: add_author(name: str) и add_article(title: str, author_id: int).Данные в запросы должны передаваться строго через аргументы функций.  Пример входных данных: вызовы add_author("admin"), затем add_article("My first backend", 1).  Ожидаемый результат: данные успешно добавлены, скрипт завершается без ошибок."""

import sqlite3

with sqlite3.connect("blog.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        );
    """)


def add_author(name: str):
    with sqlite3.connect("blog.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))


def add_article(title: str, author_id: int):
    with sqlite3.connect("blog.db") as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute(
            "INSERT INTO articles (title, author_id) VALUES (?, ?)", (title, author_id)
        )


add_author("admin")
add_article("My first backend", 1)
