DROP TABLE IF EXISTS Countries;

DROP TABLE IF EXISTS Affordability;

DROP TABLE IF EXISTS BMI;

-- DROP TABLE IF EXISTS Waste;

DROP TABLE IF EXISTS SubRegionPresets;

CREATE TABLE Countries(
    iso_alpha char(3),
    country_name text,
    sub_region text,
    sub_region_code char(3),
    region text,
    region_code char(3)
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

CREATE TABLE SubRegionPresets(
    pName text,
    subRegionCode char(3)
);

INSERT INTO SubRegionPresets
    (pName, subRegionCode)
VALUES
    ('Asia', '030'),
    ('Asia', '145'),
    ('Asia', '034'),
    ('Asia', '035'),
    ('Asia', '143');

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

\copy Countries FROM 'data_cleaned/countries_cleaned.csv' WITH CSV HEADER DELIMITER ',';
\copy Affordability FROM 'data_cleaned/unaffordability_cleaned.csv' WITH CSV HEADER DELIMITER ',';
\copy BMI FROM 'data_cleaned/bmi_cleaned.csv' WITH CSV HEADER DELIMITER ',';

