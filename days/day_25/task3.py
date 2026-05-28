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

