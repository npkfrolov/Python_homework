/* транзакции 9.2. Создайте представление, которое выводит название name 
 товарной позиции из таблицы products и соответствующее название каталога name из таблицы catalogs*/

CREATE VIEW names AS SELECT 
p.name as product,
c.name as catalog
FROM products p, catalogs c 
WHERE p.catalog_id =c.id ;


