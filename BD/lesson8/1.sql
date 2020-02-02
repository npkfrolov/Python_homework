ALTER TABLE profiles
  ADD CONSTRAINT profiles_user_id_fk 
    FOREIGN KEY (user_id) REFERENCES users(id)
      ON DELETE CASCADE,

-- проверяем, как сопрягаются внешний ключ с родительским первичным
SELECT p.photo_id, m.id 
FROM profiles p LEFT JOIN media m ON p.photo_id = m.id AND m.id = NULL ;
-- выяснилось, что надо сгенерить заново айдишники в диапазоне 1-100


-- заменяем в поле внешнего ключа несуществующие в родительском поле значения на существующие
UPDATE profiles SET photo_id = RAND()*100 WHERE photo_id > 100;

ALTER TABLE profiles
  ADD CONSTRAINT profiles_photo_id_fk
    FOREIGN KEY (photo_id) REFERENCES media(id)
      ON DELETE SET NULL;
     

ALTER TABLE communities_users 
  ADD CONSTRAINT communities_id_fk 
    FOREIGN KEY (community_id) REFERENCES communities (id)
      ON DELETE CASCADE;
  ADD CONSTRAINT users_id_fk 
    FOREIGN KEY (user_id) REFERENCES users(id)
      ON DELETE CASCADE;
      
 ALTER TABLE friendship 
  ADD CONSTRAINT user_id_fk 
    FOREIGN KEY (user_id) REFERENCES users(id)
      ON DELETE CASCADE;
  ADD CONSTRAINT friend_id_fk 
    FOREIGN KEY (friend_id) REFERENCES users(id)
      ON DELETE CASCADE;
 
 ALTER TABLE friendship MODIFY COLUMN status_id INT(10);

-- проверяем, как сопрягаются внешний ключ с родительским первичным
SELECT f.status_id , f2.id 
FROM friendship f LEFT JOIN friendship_statuses f2 ON f.status_id  = f2.id AND f2.id =0; 

-- заменяем в поле внешнего ключа несуществующие в родительском поле значения на существующие
UPDATE friendship SET status_id =2 WHERE status_id > 3;

ALTER TABLE friendship 
 	ADD CONSTRAINT status_id_fk 
    FOREIGN KEY (status_id) REFERENCES friendship_statuses(id)
      ON DELETE RESTRICT;    
     
-- проверяем, как сопрягаются внешний ключ с родительским первичным
SELECT l.user_id , u.id 
FROM likes l LEFT JOIN users u ON l.user_id = u.id AND u.id = NULL; 

SELECT user_id FROM likes l WHERE user_id < 101 ORDER BY user_id DESC ;
SELECT id FROM users u WHERE id < 101 ORDER BY id DESC;
     
ALTER TABLE likes 
	ADD CONSTRAINT us_id_fk 
    	FOREIGN KEY (user_id) REFERENCES users(id)
      		ON DELETE CASCADE;
     
ALTER TABLE likes 
	ADD CONSTRAINT target_type_id_fk 
    	FOREIGN KEY (target_type_id) REFERENCES target_types (id)
      		ON DELETE CASCADE ;
      	
ALTER TABLE likes 
	ADD CONSTRAINT target_id_fk 
    	FOREIGN KEY (target_id) REFERENCES media(id)
      		ON DELETE CASCADE;      	

ALTER TABLE media 
	ADD CONSTRAINT usermedia_id_fk 
    	FOREIGN KEY (user_id) REFERENCES users(id)
      		ON DELETE RESTRICT;
      	
ALTER TABLE media 
	ADD CONSTRAINT media_type_id_fk 
    	FOREIGN KEY (media_type_id) REFERENCES media_types(id)
      		ON DELETE RESTRICT;

ALTER TABLE messages 
	ADD CONSTRAINT fromuser_id_fk 
    	FOREIGN KEY (from_user_id) REFERENCES users(id)
      		ON DELETE CASCADE;

ALTER TABLE messages    
     ADD CONSTRAINT touser_id_fk 
    	FOREIGN KEY (to_user_id) REFERENCES users(id)
      		ON DELETE NO ACTION;
