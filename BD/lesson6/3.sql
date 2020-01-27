SELECT SUM(likescount) as summ FROM 
	(SELECT * FROM 	
		(SELECT COUNT(*) as likescount FROM likes GROUP BY target_id HAVING target_id IN 
				(SELECT id FROM media WHERE user_id IN
					(SELECT user_id FROM profiles ORDER BY birthdate DESC
					) 
				)
		) a LIMIT 10
	) b ;
