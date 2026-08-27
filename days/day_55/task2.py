"""2. Concurrent rewrite (7 мин)
Перепиши задачу 1 так, чтобы обе функции запускались конкурентно через asyncio.create_task.
Ожидаемый результат: время ≈ 1.5s (максимум из задержек, а не сумма).
    В конце добавь однострочный английский print-комментарий, поясняющий, почему стало быстрее."""

import asyncio
import time


async def download_avatar():
    print("start download avatar")
    await asyncio.sleep(1.5)
    print("avatar download successful")


async def download_settings():
    print("start download settings")
    await asyncio.sleep(1)
    print("settings download successful")


async def main():
    print("concurrency")
    task1 = asyncio.create_task(download_avatar())
    task2 = asyncio.create_task(download_settings())
    start = time.monotonic()
    result1 = await task1
    result2 = await task2
    end = time.monotonic()
    print(round(end - start, 1), "s")


asyncio.run(main())
