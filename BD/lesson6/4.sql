/* 6.4. Определить кто больше поставил лайков (всего) - мужчины или женщины?*/

SELECT CONCAT ('Лайков больше всего поставили', ' ', 
IF (
	(SELECT COUNT(l.id) as amount, p.sex 
	FROM likes l JOIN profiles p
		ON  l.user_id = p.user_id AND p.sex = 'f') > 
	(SELECT COUNT(l.id) as amount, p.sex 
	FROM likes l JOIN profiles p
		ON  l.user_id = p.user_id AND p.sex = 'm'), 
		'женщины', 'мужчины'
	)
				) as result;