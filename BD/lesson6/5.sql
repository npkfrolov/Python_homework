/* 6.5. Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети.
 
Баллы активности юзера подсчитаны как сумма числа лайков, которые он поставил; 
числа групп, в которые он входит; числа друзей, которое у него есть 
(чьи заявки он подтвердил или кому он заявку отправил, независимо от того, подтверждена такая заявка или нет); 
числа объектов медиа, которые он разместил; числа посланий, которые он отправил*/

SELECT u.id, CONCAT(u.first_name, ' ', u.last_name), counted.total
	FROM 
	(SELECT COUNT(id ) as total, id
		FROM (
			SELECT u.id 
				FROM users u 
				LEFT JOIN likes l ON u.id = l.user_id
				LEFT JOIN communities_users cu ON u.id = cu.user_id 
				LEFT JOIN friendship f ON u.id = f.user_id 
				LEFT JOIN friendship f2 ON u.id = f2.friend_id AND f2.status_id = 2
				LEFT JOIN media m ON u.id = m.user_id 
				LEFT JOIN messages m2 ON u.id = m2.from_user_id
			) consolid
	GROUP BY id
	) as counted
	JOIN 
	users u
	ON counted.id = u.id 
ORDER BY counted.total
LIMIT 10;
