"""2. Разбор кода — средняя, ~7 мин

Дан код:

python
import asyncio
import time

async def load_settings():
    print("Loading settings...")
    time.sleep(1)
    print("Settings loaded")

async def main():
    load_settings()
    print("Server ready")

asyncio.run(main())

Что реально выведет эта программа и в каком порядке? Какие здесь ошибки и как их исправить?"""

import asyncio


async def load_settings():
    print("Loading settings...")
    await asyncio.sleep(1)
    print("Settings loaded")


async def main():
    await load_settings()
    print("Server ready")


asyncio.run(main())
