SELECT id , storehouse_id , product_id , value  
FROM storehouses_products ORDER BY IF(value > 0, 1, 0) DESC, value ASC;