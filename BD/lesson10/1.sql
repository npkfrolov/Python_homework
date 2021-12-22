/* 10.1. Проанализировать какие запросы могут выполняться наиболее часто в процессе работы приложения 
 и добавить необходимые индексы*/

CREATE INDEX users_first_last_name_idx ON users(first_name, last_name);
CREATE INDEX users_created_at_idx ON users(created_at);
CREATE INDEX users_updated_at_idx ON users(updated_at);
CREATE UNIQUE INDEX users_email_uq ON users(email);
CREATE INDEX friendship_user_id_idx ON friendship(user_id);
CREATE INDEX friendship_friend_id_idx ON friendship(friend_id);
CREATE INDEX communities_users_idx ON communities_users(user_id, community_id);
CREATE INDEX media_user_id_media_type_id_idx ON media(user_id, media_type_id);
CREATE INDEX likes_user_id_target_id_idx ON likes(user_id, target_id);
CREATE INDEX profiles_birthdate_idx ON profiles(birthdate);
CREATE INDEX profiles_hometown_country_idx ON profiles(hometown, country);
CREATE INDEX profiles_user_id_idx ON profiles(user_id);
CREATE INDEX messages_from_user_id ON messages(from_user_id);
CREATE INDEX messages_to_user_id ON messages(to_user_id);
CREATE INDEX messages_created_at_id ON messages(created_at);