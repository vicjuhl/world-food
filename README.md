## world-food
By Frederik van Wylich-Muxoll (ckj429) and Victor Kaplan Kjellerup (rgp867)
For the DIS project

# Data sources
https://ourworldindata.org/food-prices#introduction
https://ncdrisc.org/data-downloads-adiposity-urban-rural.html
https://www.fao.org/platform-food-loss-waste/flw-data/en/

# Software
You need a functioning installation of miniconda to install the virtual environment. The Miniconda3 version should be download here: https://docs.conda.io/en/latest/miniconda.html. Use version number 23.1.0.

With conda installed, please do the following to install environment:
    To generate new conda env from env file (default name world-food):
    conda env create -f environment.yml

    To update existing conda env from env file:
    conda env create -f environment.yml --force

# Database setup
1. Create a PostgreSQL database named worldfood on your desired server, using port 5432.
2. Open a terminal and navigate to the world-food/ directory.
3. Run the following command:
    psql -U postgres -d worldfood -f SQL_scripts/data_importer.sql -p 5432
