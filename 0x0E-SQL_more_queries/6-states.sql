--  a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

-- create DataBase hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;


-- create the table states and INCREMENT id by 1 for each value
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    `id` INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
) ENGINE=INNODB;
