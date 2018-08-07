CREATE DATABASE practice DEFAULT CHARACTER SET utf8;
CREATE USER 'ming'@'localhost' IDENTIFIED BY 'ming';
GRANT ALL PRIVILEGES ON practice.* TO 'ming'@'host';
