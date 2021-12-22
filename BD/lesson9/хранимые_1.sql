/* хранимые 9.1. Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу 
"Добрый день", с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".*/

DROP FUNCTION IF EXISTS hello;
DELIMITER //
CREATE FUNCTION hello()
RETURNS VARCHAR(255) 
BEGIN
	DECLARE phrase VARCHAR(255);
	DECLARE part TIME;

	SET part :=  DATE_FORMAT(NOW(), "%H:%i:%s");
	IF (part > 17:59:59) THEN
		SET phrase = 'Добрый вечер';
		ELSEIF (part > 11:59:59) THEN 
		SET phrase := 'Добрый день';
		ELSEIF (part > 5:59:59) THEN 
		SET phrase := 'Доброе утро'
		ELSE SET phrase := 'Доброй ночи';
	END IF;
	RETURN phrase;
END //

-- ошибка потому, что part воспринимается почему-то как INT, а не TIME. Почему?