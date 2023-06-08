# world-food
By Frederik van Wylich-Muxoll (ckj429) and Victor Kaplan Kjellerup (rgp867)
This repo contains the World Food application. It is a visual query tool which allows you to see the correlations between the share of a population who cannot afford a healthy meal and that populations BMI in a scatter plot. The actual data is roughly simplified due to uncareful averaging over time and other parameters and <ins>SHOULD NOT</ins> be used for scientific or journalistic purposes.

## Data sources
Unaffordability of healthy foods:
https://ourworldindata.org/food-prices#introduction

BMI:
https://ncdrisc.org/data-downloads-adiposity-urban-rural.html

Countries and regions:
https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv

## Software
You need a functioning installation of miniconda to install the virtual environment. The Miniconda3 version should be download here: https://docs.conda.io/en/latest/miniconda.html. Use version number 23.5.0.

With conda installed, run the following to create or update environment as environment name world-food:

    conda env create -f environment.yml --force

Activate the enviroment:

    conda activate world-food

## Database setup
1. Create a PostgreSQL database named worldfood on your desired server, using port 5432.
2. Open a terminal and navigate to the world-food/ directory.
3. Run the following (you will be prompted to type your database password):

    Bash (UNIX):
        
        bash setup.sh

    PowerShell:
    
        .\setup.ps1


## Running the app
1. While still in the world-food directory, run:

        python run.py

2. Open the URL printed to console in a webrowser.

## Interacting with the app
### Viewing data
In the application you will find several options for filtering by:
* "sub-region" (smaller than continent regions of the world)
* gender (Males, Females, Average)
* urban vs rural population (Urban, Rural, Average)

Note: The averages are rough estimates which do not take relative population sizes into account.

To see the data, simply choose a configuration and click "View selected data" to see the scatter plot. Each mark on the scatter plot represents one country and its membership in a sub-region is indicated by its color.

### Presets
The application allows you to store, load and delete presets.

To load or delete a preset, simply select it from the dropdown menu and click either "Load preset" or "Delete preset".

To save a preset, first choose your preferred configuration, type your desired preset name, and click "Save preset". The chosen preset name must <ins>not</ins> be identical to any existing one. The preset will then immediately appear in the dropdown menu alongside the others.