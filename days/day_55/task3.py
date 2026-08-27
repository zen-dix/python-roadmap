"""3. Fetch three pages concurrently (10 мин)
Дан словарь page_delays = {"home": 0.5, "about": 0.2, "contact": 0.3} (имитация времени ответа сервера). Напиши fetch_page(name, delay) — print старт/финиш, возвращает f"<{name}> loaded". В main создай задачи для всех страниц через create_task, собери результаты циклом в список results в исходном порядке словаря, выведи список и общее время.
Ожидаемый результат: список в порядке home/about/contact, время ≈ 0.5s."""

import asyncio
import time


async def fetch_page(name, delay):
    print(f"start {name}")
    await asyncio.sleep(delay)
    print(f"end {name}")
    return f"<{name}> loaded"


async def main(dct):
    start = time.monotonic()
    tasks = [
        asyncio.create_task(fetch_page(name, delay)) for name, delay in dct.items()
    ]
    results = []
    for task in tasks:
        result = await task
        results.append(result)
    for res in results:
        print(res)
    end = time.monotonic()
    print(round(end - start, 1))


page_delays = {"home": 0.5, "about": 0.2, "contact": 0.3}

asyncio.run(main(page_delays))
