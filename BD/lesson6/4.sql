SELECT CONCAT ('Лайков больше всего поставили', ' ', IF (
			(SELECT SUM(id) as amount FROM likes WHERE user_id IN (
					SELECT user_id FROM profiles WHERE sex = 'f')) > 
			(SELECT SUM(id) as amount FROM likes WHERE user_id IN (
					SELECT user_id FROM profiles WHERE sex = 'm')), 'женщины', 'мужчины'), '') as result; 