--  Lists all records of table `second_table` of database `hbtn_0c_0` in your MySQL server
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
