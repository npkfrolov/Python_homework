/*2. Построить запрос, который будет выводить следующие столбцы:
имя группы
среднее количество пользователей в группах
самый молодой пользователь в группе
самый пожилой пользователь в группе
общее количество пользователей в группе
всего пользователей в системе
отношение в процентах (общее количество пользователей в группе / всего пользователей в системе) * 100 */

SELECT DISTINCT community, youngdate, olderdate, users_in_com, 
(SELECT COUNT(id ) FROM users u2 ) total,
(SELECT users_in_com / total) * 100 share
FROM 
	(SELECT DISTINCT c.name as community,
		COUNT(cu.user_id) OVER w AS users_in_com,
		MIN(p.birthdate ) OVER w AS youngdate,
		MAX(p.birthdate ) OVER w AS olderdate
			FROM communities c
			 JOIN communities_users cu
				ON c.id = cu.community_id 
			JOIN profiles p
				ON cu.user_id = p.user_id 
			WINDOW w AS (PARTITION BY cu.community_id)) a 
		ORDER BY community ;
	
	
			


