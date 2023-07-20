-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.

CREATE TABLE IF NOT EXISTS genreRating(
    `name` VARCHAR(100),
    `rate` INT
);

INSERT INTO genreRating VALUES 
    ("Drama", 3954), 
    ("Comedy", 2898), 
    ("Adventure", 1765), 
    ("Crime", 1196),
    ("Action", 937), 
    ("Fantasy", 828),
    ("Mystery", 932),
    ("Horror", 653), 
    ("Suspense", 586), 
    ("Thriller", 586),
    ("Romance", 303);

SELECT `name`, `rate` AS `rating` FROM genreRating
ORDER BY `rate` DESC;
