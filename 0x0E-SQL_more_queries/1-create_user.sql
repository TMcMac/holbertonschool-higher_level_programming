-- create user user_0d_1 and set password, then grant all privileges
-- Never
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEDGES ON * . * TO 'user_0d_01'@'localhost';