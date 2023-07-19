-- a script that creates the database hbtn_0d_2 and the user user_0d_2.

-- create new DataBase
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create new user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant user only SELECT privilege in the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- reload
FLUSH PRIVILEGES;
