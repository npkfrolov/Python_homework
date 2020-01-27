SELECT 	SUM(amount) as messages, 
	(SELECT	CONCAT(first_name, ' ', last_name) 
		FROM users u2 WHERE id = united.friend ) as friend 
			FROM (
				(SELECT COUNT(*) as amount, from_user_id as friend 
					FROM messages GROUP BY from_user_id , to_user_id HAVING to_user_id = 19) 
				UNION 
				(SELECT COUNT(*) as amount, to_user_id as friend 
					FROM messages GROUP BY from_user_id , to_user_id HAVING from_user_id = 19)
				) as united
				WHERE friend IN
					(SELECT friend_id FROM friendship f WHERE user_id = 19
						AND status_id IN (
			          		SELECT id FROM friendship_statuses 
			            		WHERE name = 'Confirmed'
	          	)
	    	)
		GROUP BY friend
		ORDER BY messages DESC LIMIT 1;