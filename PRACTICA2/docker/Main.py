#Importacio de tots els altres arxius mes psycoph2 per a que funcioni la conexio a la base de dades
import psycopg2
import connection
import create_table
import create
import read
import update
import delete
try :
    #Guardem la informacio obtenguda del return
    conn, conectar = connection.connect()
    #Truquem la funcio consulta amb els parametres conn i conectar per crear la taula
    create_table.consulta(conn, conectar)
    #Truquem la funcio buscar amb el parametre conectar per a que ens mostri tota la informacio de la db
    read.buscar(conectar)
    #Truquem la funcio crearCharacter amb els parametres conn i conectar per crear un personatge
    create.crearCharacter(conn, conectar)
    #Truquem la funcio actualitzar amb els parametres conn i conectar que modificar la informacio de un cert personatge
    update.actualitzar(conn, conectar)
    #Truquem la funcio eliminar amb els parametres conn i conectar amb el que eliminem cert personatge
    delete.eliminar(conn, conectar)
    #Truquem la funcio buscar amb els parametres conectar per tornar a mostrar les dades que hagin canviat
    read.buscar(conectar)
#Si hi ha un error al fer try ens mostrarar un print error amb l'error que ens ha donat
except (Exception, psycopg2.Error) as error:
    print("Error", error)
#Pasi el que pasi sempre es tancara la conexio
finally:
    conn.close()