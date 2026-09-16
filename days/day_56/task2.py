"""2. [Лёгкая, ~7 мин] Дан список items = ["book", "pen", "notebook", "pencil", "eraser"] и список задержек delays = [0.5, 1.0, 0.3, 0.8, 1.2] (индексы соответствуют). Напиши fetch_item(item, delay), которая спит delay секунд и возвращает dict {"item": item, "status": "ready"}. Через list comprehension собери список корутин и запусти их все gather-ом. Выведи результаты — порядок должен соответствовать исходному списку items."""

import asyncio

items = ["book", "pen", "notebook", "pencil", "eraser"]
delays = [0.5, 1.0, 0.3, 0.8, 1.2]


async def fetch_item(item, delay):
    await asyncio.sleep(delay)
    return {"item": item, "status": "ready"}


coroutines = [fetch_item(item, delay) for item, delay in zip(items, delays)]


async def main():
    res = await asyncio.gather(*coroutines)
    print(*res, sep="\n")


asyncio.run(main())
