-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

-- select from table
SELECT cities.id, cities.name, states.name FROM cities

-- join table from fight to the left one
LEFT JOIN states ON states.id = cities.state_id


-- order output by id
ORDER BY cities.id ASC;
