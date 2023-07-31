-- lists all records with exceptions
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
