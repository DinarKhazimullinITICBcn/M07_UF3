def consulta(conn, conectar) :
    #Query de sql per poder crear la taula en cas de que no existeix
    sql = '''CREATE TABLE IF NOT EXISTS CHARACTER(
                    character_id SERIAL PRIMARY KEY,
                    character_name VARCHAR(255) NOT NULL,
                    character_age VARCHAR(255) NOT NULL,
                    character_power VARCHAR(255) NOT NULL,
                    character_faction VARCHAR(255) NOT NULL,
                    character_class VARCHAR(255)
    )'''
    #Executacio de la query
    conectar.execute(sql)
    #Desa els canvis vius en la base de dades
    conn.commit()