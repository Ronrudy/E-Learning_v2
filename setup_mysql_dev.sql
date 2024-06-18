--   Creates a MySQL server with:
--   Database el_dev_db.
--   User el_dev with password el in localhost.
--   Grants all privileges for el_dev on el_dev_db.
--   Grants SELECT privilege for el_dev on performance.

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS el_dev_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'el_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on el_dev_db to el_dev
GRANT ALL PRIVILEGES ON el_dev_db.* TO 'el_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to el_dev
GRANT SELECT ON performance_schema.* TO 'el_dev'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;