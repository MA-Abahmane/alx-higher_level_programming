--  a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

-- I had reasons
SELECT `name` FROM tv_genres
WHERE `name` = 'Adventure' OR `name` = 'Comedy' OR `name` = 'Fantasy'
ORDER BY `name` ASC;
