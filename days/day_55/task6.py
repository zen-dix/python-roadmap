"""6. Итоговая — Mini async downloader (12 мин)
Дан urls_response_time = {"api/users": 0.4, "api/orders": 0.6, "api/products": 0.2, "api/stats": 0.5}. Напиши download(url, delay) — print старт/финиш, asyncio.sleep(delay), возвращает {"url": url, "size_kb": int(delay * 100)}. В main:

Создай задачи для всех url конкурентно.
Собери результаты.
Отсортируй итоговый список по полю "url" по алфавиту.
Выведи отсортированный список и общее время.

Ожидаемый результат: время ≈ 0.6s (max, не сумма 1.7s), список отсортирован: api/orders, api/products, api/stats, api/users."""

import asyncio
import time


async def download(url, delay):
    print(f"start {url}")
    await asyncio.sleep(delay)
    print(f"end {url}")
    return {"url": url, "size_kb": int(delay * 100)}


async def main(urls):
    start = time.monotonic()
    results = []
    tasks = [asyncio.create_task(download(url, delay)) for url, delay in urls.items()]
    for task in tasks:
        result = await task
        results.append(result)
    for res in sorted(results, key=lambda x: x["url"]):
        print(res)
    end = time.monotonic()
    print(round(end - start, 1))


urls_response_time = {
    "api/users": 0.4,
    "api/orders": 0.6,
    "api/products": 0.2,
    "api/stats": 0.5,
}

asyncio.run(main(urls_response_time))
