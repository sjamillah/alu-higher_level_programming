-- creates table with a unique key object
CREATE TABLE IF NOT EXISTS unique_id(
	id int DEFAULT 1 UNIQUE,
	name varchar(256)
);
