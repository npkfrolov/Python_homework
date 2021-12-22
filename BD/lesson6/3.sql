/* 6.3. Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей*/

SELECT SUM(l.likescount) as summ 
	FROM (SELECT COUNT(*) as likescount, target_id FROM likes  GROUP BY target_id) as l 
	JOIN target_types t
	ON t.name = 'users'
	RIGHT JOIN  users u
	ON l.target_id = u.id 
	JOIN (SELECT user_id FROM profiles ORDER BY birthdate DESC  LIMIT 10) as y
	ON y.user_id = u.id;
