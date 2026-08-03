/*

Задача 4 (Сложная, 15 мин)  Дана таблица products с колонками id, name, price, stock.Условие: Напиши два отдельных SQL-запроса. Первый должен добавить сразу два товара одной командой (используй один INSERT INTO и несколько блоков VALUES). Второй запрос должен увеличить цену на 10% (умножить на 1.1) для всех товаров, у которых остаток на складе (stock) меньше 10.Входные данные для добавления:'Mechanical Keyboard', цена 5000, остаток 5.'Mouse', цена 2000, остаток 15.Ожидаемый результат после обоих запросов:Plaintextid | name                | price | stock
1  | Mechanical Keyboard | 5500  | 5
2  | Mouse               | 2000  | 15
*/
CREATE TABLE products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT, 
  price INTEGER,
  stock INTEGER
);
INSERT INTO products (name, price, stock)
VALUES
  ('Mechanical Keyboard', 5000, 5),
  ('Mouse', 2000, 15);
UPDATE products
SET price = price * 1.10
WHERE stock < 10;
SELECT id, name, price, stock
FROM products;
