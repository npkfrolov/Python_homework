/* 6_2. Пусть задан некоторый пользователь. 
Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.*/

SELECT 	 mes.messages, 
		CONCAT(us.first_name, ' ', us.last_name) as name 
FROM users us
	JOIN 
	(SELECT SUM(amount) as messages,
			friend 
	FROM (
			(SELECT COUNT(*) as amount, 
					from_user_id as friend
			FROM messages GROUP BY from_user_id , to_user_id HAVING to_user_id = 19) 
			UNION 
			(SELECT COUNT(*) as amount, to_user_id as friend 
				FROM messages GROUP BY from_user_id , to_user_id HAVING from_user_id = 19)
		) as a GROUP BY friend 
		) AS mes
	ON us.id = mes.friend
	JOIN friendship_statuses fr  
 	ON fr.name = 'Confirmed'
ORDER BY messages DESC LIMIT 1;
