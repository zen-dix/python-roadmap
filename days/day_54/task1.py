"""Проверка сервера — лёгкая, ~6 мин

Напишите корутину check_server(name): печатает f"Checking {name}...", ждёт await asyncio.sleep(1), печатает f"{name} is online". Запустите через asyncio.run().

Входные данные: name = "auth-service" — передаётся в коде как аргумент при вызове.
Ожидаемый результат:
Checking auth-service...
auth-service is online"""

import asyncio


async def check_server(name):
    print(f"Checking {name}...")
    await asyncio.sleep(1)
    print(f"{name} is online")


name = "auth-service"
asyncio.run(check_server(name))
