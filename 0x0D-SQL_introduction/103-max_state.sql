-- a script that displays the max temperature of each state (ordered by State name).

SELECT `state`, MAX(`value`) AS `max_temp` FROM `temperatures`

-- group by state and order

GROUP BY `state` ORDER BY `state` ASC

