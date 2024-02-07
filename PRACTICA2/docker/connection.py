import psycopg2

def conexio():
    conn = psycopg2.connect(
        database = "postgres",
        user = "dinar",
        password = "3412", 
        host = "localhost",
        port = 5432
    )
    connection = conn.cursor()
    return connection