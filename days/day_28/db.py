import json
from pathlib import Path
def add_user(username, role):
    path = Path("users.json")
    if not path.exists():
        with open(path, "w", encoding="utf-8") as file:
            json.dump({}, file, ensure_ascii=False, indent=4)
    else:
        with open(path, "w", encoding="utf-8") as file:
            json.dump({username:role}, file, ensure_ascii=False, indent=4)
add_user("zen-dix", "admin")