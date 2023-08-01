-- creates a database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id int UNIQUE AUTO-INCREMENT NOT NULL PRIMARY KEY,
	name varchar(256)
);
