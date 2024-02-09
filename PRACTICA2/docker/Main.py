import psycopg2
import connection
import create_table
import create
import read
import update
try :
    conn, conectar = connection.connect()
    create_table.consulta(conn, conectar)
    create.crearCharacter(conn, conectar)
    read.buscar(conectar)
    update.actualitzar(conn, conectar)
except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    conn.close()