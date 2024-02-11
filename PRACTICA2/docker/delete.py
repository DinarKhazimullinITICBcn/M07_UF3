def eliminar(conn, conectar) :
    #Query per eliminar el personatge amb la id 6
    sql = """delete from character where character_id = 6"""
    #Executar la query
    conectar.execute(sql)
    #Guardar els canvis a la base de dades
    conn.commit() 