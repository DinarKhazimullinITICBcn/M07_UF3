def actualitzar(conn, conectar) :
    sql = """update character set character_faction = 'BEAR' where character_id = 3"""
    conectar.execute(sql)
    conn.commit()