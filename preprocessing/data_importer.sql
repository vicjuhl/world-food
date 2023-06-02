DROP TABLE IF EXISTS Countries;

DROP TABLE IF EXISTS Affordability;

DROP TABLE IF EXISTS BMI;

DROP TABLE IF EXISTS Waste;


CREATE TABLE Countries(
    iso integer, 
    iso_alpha text,
    population_ integer,
    count_name text,
    subcontinent text,
    continent text
);

CREATE TABLE Affordability(
    iso_alpha text,
    year_ integer,
    unaffordable float
);

CREATE TABLE BMI(
    iso_alpha char(3),
    sex varchar(5),
    year_ integer,
    mean_urban float,
    mean_rural float
);

/* CREATE TABLE Waste(
    iso integer,
    iso_alpha text, 
    year integer, 
    commodity text,
    loss_pct float, 
    stage text          );              Could perhaps be changed to a integer (as index for a chronological stage number) */

/*
CREATE TABLE Waste(
    m49_code text,
    country text,
    region text,
    cpc_code text,
    commodity text,
    year text,
    loss_percentage text,
    loss_percentage_original text,
    loss_quantity text,
    activity text,
    food_supply_stage text,
    treatment text,
    cause_of_loss text,
    sample_size text,
    method_data_collection text,
    reference text,
    url text,
    notes text
);
*/

\copy Affordability FROM 'data_cleaned/unaffordability_cleaned.csv' WITH CSV HEADER DELIMITER ',';

\copy BMI FROM 'data_cleaned/bmi_cleaned.csv' WITH CSV HEADER DELIMITER ',';

