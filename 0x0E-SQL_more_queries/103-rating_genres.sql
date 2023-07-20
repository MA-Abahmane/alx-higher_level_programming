-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.

CREATE TABLE IF NOT EXISTS genres(
    `name` VARCHAR(100),
    `rate` INT
);

INSERT INTO genres VALUES 
    ("Drama", 150), 
    ("Comedy", 92), 
    ("Adventure", 79), 
    ("Fantasy", 79),
    ("Mystery", 45), 
    ("Crime", 40), 
    ("Suspense", 40), 
    ("Thriller", 40);

SELECT `name`, `rate` AS `rating` FROM genres
ORDER BY `rate` DESC;
