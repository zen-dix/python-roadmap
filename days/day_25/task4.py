"""Задание 4: Подсчет статистики почтовых доменов (task4.py)Сложность: 5/10Время: 15 минЦель: Закрепить навыки работы со строками и агрегации данных в словари.Условие: Напиши функцию email_count(). Функция должна прочитать users.json, извлечь из каждого почтового адреса доменную часть (всё, что идет после @), посчитать количество пользователей для каждого домена и вывести итоговый словарь в консоль.  Входные данные: Файл users.json.Вывод: Словарь в консоли вида {'gmail.com': 4, 'yahoo.com': 2, ...}."""
import json
def email_count():
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)
    dct = {}
    for user in users:
        ind = user["email"].index("@")
        email = user["email"][ind+1:]
        dct[email] = dct.get(email, 0) + 1
    print(dct)

