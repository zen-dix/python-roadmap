import faker 
import json
def generate_users():
    lst = []
    for i in range(10):
        fake = faker.Faker()
        lst.append({"name": fake.name(), "email": fake.email()})
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(lst, file,  ensure_ascii = False, indent = 4)

