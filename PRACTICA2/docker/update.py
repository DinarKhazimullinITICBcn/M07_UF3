def actualitzar(conn, conectar) :
    sql = """update character set character_faction = 'BEAR' where character_id = 5"""
    conectar.execute(sql)
    conn.commit() 