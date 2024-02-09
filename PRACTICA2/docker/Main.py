import connection
import psycopg2
try :
    connect = connection.conn.cursor()
    print(connect)
except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    connection.conn.close()