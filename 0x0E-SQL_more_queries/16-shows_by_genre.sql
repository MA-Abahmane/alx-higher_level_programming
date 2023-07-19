-- a script that lists all shows contained in the database hbtn_0d_tvshows.

-- select show name and its genres
SELECT tv_shows.title, tv_genres.name

-- join table tv_show_genres to table tv_shows
FROM tv_shows 

LEFT JOIN tv_show_genres 
ON tv_show_genres.show_id = tv_shows.id

-- then join table tv_genres to them
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id

-- sort output my alpha order
ORDER BY tv_shows.title, tv_genres.name ASC;
