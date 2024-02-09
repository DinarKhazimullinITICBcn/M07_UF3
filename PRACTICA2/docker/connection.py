import psycopg2

conn = psycopg2.connect(
    database = "postgres",
    user = "dinar",
    password = "3412", 
    host = "localhost",
    port = 5432
)