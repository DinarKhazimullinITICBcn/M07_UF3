import psycopg2
import connection
import create_table
import create
import read
try :
    conn, conectar = connection.connect()
    create_table.consulta(conn, conectar)
    create.crear(conectar)
    read.buscar(conectar)
except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    conn.close()