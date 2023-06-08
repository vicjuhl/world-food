DROP TABLE IF EXISTS Countries CASCADE;
DROP TABLE IF EXISTS Affordability;
DROP TABLE IF EXISTS BMI;

DROP TABLE IF EXISTS Presets CASCADE;
DROP TABLE IF EXISTS SubRegionPresets;

CREATE TABLE Countries(
    iso_alpha char(3),
    country_name text,
    sub_region text,
    sub_region_code char(3),
    region text,
    region_code char(3),
    PRIMARY KEY (iso_alpha)
);

CREATE TABLE Affordability(
    iso_alpha char(3),
    year_ integer,
    unaffordable float,
    PRIMARY KEY (iso_alpha, year_),
    FOREIGN KEY (iso_alpha) REFERENCES Countries
);

CREATE TABLE BMI(
    iso_alpha char(3),
    sex varchar(5),
    year_ integer,
    mean_urban float,
    mean_rural float,
    PRIMARY KEY (iso_alpha, sex, year_),
    FOREIGN KEY (iso_alpha) REFERENCES Countries
);

CREATE TABLE Presets(
    pName text,
    rural_urban text NOT NULL,
    male_female text NOT NULL,
    PRIMARY KEY (pName)
);

INSERT INTO Presets
    (pName, rural_urban, male_female)
VALUES
    ('The World', 'Average', 'Average'),
    ('Asia', 'Average', 'Average'),
    ('Europe', 'Average', 'Average'),
    ('Europe: Women in Cities', 'Urban', 'Females');

CREATE TABLE SubRegionPresets(
    pName text NOT NULL,
    subRegionCode char(3),
    PRIMARY KEY (pName, subRegionCode),
    FOREIGN KEY (pName) REFERENCES Presets
        ON DELETE CASCADE
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
    ('The World', '061'),
    ('Asia', '030'),
    ('Asia', '145'),
    ('Asia', '034'),
    ('Asia', '035'),
    ('Asia', '143'),
    ('Europe', '155'),
    ('Europe', '154'),
    ('Europe', '039'),
    ('Europe', '151'),
    ('Europe: Women in Cities', '155'),
    ('Europe: Women in Cities', '154'),
    ('Europe: Women in Cities', '039'),
    ('Europe: Women in Cities', '151');

\copy Countries FROM 'data_cleaned/countries_cleaned.csv' WITH CSV HEADER DELIMITER ',';
\copy Affordability FROM 'data_cleaned/unaffordability_cleaned.csv' WITH CSV HEADER DELIMITER ',';
\copy BMI FROM 'data_cleaned/bmi_cleaned.csv' WITH CSV HEADER DELIMITER ',';

