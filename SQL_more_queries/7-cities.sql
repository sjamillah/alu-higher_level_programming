-- creates a database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id int UNIQUE AUTO-INCREMENT NOT NULL PRIMARY KEY,
	state_id int NOT NULL FOREIGN KEY (state_id) REFERENCES states(id),
	name varchar(256) NOT NULL
);
