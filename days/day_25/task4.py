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

