-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

-- select genres names of show
SELECT Tg.name FROM tv_genres Tg, tv_show_genres Tsg, tv_shows Ts

-- match the show geare and show title
WHERE Tg.id = Tsg.genre_id AND Ts.title = 'Dexter' AND Tsg.show_id = Ts.id

-- order by type
ORDER BY Tg.name ASC;
