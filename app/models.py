from app import conn

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