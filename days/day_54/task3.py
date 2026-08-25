"""3. Данные пользователя — средняя, ~9 мин

Напишите корутину fetch_user(user_id): ждёт await asyncio.sleep(1), возвращает {"id": user_id, "name": f"user_{user_id}"}. Напишите корутину fetch_orders(user_id): ждёт await asyncio.sleep(1), возвращает ["order_1", "order_2"]. В main() последовательно дождитесь обеих для одного user_id и выведите результат.

Входные данные: user_id = 7 — передаётся в коде как аргумент при вызове.
Ожидаемый результат:
User: {'id': 7, 'name': 'user_7'}
Orders: ['order_1', 'order_2']"""

import asyncio


async def fetch_user(user_id):
    await asyncio.sleep(1)
    return {"id": user_id, "name": f"user_{user_id}"}


async def fetch_orders(user_id):
    await asyncio.sleep(1)
    return ["order_1", "order_2"]


async def main(user_id):
    users = await fetch_user(user_id)
    orders = await fetch_orders(user_id)
    print(f"User: {users}")
    print(f"Orders: {orders}")


asyncio.run(main(8))
