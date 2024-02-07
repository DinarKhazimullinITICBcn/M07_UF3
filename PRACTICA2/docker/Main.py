import connection
import psycopg2
try :
    connect = connection.conexio()
except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    conn.close()