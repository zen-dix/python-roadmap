"""Задача 4: Безопасное удаление (Средняя, 10 мин)  Напиши функцию delete_out_of_stock() -> None, которая удаляет из таблицы products все товары, у которых stock = 0. Функция должна выводить в консоль количество удаленных записей. Проверь её работу: добавь тестовый товар с нулевым остатком и вызови функцию.Ожидаемый результат в консоли: Deleted products: 1"""

import sqlite3


def delete_out_of_stock() -> None:
    with sqlite3.connect("products.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE stock = 0")
    print(f"Deleted products: {cursor.rowcount}")


delete_out_of_stock()
