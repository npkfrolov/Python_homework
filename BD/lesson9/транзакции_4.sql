/* транзакции 9.4. (по желанию) Пусть имеется любая таблица с календарным полем created_at. 
Создайте запрос, который удаляет устаревшие записи из таблицы, оставляя только 5 самых свежих записей. 
*/

ALTER VIEW last5 AS SELECT * FROM orders ORDER BY created_at DESC LIMIT 5; 

/* это, конечно, неверное решение - здесь нет удаления из таблицы. Но создание переменной 

SET @last5 := 0;
SELECT *, @last5 := @last5 + 1 AS last5 FROM orders ORDER BY created_at DESC;
DELETE FROM orders WHERE @last5 > 5;

что то не сработало
*/
