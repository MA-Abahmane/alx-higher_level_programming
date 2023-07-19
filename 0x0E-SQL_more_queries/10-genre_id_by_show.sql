-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

-- select the two table
SELECT tv_shows.title, tv_show_genres.genre_id

-- Join the two tables into one
FROM tv_shows JOIN tv_show_genres

-- join bases on show id of each table
ON tv_show_genres.show_id = tv_shows.id

-- sort output
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
