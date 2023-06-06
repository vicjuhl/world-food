from app import conn, plot_dir
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.use('Agg')

def fetch_test(fname: str):
    cur = conn.cursor()
    sql = """
        SELECT *
        FROM Affordability
        WHERE country = %s
    """
    cur.execute(sql, (fname, ))
    result = cur.fetchone()
    cur.close()
    return result

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

def fetch_region(subregions: list[str]):
    cur = conn.cursor()
    sql = """
        SELECT sub_region, unaf_avg, bmi_avg
		FROM
		(SELECT region,
            sub_region,
            avg(unaffordable) unaf_avg,
            avg((mean_urban + mean_rural)/2) bmi_avg
        FROM Countries
        JOIN bmi
            USING (iso_alpha)
        JOIN affordability
            USING (iso_alpha)
        WHERE sub_region IN %s
        GROUP BY region, country_name, sub_region
		ORDER BY region, sub_region) A
    """    
    cur.execute(sql, [tuple(subregions)])
    result = cur.fetchall()
    cur.close()
    return result

def get_plot(subregions: list[str]):
    """Make scatterplot and return its figure."""    
    result = fetch_region(subregions)
    subregion, affordability, bmi_or_waste = zip(*result)

    df = pd.DataFrame(dict(subregion=subregion, affordability = affordability, bmi_or_waste = bmi_or_waste))

    fig, ax = plt.subplots(figsize=(14, 8))

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

    ax.scatter(df['affordability'], df['bmi_or_waste'], c=df['subregion'].map(colors))
    
    legend_labels = list(colors.keys())
    legend_handles = [plt.Line2D([0], [0], marker='o', color='w', label=label, markerfacecolor=color, markersize=10)
                      for label, color in colors.items()]
    ax.legend(handles=legend_handles, labels=legend_labels, loc='upper right') #TODO: improve legend to only display subregions chosen (without mismatching colors)

    plt.xlabel('Affordability')
    plt.ylabel('BMI or Waste')
    plt.tight_layout()
    return plt

def update_plot(subregions: list[str]) -> None:
    plot = get_plot(subregions)
    plot.savefig(plot_dir / 'plot.png')
    plot.close()
