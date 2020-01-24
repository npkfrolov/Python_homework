--сделал поля со строчным типом данных, залил в них значения из полей в формате DATETIME
ALTER TABLE users ADD COLUMN created_at_varchar VARCHAR(100);
ALTER TABLE users ADD COLUMN updated_at_varchar VARCHAR(100);
UPDATE users SET created_at_varchar='20.10.2017 8:10';
UPDATE users SET updated_at_varchar='20.10.2017 8:10';

--перестроил цифирьки и привел обратно к типу DATETIME
UPDATE users SET created_at_varchar=CONVERT(CONCAT(SUBSTRING(created_at_varchar,7,4), '-', SUBSTRING(created_at_varchar,4,2), '-', SUBSTRING(created_at_varchar,1,2), ' ', SUBSTRING(created_at_varchar,12,3), SUBSTRING(created_at_varchar,15,2)), DATETIME);
UPDATE users SET updated_at_varchar=CONVERT(CONCAT(SUBSTRING(updated_at_varchar,7,4), '-', SUBSTRING(updated_at_varchar,4,2), '-', SUBSTRING(updated_at_varchar,1,2), ' ', SUBSTRING(updated_at_varchar,12,3), SUBSTRING(updated_at_varchar,15,2)), DATETIME);
