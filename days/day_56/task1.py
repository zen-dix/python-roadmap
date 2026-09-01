"""1. [Лёгкая, ~6 мин] Напиши fetch_weather(city) и fetch_time(city) — каждая через asyncio.sleep имитирует задержку (1 сек и 0.5 сек соответственно) и возвращает строку вида "Weather in Moscow: sunny". Запусти обе через gather, замерь общее время выполнения (time.monotonic() до/после) и выведи его — покажи, что оно ~1 сек, а не 1.5."""

import asyncio
import time


async def fetch_weather(city):
    await asyncio.sleep(1)
    return f"Weather in {city}: sunny"


async def fetch_time(city):
    await asyncio.sleep(0.5)
    return f"Time in {city}: 12:00"


async def main():
    start = time.monotonic()
    res = await asyncio.gather(fetch_weather("Moscow"), fetch_time("New York"))
    print(*res, sep="\n")
    end = time.monotonic()
    print(round(end - start, 1))


asyncio.run(main())
