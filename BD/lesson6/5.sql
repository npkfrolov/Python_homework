/*баллы активности юзера подсчитаны как сумма числа лайков, которые он поставил; 
числа групп, в которые он входит; числа друзей, которое у него есть 
(чьи заявки он подтвердил или кому он заявку отправил, независимо от того, подтверждена такая заявка или нет); 
числа объектов медиа, которые он разместил; числа посланий, которые он отправил*/

SELECT 	activities, 
		(SELECT CONCAT(first_name, ' ', last_name) FROM users WHERE id = b.user_id) as username 
FROM 
	(SELECT SUM(amount) as activities, user_id FROM
		((SELECT COUNT(id) as amount, user_id FROM likes GROUP BY user_id
		UNION
		SELECT COUNT(user_id) as amount, user_id FROM communities_users  GROUP BY user_id
		UNION 
		SELECT COUNT(user_id) as amount, user_id FROM friendship GROUP BY user_id 
		UNION 
		SELECT COUNT(friend_id) as amount, friend_id as user_id FROM friendship GROUP BY friend_id 
			HAVING friend_id IN 
      			(SELECT friend_id FROM friendship WHERE status_id IN
      					(SELECT id FROM friendship_statuses 
        					WHERE name = 'Confirmed'
        				)
        		)
		UNION 
		SELECT COUNT(user_id) as amount, user_id FROM media GROUP BY user_id
		UNION 
		SELECT COUNT(from_user_id) as amount, from_user_id FROM messages GROUP BY from_user_id) 
		) a
	GROUP BY user_id) b
ORDER BY activities 
LIMIT 10;

