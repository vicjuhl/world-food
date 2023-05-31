DROP TABLE IF EXISTS Countries;

DROP TABLE IF EXISTS Affordability;

DROP TABLE IF EXISTS BMI;

DROP TABLE IF EXISTS Waste;


CREATE TABLE Countries(
    iso integer, 
    iso_alpha text,
    population integer,
    count_name text,
    subcontinent text,
    continent float                      /* Could perhaps be changed to a integer (as index for a chronological stage number) */
);

CREATE TABLE Affordability(
    country text,                  /* Should be dropped since we use iso as foreign key */
    iso text, 
    year integer, 
    affordable float
);

CREATE TABLE BMI(
    iso text, 
    sex text, 
    year integer, 
    mean_BMI_urban float,
    mean_BMI_rural float
);

CREATE TABLE Waste(
    iso text, 
    year integer, 
    commodity text,
    loss_pct float, 
    stage text                      /* Could perhaps be changed to a integer (as index for a chronological stage number) */
);


\copy Affordability FROM 'raw_data\food-prices.csv' WITH CSV HEADER DELIMITER ',';

