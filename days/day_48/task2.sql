/*

Задача 2 (Средняя, 10 мин)  Дана таблица articles с колонками id, title, published, views.Условие: Нужно опубликовать статью и сбросить счетчик просмотров. Обнови записи, у которых published равно 0.Действие: Установи published = 1 и views = 0 для нужных строк.До обновления:Plaintextid | title       | published | views
1  | Linux setup | 0         | NULL
Ожидаемый результат:Plaintextid | title       | published | views
1  | Linux setup | 1         | 0
*/
CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  title TEXT,
  published INTEGER,
  views INTEGER
);
INSERT INTO articles (title, published, views)
VALUES ('Linux setup', 0, NULL);

SELECT id, title, published, views 
FROM articles;

UPDATE articles
SET published = 1, views = 0
WHERE published = 0;

SELECT id, title, published, views 
FROM articles;
