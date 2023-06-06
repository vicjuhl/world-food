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

def fetch_region(subregion: str):
    
    print("generating results...")
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
        WHERE sub_region = %s
        GROUP BY country_name, sub_region
    """
    cur.execute(sql, (subregion, ))
    result = cur.fetchall()
    cur.close()
    return result

def get_plot(subregion: str):
    """Make scatterplot and return its figure."""    
    print("getting results ...")
    result = fetch_region(subregion)
    subregion, affordability, bmi_or_waste = zip(*result)
    print("creating plot...")
    plt.scatter(affordability, bmi_or_waste) # TODO: add colorscheme to sub-regions
    plt.xlabel('Affordability')
    plt.ylabel('BMI or Waste')
    return plt

def update_plot(subregion) -> None:
    print("updating plot...")
    plot = get_plot(subregion)
    print("saving plot")
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