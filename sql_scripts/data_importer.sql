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
    continent text
);

CREATE TABLE Affordability(
    country text,                  /* Should be dropped since we use iso as foreign key */
    iso_alpha text, 
    year integer, 
    affordable float
);

/* CREATE TABLE BMI(
    iso_alpha text, 
    sex text, 
    year integer, 
    mean_BMI_urban float,
    mean_BMI_rural float
); */

CREATE TABLE BMI(
    Country_Region_World text,
    ISO text,
    Sex text,
    Year text,
    Mean_BMI_urban text,
    Mean_BMI_urban_lower_95 text,
    Mean_BMI_urban_upper_95 text,
    Mean_BMI_rural text,
    Mean_BMI_rural_lower_95 text,
    Mean_BMI_rural_upper_95 text,
    Mean_BMI_urban_rural_diff text,
    Mean_BMI_urban_rural_diff_lower_95 text,
    Mean_BMI_urban_rural_diff_upper_95 text
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

\copy Affordability FROM 'raw_data/food-prices.csv' WITH CSV HEADER DELIMITER ',';

\copy BMI FROM 'raw_data/NCD_RisC_Nature_2019_age_standardised_country.csv' WITH CSV HEADER DELIMITER ',';

-- \copy Waste FROM 'raw_data/food-loss-waste-Data.csv' WITH CSV HEADER DELIMITER ',';
