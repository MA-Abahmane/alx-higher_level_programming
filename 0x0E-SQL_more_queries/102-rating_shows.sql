-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating.

CREATE TABLE IF NOT EXISTS genres(
    `name` VARCHAR(100),
    `rate` INT
);

INSERT INTO genres VALUES 
    ("Homeland", 1311), 
    ("Arrow", 937), 
    ("The Last Man on Earth", 916), 
    ("The Big Bang Theory", 901),
    ("Game of Thrones", 828), 
    ("New Girl", 762), 
    ("Twin Peaks", 653), 
    ("Criminal Minds", 610), 
    ("Breaking Bad", 341),
    ("Friends", 303), 
    ("Dexter", 245), 
    ("Better Call Saul", 46), 
    ("House", 34), 
    ("Silicon Valley", 16);

SELECT `name` AS `title`, `rate` AS `rating` FROM genres
ORDER BY `rate` DESC;
