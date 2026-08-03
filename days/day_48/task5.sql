/*

Задача 5 (Итоговая, 20 мин)  Мы эмулируем backend-транзакцию покупки товара. У нас есть три таблицы:wallets (user_id, balance)inventory (item_id, stock)orders (id, user_id, item_id, status)Условие: Напиши последовательность из четырех SQL-запросов, которые выполнит сервер, когда user_id = 1 покупает item_id = 42 стоимостью 500.Создай новую запись в таблице orders (поля user_id, item_id, status). Статус должен быть 'PENDING'.Вычти 500 из balance в таблице wallets для user_id = 1.Вычти 1 из stock в таблице inventory для item_id = 42.Обнови статус заказа в таблице orders на 'SUCCESS' для user_id = 1 и item_id = 42.Ожидаемое состояние таблиц (логика успешной покупки):Plaintext-- wallets
user_id | balance
1       | [старый баланс - 500]

-- inventory
item_id | stock
42      | [старый остаток - 1]

-- orders
id | user_id | item_id | status
1  | 1       | 42      | SUCCESS
*/

CREATE TABLE wallets (
  user_id INTEGER PRIMARY KEY ATOINCREMENT,
  balance TEXT
);
CREATE TABLE inventory (
  item_id INTEGER PRIMARY KEY ATOINCREMENT,
  stock TEXT
);
CREATE TABLE orders(
  id INTEGER PRIMARY KEY ATOINCREMENT,
  user_id INTEGER,
  item_id INTEGER,
  status
);

