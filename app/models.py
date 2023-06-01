from app import conn

def fetch_test():
    cur = conn.cursor()
    sql = """
        SELECT *
        FROM Affordability
    """
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    return str(result[0])