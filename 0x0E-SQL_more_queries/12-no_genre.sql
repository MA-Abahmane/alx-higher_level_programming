-- a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

-- select the two table
SELECT tv_shows.title, tv_show_genres.genre_id

-- join table tv_show_genres to table tv_shows
FROM tv_shows LEFT JOIN tv_show_genres

-- join bases on show id of each table
ON tv_show_genres.show_id = tv_shows.id

-- output condition
WHERE tv_show_genres.genre_id IS NULL

-- sort output
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;