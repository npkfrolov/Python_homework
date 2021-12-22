/* 11.1_оптимизация. Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах 
 users, catalogs и products в таблицу logs помещается время и дата создания записи, название таблицы, 
 идентификатор первичного ключа и содержимое поля name.*/

DROP TABLE IF EXISTS logs;
DROP TRIGGER IF EXISTS log_append_users;
DROP TRIGGER IF EXISTS log_append_catalogs;
DROP TRIGGER IF EXISTS log_append_products;

CREATE TABLE logs (
date_of_ins datetime,
table_name varchar(255) ,
table_id integer,
name_from_table varchar(255) 
) ENGINE=ARCHIVE;

DELIMITER //

CREATE TRIGGER log_append_users AFTER INSERT ON shop.users
FOR EACH ROW
BEGIN
  INSERT INTO logs(date_of_ins ,table_name ,table_id ,name_from_table ) VALUES (NOW(), 'users', NEW.id, NEW.name);
END//

CREATE TRIGGER log_append_catalogs AFTER INSERT ON shop.catalogs
FOR EACH ROW
BEGIN
 INSERT INTO logs(date_of_ins ,table_name ,table_id ,name_from_table ) VALUES (NOW(), 'catalogs', NEW.id , NEW.name );
END//

CREATE TRIGGER log_append_products AFTER INSERT ON shop.products
FOR EACH ROW
BEGIN
  INSERT INTO logs(date_of_ins ,table_name ,table_id ,name_from_table ) VALUES (NOW(), 'products', NEW.id, NEW.name);
END//

DELIMITER ;

-- почему в лог в поле table_id записывается значение, на единицу большее, чем реальный айдишник в таблицах, мне непонятно.

INSERT INTO users(name) VALUES ('Петя');
INSERT INTO catalogs(name) VALUES ('vdfsws');
INSERT INTO products(name) VALUES ('g3ghhаfcfg');