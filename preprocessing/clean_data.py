import pandas as pd
import pathlib as pl

main_dir = pl.Path(__file__).parent.parent.resolve()
in_dir = main_dir / "data_raw/"
out_dir = main_dir / "data_cleaned/"
out_dir.mkdir(exist_ok=True)

# Unaffordability
print("Copying affordability...")
unaff_path = in_dir / "food-prices.csv"
unaff = pd.read_csv(unaff_path)
unaff = unaff[unaff["Code"].notna()]
unaff.drop(columns=["Entity"], inplace=True)
unaff.rename(columns={"Code": "iso_alpha", "Year": "year_"}, inplace=True)
unaff.to_csv(out_dir / "unaffordability_cleaned.csv", index=False)
print("Copied affordability")

# BMI
print("Copying BMI...")
bmi_path = in_dir / "NCD_RisC_Nature_2019_age_standardised_country.csv"
bmi = pd.read_csv(bmi_path)
bmi = bmi[["ISO", "Sex", "Year", "Mean BMI (urban)", "Mean BMI (rural)"]]
bmi.rename(
    columns= {
        "ISO": "iso_alpha",
        "Sex": "sex",
        "Year": "year_",
        "Mean BMI (urban)": "mean_urban",
        "Mean BMI (rural)": "mean_rural"
    }
    , inplace=True
)
bmi.to_csv(out_dir / "bmi_cleaned.csv", index=False)
print("Copied BMI")

# Countries
print("Copying countries...")
ctr_path = in_dir / "countries.csv"
ctr = pd.read_csv(ctr_path)
ctr = ctr[["alpha-3", "name", "sub-region", "region"]]
ctr.rename(columns={"alpha-3": "iso_alpha", "name": "country_name", "sub-region": "sub_region"}, inplace=True)
ctr.to_csv(out_dir / "countries_cleaned.csv", index=False)
print("Copied countries")