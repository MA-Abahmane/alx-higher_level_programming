-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

-- select from table
SELECT cities.id, cities.name, states.name

-- join table states to table cities
FROM cities LEFT JOIN states
ON states.id = cities.state_id


-- order output by id
ORDER BY cities.id ASC;
