SELECT * FROM 
(SELECT id, name, DATE_FORMAT(birthday_at, '%M')  as 'month' FROM users) 
AS birthdays
WHERE month IN ('May', 'August');