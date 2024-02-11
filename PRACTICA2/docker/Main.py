import psycopg2
import connection
import create_table
import create
import read
import update
import delete
try :
    conn, conectar = connection.connect()
    create_table.consulta(conn, conectar)
    read.buscar(conectar)
    create.crearCharacter(conn, conectar)
    update.actualitzar(conn, conectar)
    delete.eliminar(conn, conectar)
    read.buscar(conectar)
except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    conn.close()