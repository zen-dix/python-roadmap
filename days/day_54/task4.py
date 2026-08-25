"""4. Обработка заказов — сложная, ~13 мин

Напишите корутину process_order(order_id): печатает f"Processing order {order_id}...", ждёт await asyncio.sleep(0.5), печатает f"Order {order_id} done". Напишите корутину process_all(order_ids): для каждого id в списке последовательно дожидается process_order(id), в конце печатает f"Total processed: {N}", где N — число обработанных заказов.

Входные данные: order_ids = [101, 102, 103] — передаётся в коде как аргумент при вызове.
Ожидаемый результат:
Processing order 101...
Order 101 done
Processing order 102...
Order 102 done
Processing order 103...
Order 103 done
Total processed: 3"""

import asyncio


async def process_order(order_id):
    print(f"Processing order {order_id}...")
    await asyncio.sleep(0.5)
    print(f"Order {order_id} done")


async def process_all(order_ids):
    for id in order_ids:
        await process_order(id)
    print(f"Total processed {len(order_ids)}")


order_ids = [101, 102, 103]
asyncio.run(process_all(order_ids))
