from app import conn, plot_dir
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from app.utils.exceptions import NoDataException

matplotlib.use('Agg')

def get_all_regions():
    cur = conn.cursor()
    sql = """
        SELECT sub_region
        FROM (
            SELECT distinct sub_region, region
            FROM Countries
            ORDER BY region, sub_region) C
    """
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    result_list = [elm[0] for elm in result]
    return result_list

def fetch_plot_data(subregions: list[str], rural_urban: str):
    cur = conn.cursor()
    cur.execute(f"""
        SELECT sub_region, unaf_avg, bmi_avg
		FROM
		(SELECT region,
            sub_region,
            AVG(unaffordable) unaf_avg,
            AVG({
                "(mean_urban + mean_rural)/2" if rural_urban == "average"
                else "mean_urban" if rural_urban == "urban"
                else "mean_rural"
            }) bmi_avg
        FROM Countries
        JOIN bmi
            USING (iso_alpha)
        JOIN affordability
            USING (iso_alpha)
        WHERE sub_region IN {tuple(subregions)}
        GROUP BY region, country_name, sub_region
		ORDER BY region, sub_region) A
    """)
    result = cur.fetchall()
    cur.close()
    return result

def get_all_preset_names() -> list[str]:
    cur = conn.cursor()
    sql = """
        SELECT DISTINCT pName
        FROM SubRegionPresets
        ORDER BY pName
    """
    cur.execute(sql)
    p_names = cur.fetchall()
    cur.close()
    return [name[0] for name in p_names]

def get_preset(preset_name: str) -> dict[str, list[str]]:
    cur = conn.cursor()
    sql = """
        SELECT DISTINCT sub_region
        FROM countries
        JOIN SubRegionPresets
            ON sub_region_code = subregioncode
        WHERE pName = %s
    """
    cur.execute(sql, (preset_name, ))
    subregions = cur.fetchall()
    result = {"sub_regions": [reg[0] for reg in subregions]}
    cur.close()
    return result

def save_preset(preset_name: str, checked_subs: list[str]) -> None:
    cur = conn.cursor()
    for sub_name in checked_subs:
        cur.execute(f"""
            INSERT INTO SubRegionPresets
                (pName, subRegionCode)
            VALUES(
                {preset_name},
                (SELECT DISTINCT sub_region_code
                FROM Countries
                WHERE sub_region = {sub_name})
            );
        """)
    conn.commit()
    cur.close()

def delete_preset(preset_name: str) -> None:
    cur = conn.cursor()
    cur.execute(f"""
        DELETE
        FROM subregionpresets
        WHERE pName = {preset_name};
    """)
    conn.commit()
    cur.close()

def get_plot(subregions: list[str], rural_urban: str):
    """Make scatterplot and return its figure."""    
    result = fetch_plot_data(subregions, rural_urban)
    try:
        subregion, affordability, bmi_or_waste = zip(*result)
    except:
        raise NoDataException

    df = pd.DataFrame(dict(subregion=subregion, affordability = affordability, bmi_or_waste = bmi_or_waste))
    chosen_subregions = df['subregion'].drop_duplicates()

    _, ax = plt.subplots(figsize=(12, 8))

    colors = {
        "Antarctica": 'gray',
        "Northern America": 'yellow',
        "Latin America and the Caribbean": 'red',
        "Northern Europe": 'lightblue',
        "Western Europe": 'navy',
        "Eastern Europe": 'blue',
        "Southern Europe": 'royalblue',
        "Northern Africa": 'darkorange',
        "Sub-Saharan Africa": 'goldenrod',
        "Western Asia": 'lime',
        "Central Asia": 'green',
        "Eastern Asia": 'forestgreen',
        "Southern Asia": 'darkgreen',
        "South-eastern Asia": 'springgreen',
        "Australia and New Zealand": 'darkviolet',
        "Micronesia": 'purple',
        "Melanesia": 'magenta',
        "Polynesia": 'plum'
        }

    ax.scatter(df['affordability'], df['bmi_or_waste'], c = df['subregion'].map(colors))
    
    legend_labels = list(chosen_subregions)
    legend_handles = [plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=colors[label], markersize=10)
                      for label in chosen_subregions]
    ax.legend(handles=legend_handles, labels=legend_labels, loc='upper right')

    plt.xlabel('Affordability in %')
    plt.ylabel('BMI')
    plt.tight_layout()
    return plt

def update_plot(subregions: list[str], rural_urban: str) -> None:
    plot = get_plot(subregions, rural_urban)
    plot.savefig(plot_dir / 'plot.png')
    plot.close()
