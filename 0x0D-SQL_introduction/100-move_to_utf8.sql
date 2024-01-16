-- converts hbtn_0c_0 database to UTF8
USE hbtn_0c_0

-- change charset and collation of the table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
