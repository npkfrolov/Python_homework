--без округления

SELECT AVG((TIMESTAMPDIFF(YEAR, birthday_at, NOW()))) FROM users u ;

--с округлением 

SELECT FLOOR(AVG((TIMESTAMPDIFF(YEAR, birthday_at, NOW())))) FROM users u ;