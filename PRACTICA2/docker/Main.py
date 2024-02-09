import psycopg2
import connection
import create
try :
    connection.connect()
    create.consulta()
except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    connection.conn.close()