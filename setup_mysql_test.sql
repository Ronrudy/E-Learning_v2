-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS el_test_db;
CREATE USER IF NOT EXISTS 'el_test'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `el_test_db`.* TO 'el_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'el_test'@'localhost';
FLUSH PRIVILEGES;