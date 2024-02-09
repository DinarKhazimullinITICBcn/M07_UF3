import psycopg2
def connect() :
    conn = psycopg2.connect(
        database = "postgres",
        user = "dinar",
        password = "3412", 
        host = "localhost",
        port = 5432
    )
    conectar = conn.cursor()
    print(conectar)