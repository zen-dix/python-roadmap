"""
Задание 2: Генерация моковых данных пользователей (task2.py)Сложность: 4/10Время: 15 минЦель: Освоить генерацию тестовых данных (seed/mock data) для бэкенда с помощью библиотеки faker.  Условие: Создай функцию generate_users(). Она должна сгенерировать список из 10 пользователей, где каждый пользователь — словарь с ключами "name" и "email" (используй faker.Faker()). Запиши полученный список в файл users.json с отступами в 4 пробела.  Входные данные: Отсутствуют.Вывод: Сформированный файл users.json со структурой:JSON[
    {
        "name": "John Doe",
        "email": "johndoe@example.com"
    }
]

"""
import faker
import json
def generate_users():
    lst = []
    for i in range(10):
        fake = faker.Faker()
        lst.append({"name": fake.name(), "email": fake.email()})
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(lst, file,  ensure_ascii = False, indent = 4)

