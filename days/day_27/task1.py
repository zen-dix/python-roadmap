from task2 import settings
import json
setting = settings()
with open("setting.json", "w", encoding="utf-8") as file:
    json.dump(setting, file, ensure_ascii=False, indent=4)