SELECT f.id, 
cities_departure.name as departure,
cities_arrival.name as arrival
FROM flights f 
LEFT JOIN cities AS cities_departure
ON cities_departure.label=f.departure
LEFT JOIN
cities AS cities_arrival
ON cities_arrival.label=f.arrival;