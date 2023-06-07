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
    ('The World', '053'), 
    ('The World', '030'), 
    ('The World', '145'), 
    ('The World', '015'), 
    ('The World', '155'), 
    ('The World', '054'), 
    ('The World', '202'), 
    ('The World', '143'), 
    ('The World', '034'), 
    ('The World', '154'), 
    ('The World', '039'), 
    ('The World', '035'), 
    ('The World', '057'), 
    ('The World', '419'), 
    ('The World', '151'), 
    ('The World', '021'), 
    ('The World', '061');

INSERT INTO SubRegionPresets
    (pName, subRegionCode)
VALUES
    ('Asia', '030'),
    ('Asia', '145'),
    ('Asia', '034'),
    ('Asia', '035'),
    ('Asia', '143');

INSERT INTO SubRegionPresets
    (pName, subRegionCode)
VALUES
    ('Europe', '155'),
    ('Europe', '154'),
    ('Europe', '039'),
    ('Europe', '151');


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

