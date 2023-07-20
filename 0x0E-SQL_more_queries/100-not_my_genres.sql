--  a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter


CREATE TABLE IF NOT EXISTS genres(
    `name` VARCHAR(100)
);

INSERT INTO `genres` VALUES ('Action'), ('Adventure'), ('Comedy'), ('Fantasy'), ('Romance');

SELECT `name` FROM genres
ORDER BY `name` ASC;
