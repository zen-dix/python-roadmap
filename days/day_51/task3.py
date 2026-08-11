"""Задача 3: Обновление запасов (Средняя, 10 мин)  Напиши функцию update_stock(product_id: int, new_stock: int) -> bool. Функция должна обновить поле stock для товара с указанным id. Верни True, если товар был найден и обновлен (используй проверку через cursor.rowcount), и False, если товара с таким id нет. Не забудь commit().Входные данные: update_stock(1, 8)Ожидаемый результат: Функция возвращает True. Повторный SELECT для id=1 покажет stock = 8."""

import sqlite3


def update_stock(product_id: int, new_stock: int) -> bool:
    with sqlite3.connect("products.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE products SET stock = (?) WHERE id = (?)",
            (new_stock, product_id),
        )
        return cursor.rowcount > 0


print(update_stock(1, 0))
print(update_stock(423, 1))
