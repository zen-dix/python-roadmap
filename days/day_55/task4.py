"""
4.Найди и почини баг (10 мин, без изменения handle_client)
async def handle_client(client_id, delay):
    print(f"start client {client_id}")
    await asyncio.sleep(delay)
    print(f"done client {client_id}")
    return client_id

async def main():
    clients = [(1, 1), (2, 0.5), (3, 0.7)]
    results = []
    for client_id, delay in clients:
        task = asyncio.create_task(handle_client(client_id, delay))
        results.append(await task)  # bug is here
    print(results)

asyncio.run(main())
Ограничение: менять можно только main(), функцию handle_client трогать нельзя.
Ожидаемый результат после фикса: время ≈ 1.0s (max delay) вместо 2.2s (сумма).
"""

import asyncio
import time


async def handle_client(client_id, delay):
    print(f"start client {client_id}")
    await asyncio.sleep(delay)
    print(f"done client {client_id}")
    return client_id


async def main():
    start = time.monotonic()
    clients = [(1, 1), (2, 0.5), (3, 0.7)]
    results = []
    tasks = [
        asyncio.create_task(handle_client(client_id, delay))
        for client_id, delay in clients
    ]
    for task in tasks:
        result = await task
        results.append(result)

    print(results)
    end = time.monotonic()
    print(round(end - start, 1))


asyncio.run(main())
