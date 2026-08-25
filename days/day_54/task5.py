"""5. Итоговая: вход пользователя — ~12 мин

Три корутины:

authenticate(username, password) — ждёт await asyncio.sleep(1), возвращает True, если password == "qwerty123", иначе False.
load_profile(username) — ждёт await asyncio.sleep(1), возвращает {"username": username, "role": "developer"}.
log_action(username, action) — ждёт await asyncio.sleep(0.3), печатает f"[LOG] {username}: {action}".

В main(): вызовите authenticate для username = "gleb", password = "qwerty123". Если вход успешен — дождитесь load_profile, выведите профиль, вызовите log_action(username, "login success"). Если нет — выведите "Access denied", вызовите log_action(username, "login failed") без вызова load_profile.

Входные данные: username = "gleb", password = "qwerty123" — передаются в коде как аргументы.
Ожидаемый результат (успешный вход):
{'username': 'gleb', 'role': 'developer'}
[LOG] gleb: login success"""

import asyncio


async def authenticate(username, password):
    await asyncio.sleep(1)
    return password == "qwerty123"


async def load_profile(username):
    await asyncio.sleep(1)
    return {"username": username, "role": "developer"}


async def log_action(username, action):
    await asyncio.sleep(0.3)
    print(f"[LOG] {username}: {action}")


async def main(username, password):
    if await authenticate(username, password):
        profile = await load_profile(username)
        print(profile)
        await log_action(username, "login success")
    else:
        print("Access denied")
        await log_action(username, "login failed")


asyncio.run(main("gleb", "qwerty123"))
