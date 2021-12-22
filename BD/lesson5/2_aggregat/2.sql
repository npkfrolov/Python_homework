SELECT COUNT(*) as total , DATE_FORMAT(CONCAT(SUBSTRING(NOW(),1, 5 ), SUBSTRING(birthday_at , 6, 5) ), '%W')  as days 
FROM users GROUP BY days;
