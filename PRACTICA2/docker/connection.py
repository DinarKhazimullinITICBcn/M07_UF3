#Importacio de psycopg2 per poder conectar-nos a la db de pgadmin
import psycopg2
#Modul que ens permet connectar-nos i ens retorna les variables conn i conectar
def connect() :
    #Dades de la nostra base de dades.
    conn = psycopg2.connect(
        database = "postgres",
        user = "dinar",
        password = "3412", 
        host = "localhost",
        port = 5432
    )
    conectar = conn.cursor()
    print(conectar)
    return conn, conectar