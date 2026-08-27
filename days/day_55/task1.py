"""1. Sequential warm-up (6 мин)
Напиши download_avatar() (asyncio.sleep(1.5)) и download_settings() (asyncio.sleep(1)). Внутри каждой — print в начале и в конце. В main() вызови их последовательно через await, замерь общее время через time.monotonic(), выведи результат.
Данные: задержки захардкожены в коде.
Ожидаемый результат: время ≈ 2.5s (сумма задержек)."""

import asyncio
import time


async def download_avatar():
    print("start download avatar")
    await asyncio.sleep(1.5)
    print("avatar download succeful")


async def download_settings():
    print("start download settings")
    await asyncio.sleep(1)
    print("settings download succeful")


async def main():
    start = time.monotonic()
    await download_avatar()
    await download_settings()
    end = time.monotonic()
    print(round(end - start, 1), "s")


asyncio.run(main())
