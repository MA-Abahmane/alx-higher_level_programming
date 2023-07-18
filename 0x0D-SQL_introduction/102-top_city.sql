-- a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures`

-- only during July and August, group by city and order

WHERE `month` = 7 OR `month` = 8
GROUP BY `city` ORDER BY `avg_temp` DESC

-- show only first 3
LIMIT 3;
