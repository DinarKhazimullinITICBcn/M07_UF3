def eliminar(conn, conectar) :
    sql = """delete from character where character_id = 6"""
    conectar.execute(sql)
    conn.commit() 