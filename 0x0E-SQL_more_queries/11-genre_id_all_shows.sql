-- a script that lists all shows contained in the database hbtn_0d_tvshows.

-- select the two table
SELECT tv_shows.title, tv_show_genres.genre_id

-- join tv_show_genres to tv_shows
FROM tv_shows LEFT JOIN tv_show_genres

-- join bases on show id of each table
ON tv_show_genres.show_id = tv_shows.id

-- sort output
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;