/* хранимые 9.2. В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
 * Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
 * Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. 
 * При попытке присвоить полям NULL-значение необходимо отменить операцию.*/

DROP trigger IF EXISTS notnull_upd;
DROP trigger IF EXISTS notnull_ins;

DELIMITER //

CREATE TRIGGER notnull_ins BEFORE INSERT ON products
FOR EACH ROW
BEGIN
	IF (NEW.name IS NULL AND NEW.description IS NULL) THEN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'INSERT canceled';
	END IF;
END//

CREATE TRIGGER notnull_upd BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
	IF ((NEW.name IS NULL AND NEW.description IS NULL)
	OR  (NEW.name IS NULL AND OLD.description IS NULL) 
	OR 	(OLD.name IS NULL AND NEW.description IS NULL)) THEN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'UPDATE canceled';
	END IF;
END//

DELIMITER ;

