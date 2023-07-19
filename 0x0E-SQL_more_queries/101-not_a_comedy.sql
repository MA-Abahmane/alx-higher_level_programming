-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.

-- select all genres that are not Comedy
SELECT title FROM tv_shows WHERE title NOT IN 
(
-- select show names
SELECT Ts.title FROM tv_genres Tg, tv_show_genres Tsg, tv_shows Ts

-- match the shows that are of the 'Comedy' type
WHERE Tg.id = Tsg.genre_id AND Tg.name = 'Comedy' AND Tsg.show_id = Ts.id
)
ORDER BY title ASC;
-- order output in alphabetical order
