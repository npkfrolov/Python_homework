SELECT dep.id, departure, arrival FROM  
(SELECT f.id, 
c.name as departure 
FROM flights f JOIN cities c WHERE f.departure = c.label) as dep
JOIN 
(SELECT f.id, 
c.name as arrival 
FROM flights f JOIN cities c WHERE f.arrival = c.label) as arr
ON (dep.id = arr.id);