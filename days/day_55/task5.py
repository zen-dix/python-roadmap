"""5. Order handler (12 мин)
Дан orders = [("order-1", 2), ("order-2", 0.5), ("order-3", 1)] (id, время обработки в секундах). Напиши process_order(order_id, delay) — print старт/финиш, возвращает {"id": order_id, "status": "processed"}. В main запусти обработку всех заказов конкурентно, собери результаты в исходном порядке заказов (не порядке завершения), выведи список и общее время. В начале main выведи, сколько заказов в очереди (len(orders)).
Ожидаемый результат: время ≈ 2s, порядок результатов — order-1, order-2, order-3."""

import asyncio
import time


async def process_order(order_id, delay):
    print(f"start {order_id}")
    await asyncio.sleep(delay)
    print(f"end {order_id}")
    return {"id": order_id, "status": "processed"}


async def main(orders):
    start = time.monotonic()
    print(len(orders))
    results = []
    tasks = [
        asyncio.create_task(process_order(order_id, delay))
        for order_id, delay in orders
    ]
    for task in tasks:
        result = await task
        results.append(result)
    for res in results:
        print(res)
    end = time.monotonic()
    print(round(end - start, 1))


orders = [("order-1", 2), ("order-2", 0.5), ("order-3", 1)]
asyncio.run(main(orders))
