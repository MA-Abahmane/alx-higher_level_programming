--  a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

-- select database and table to convert

USE hbtn_0c_0
ALTER TABLE first_table

-- convert to utf8mb4 style with  collate utf8mb4_unicode_ci

CONVERT TO CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
