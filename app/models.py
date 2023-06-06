from app import conn, plot_dir
import matplotlib
import matplotlib.pyplot as plt
import os
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

def fetch_region(subregions: list[str]):
    cur = conn.cursor()
    sql = """
        SELECT
            sub_region,
            avg(unaffordable) unaf_avg,
            avg((mean_urban + mean_rural)/2) bmi_avg
        FROM Countries
        JOIN bmi
            USING (iso_alpha)
        JOIN affordability
            USING (iso_alpha)
        WHERE sub_region IN %s
        GROUP BY country_name, sub_region
    """
    cur.execute(sql, [tuple(subregions)])
    result = cur.fetchall()
    cur.close()
    return result

def get_plot(subregions: list[str]):
    """Make scatterplot and return its figure."""    
    result = fetch_region(subregions)
    subregion, affordability, bmi_or_waste = zip(*result)
    plt.scatter(affordability, bmi_or_waste) # TODO: add colorscheme to sub-regions
    plt.xlabel('Affordability')
    plt.ylabel('BMI or Waste')
    return plt

def update_plot(subregions: list[str]) -> None:
    plot = get_plot(subregions)
    plot.savefig(plot_dir / 'plot.png')
    plot.close()

def get_all_regions():
    cur = conn.cursor()
    sql = """
        SELECT DISTINCT sub_region
        FROM Countries
    """
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    result_list = [elm[0] for elm in result]
    return result_list