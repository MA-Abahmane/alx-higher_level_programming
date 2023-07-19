-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

-- select the genre names and count number how many we have of each one
SELECT tv_genres.name AS `genre`, COUNT(*) AS `number_of_shows`

-- join table tv_show_genres to table tv_shows
FROM tv_show_genres LEFT JOIN tv_genres 
ON tv_genres.id = genre_id

-- group by genre id
GROUP BY `genre_id`

-- sort output
ORDER BY COUNT(*) DESC;