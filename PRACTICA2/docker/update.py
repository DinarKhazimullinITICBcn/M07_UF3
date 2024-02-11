def actualitzar(conn, conectar) :
    #Query sql que modifica la faccio de un personatge amb la id 5
    sql = """update character set character_faction = 'BEAR' where character_id = 5"""
    #Executa la Query
    conectar.execute(sql)
    #Guardar els canvis a la b ase de dades
    conn.commit() 