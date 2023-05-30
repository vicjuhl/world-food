DROP TABLE IF EXISTS Affordability;

CREATE TABLE Affordability(name text, iso text, year integer, affordability float);

start transaction;
/*-h host_name -U user_name -d database_name -c " */

copy Affordability 
FROM '\Users\45609\OneDrive\Desktop\Filer\KU\DIS\world-food\raw_data\food-prices.csv' 
WITH CSV HEADER DELIMITER ','
;

/* " */ 