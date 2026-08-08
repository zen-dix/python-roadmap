"""Задание 3: Форматированный CLI-вывод и обработка ошибок (task3.py)Сложность: 4/10Время: 15 минЦель: Научиться выводить структурированные данные в виде таблиц через tabulate и обрабатывать отсутствие файла.  Условие: Реализуй функцию show_emails(). Функция должна читать users.json и выводить данные в виде таблицы в консоль. Если файл users.json не найден, перехвати FileNotFoundError и выведи красным цветом сообщение: "Файл не найден. Сначала запустите task2.py".  Входные данные: Файл users.json.Вывод: Таблица с заголовками или цветная ошибка в терминале."""

import json
from tabulate import tabulate
from termcolor import cprint
def show_emails():
    def display_users(lst):
        print(tabulate(lst, headers="keys"))
    try:
        with open("users.json", "r", encoding="utf-8") as file:
            users = json.load(file)
        display_users(users)
    except FileNotFoundError:
        cprint("Файл не найден. Сначала запустите task2.py", (255,0,0))

