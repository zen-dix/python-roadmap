import task2, task3, task4, json
try:
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)
except FileNotFoundError:
    task2.generate_users()
task3.show_emails()
task4.email_count()