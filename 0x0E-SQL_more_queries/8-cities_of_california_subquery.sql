-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

-- select from table
SELECT `id`, `name` FROM cities 

-- set condition to get the id of 'California'
WHERE state_id = (SELECT id FROM states WHERE `name` = 'California')

-- order output by id
ORDER BY id ASC;