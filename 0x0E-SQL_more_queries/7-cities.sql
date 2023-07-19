--  a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

-- create DataBase hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;


-- create the table cities and INCREMENT id by 1 for each value
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    `id` INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    -- set foreign key
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
) ENGINE=INNODB;
